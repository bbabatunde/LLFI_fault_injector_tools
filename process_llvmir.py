#!/usr/bin/python
import re

def process_reg(c, conn, file_name):
    kernel_start_rnages = []
    kernel_end_ranges = []
    kernel_id = 0
    index = 0
    with open(file_name) as bamboo_llvmfile:
        bamboo_llvmfile = bamboo_llvmfile.readlines()
        for line_number, line in enumerate(bamboo_llvmfile):
            if re.search(r'define\svoid\s@_+[^.{^,\(}$]+\((.*?)\)\salwaysinline', line):
                kernel_start_rnages.append(line_number)
            elif re.search(r'ret[\s]void', line):
                if len(kernel_start_rnages) == 0:
                    continue
                kernel_end_ranges.append(line_number)
        for start, end in kernel_start_rnages, kernel_end_ranges:
            kernel_id += 1
            c, conn, index = process_kernel(c, conn, index, kernel_id, start, end, bamboo_llvmfile)
    return c, conn


def process_kernel(c, conn, index, kernel_id, start, end, llvmfile):
    for line in (llvmfile[start:end]):
        if re.search(r'bamboo_index', line):
            c, conn, index = process_bamboo_line(c, conn,index, kernel_id, line)
    return c, conn, index

def process_bamboo_line(c, conn, index, kernel_id, str):
    # bamboo_index
    bamboo_index = -1
    debug_line = -1
    match = re.search(r'bamboo_index\s[\!][0-9]*', str)
    if match:
        bamboo_index_info = match.group()
        bamboo_index = re.findall(r'\b\d+\b', bamboo_index_info)
        if bamboo_index:
            bamboo_index = int(bamboo_index[0])

    match = re.search(r'debug\sline\s[\=]\s[0-9]*', str)
    if match:
        debug_line_info = match.group()
        debug_line = re.findall(r'\b\d+\b', debug_line_info)
        if debug_line:
            debug_line = int(debug_line[0])
    c.execute('INSERT OR IGNORE INTO LlvmOutput VALUES (%d,%d,%d,%d);'
              % (index, bamboo_index, kernel_id, debug_line))
    conn.commit()
    index += 1
    return c, conn, index

# main
def llvm_main(c, conn, benchmark):
    file_name = "/home/baba/rodinia_3.1/cuda/" +benchmark+ "/bamboo_fi/" +benchmark+ "_injection.ll.ll"
    c, conn = process_reg(c, conn, file_name)
    return c, conn

