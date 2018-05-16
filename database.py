import sqlite3
from profilling import profiling_main


# initialize database
def initDB(db_name):
    """
     Adds Tables to sql database
     """

    conn = sqlite3.connect(db_name + '.db', timeout=15)
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS ' \
              'Injection  (ID INTEGER PRIMARY KEY, ' \
              'ConfigThreadIndex INTEGER,ConfigInstCount INTEGER,' \
              'DynKernelIndex INTEGER, StaticKernelIndex INTEGER, ' \
              'SeedFactor REAL,ErrorDetected TEXT, FiBit INTEGER,' \
              'FiBambooIndex INTEGER,Type TEXT, RuntimeThreadIndex INTEGER, ' \
              'RuntimeInstCount INTEGER, RuntimeFiBit INTEGER, OriginalValue TEXT, ' \
              'CorruptedValue TEXT)')

    c.execute('CREATE TABLE IF NOT EXISTS ' \
              'Profiling (ID INTEGER PRIMARY KEY,ThreadIndex INTEGER, ' \
              'InstructionCount INTEGER,DynamicKernelIndex INTEGER, ' \
              'StaticKernelIndex INTEGER)')

    return c, conn;


# main
def main():
    benchmark_name = raw_input("Enter benchmark pathname:")
    c, conn = initDB(benchmark_name)
    profiling_main(c, conn, benchmark_name)

if __name__ == "__main__":
    main()
