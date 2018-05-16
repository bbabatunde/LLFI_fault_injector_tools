#!/usr/bin/python
import re

def process_reg(file_name):
    kernel_start_rnages = []
    kernel_end_ranges = []
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
            process_kernel(start, end, bamboo_llvmfile)


def process_kernel(start, end, llvmfile):
    for line in (llvmfile[start:end]):
        if re.search(r'bamboo_index', line):
            process_bamboo_line(line)


def process_bamboo_line(str):
    # bamboo_index
    match = re.search(r'bamboo_index\s[\!][0-9]*', str)
    if match:
        bamboo_index_info = match.group()
        bamboo_index = re.findall(r'\b\d+\b', bamboo_index_info)
        if bamboo_index:
            bamboo_index = int(bamboo_index[0])
            print bamboo_index

    match = re.search(r'debug\sline\s[\=]\s[0-9]*', str)
    if match:
        debug_line_info = match.group()
        debug_line = re.findall(r'\b\d+\b', debug_line_info)
        if debug_line:
            debug_line = int(debug_line[0])
            print debug_line

# main
def main():
    file_name = "/home/baba/rodinia_3.1/cuda/bfs/bamboo_fi/bfs_injection.ll.ll"
    process_reg(file_name)


if __name__ == "__main__":
    main()
