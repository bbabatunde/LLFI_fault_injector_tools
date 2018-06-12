# LLFI_fault_injector_tools
Utilized regular expressions to parse LLFI output files and create a SQL database

# database.py

This script initiate the database and calls the other scripts depending on the process type

**run** python database.py

Enter benchmark name: e.g gaussian

Enter process type: e.g a

process type

- a: processes and create database for all LLFI output
- p: processes and create database for profilling file
- e: processes and create database for error output
- l: processes and create database for LLVM IR file
- s: processes and create database for standard output folder
- pr: processes and create database for program output folder


# process_error_output.py

Processes files in /bamboo_fi/err_output

**Modification** 

Change **suite_path = "/home/baba/rodinia_3.1/cuda/"** in **create_file_path**  function to your file path

May require more changes in **create_file_path** function if not using rodinia benchmark suite

## process_llvmir.py

Process the LLVM IR file in /bamboo_fi after adding debug info to the LLVM file using llvm-dis -show-annotation **LLVM IR file name**

**Modification** 

 Change **file_path = "/home/baba/rodinia_3.1/cuda/" +benchmark+ "/bamboo_fi/" +benchmark+ "_injection.ll.ll"** in llvm_main funtion to your file path

## process_prog_out.py
Compares the golden output with the program output files in /bamboo_fi/prog_output. Store comparison results as either 1's for true and 0's for false

**Modification** 

create_file_path function requires changes to golden_outfile path and suite_path

 
## process_std_output.py
Processes files in /bamboo_fi/std_output 

**Modification** 

Change **suite_path = "/home/baba/rodinia_3.1/cuda/"** in **create_file_path**  function to your file path

## profilling.py
Processes the bamboo.profile.txt file

**Modification** 

 Change **file_path = "/home/baba/rodinia_3.1/cuda/" + benchmark + "/bamboo_fi/bamboo.profile.txt"** in profilling_main funtion to your file path
