#!/usr/bin/python
import os
import filecmp

def create_file_path(benchmark):
    suite_path = "/home/baba/rodinia_3.1/cuda/"
    prog_out_directory = suite_path + benchmark + "/bamboo_fi/prog_output/"
    golden_outfile = suite_path + benchmark + "/bamboo_fi/baseline/results.txt"
    compare_file(golden_outfile, prog_out_directory)

def compare_file(golden_outfile, prog_out_directory):
       for prog_out_file in sorted(os.listdir(prog_out_directory)):
        prog_out_file_index = int(prog_out_file.split("-")[1])
        file_path = prog_out_directory + prog_out_file
        compare_to_golden_output(golden_outfile, file_path)

def compare_to_golden_output(golden_outfile, file_path):
    if filecmp.cmp(golden_outfile, file_path):
        print "true"
    else:
        print "false"

# main
def main():
    benchmark = "gaussian"
    create_file_path(benchmark)
if __name__ == "__main__":
    main()
