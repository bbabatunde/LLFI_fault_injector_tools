import sqlite3
from profilling import profiling_main
from process_err_output import err_out_main
from process_llvmir import llvm_main
from process_std_output import std_out_main


# initialize database
def initDB(db_name):
    """
     Adds Tables to sql database
     """

    conn = sqlite3.connect(db_name + '.db', timeout=15)
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS ' \
              'ErrorOutput (ID INTEGER PRIMARY KEY, ' \
              'FiThreadIndex INTEGER,FiInstCount INTEGER,' \
              'FiDynKernelIndex INTEGER, FiStaticKernelIndex INTEGER, ' \
              'FiBit INTEGER,' \
              'FiBambooIndex INTEGER, RuntimeThreadIndex INTEGER, ' \
              'RuntimeInstCount INTEGER, RuntimeFiBit INTEGER, OriginalValue TEXT, ' \
              'CorruptedValue TEXT,ErrorDetected TEXT)')

    c.execute('CREATE TABLE IF NOT EXISTS ' \
              'StdOutput (ID INTEGER PRIMARY KEY, ' \
              'FiThreadIndex INTEGER,FiInstCount INTEGER,' \
              'FiDynKernelIndex INTEGER, FiStaticKernelIndex INTEGER, ' \
              'FiBit INTEGER,' \
              'FiBambooIndex INTEGER, RuntimeThreadIndex INTEGER, ' \
              'RuntimeInstCount INTEGER, RuntimeFiBit INTEGER, OriginalValue TEXT, ' \
              'CorruptedValue TEXT)')

    c.execute('CREATE TABLE IF NOT EXISTS ' \
              'profiling (ID INTEGER PRIMARY KEY,ThreadIndex INTEGER, ' \
              'InstructionCount INTEGER,DynamicKernelIndex INTEGER, ' \
              'StaticKernelIndex INTEGER)')

    c.execute('CREATE TABLE IF NOT EXISTS ' \
              'LlvmOutput (ID INTEGER PRIMARY KEY,BambooIndex INTEGER, ' \
              'KernelId INTEGER,KernelLine INTEGER)')
    return c, conn;


# main
def main():

    benchmark_name = raw_input("Enter benchmark pathname:")
    process = raw_input("Enter process type:").lower()

    c, conn = initDB(benchmark_name)

    if(process == "a"):
        c, conn = profiling_main(c, conn, benchmark_name)
        c, conn = err_out_main(c, conn, benchmark_name)
        c, conn = llvm_main(c, conn, benchmark_name)
        c, conn = std_out_main(c, conn, benchmark_name)
    elif(process == "p"):
        c, conn = profiling_main(c, conn, benchmark_name)
    elif(process == "e"):
        c, conn = err_out_main(c, conn, benchmark_name)
    elif(process == "l"):
        c, conn = llvm_main(c, conn, benchmark_name)
    elif(process == "s"):
        c, conn = std_out_main(c, conn, benchmark_name)
    else:
        print "Wrong Input"

if __name__ == "__main__":
    main()
