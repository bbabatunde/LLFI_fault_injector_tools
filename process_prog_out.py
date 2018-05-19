#!/usr/bin/python
import os
import filecmp


def create_file_path(c, conn, benchmark):
    suite_path = "/home/baba/rodinia_3.1/cuda/"
    prog_out_directory = suite_path + benchmark + "/bamboo_fi/prog_output/"
    golden_outfile = suite_path + benchmark + "/bamboo_fi/baseline/results.txt"
    c, conn = compare_file(c, conn, golden_outfile, prog_out_directory)
    return c, conn


def compare_file(c, conn, golden_outfile, prog_out_directory):
    index = 0
    for prog_out_file in sorted(os.listdir(prog_out_directory)):
        prog_out_file_index = int(prog_out_file.split("-")[1])
        file_path = prog_out_directory + prog_out_file
        if filecmp.cmp(golden_outfile, file_path):
            filecmp_boolean = 1
            c.execute('INSERT OR IGNORE INTO ProgOut ' \
                      'VALUES (%d,%d,%d);'
                      % (index, prog_out_file_index, filecmp_boolean
                         ))
        else:
            filecmp_boolean = 0
            c.execute('INSERT OR IGNORE INTO ProgOut ' \
                      'VALUES (%d,%d,%d);'
                      % (index, prog_out_file_index, filecmp_boolean
                         ))
        conn.commit()
        index += 1

    return c, conn


# main
def prog_out_main(c, conn, benchmark):
    c, conn = create_file_path(c, conn, benchmark)
    return c, conn
