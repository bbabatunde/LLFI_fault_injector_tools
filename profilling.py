#!/usr/bin/python
import re

# process whole file
def process_profile_info(c, conn, file_name):
    with open(file_name) as profile_file:
        profile_file = profile_file.readlines()
        for line_no, line in enumerate(profile_file):
            process_line(c, conn, line_no, line)
    return c, conn

# process each line with bamboo index
def process_line(c, conn, line_no, str):
    # thread index
    match = re.search(r'--\sthreadIndex\s[0-9]*', str)
    if match:
        thread_index_info = match.group()
        thread_index = re.findall(r'\b\d+\b', thread_index_info)
        if thread_index:
            thread_index = int(thread_index[0])
        else:
            thread_index = -1
    # instCount
    match = re.search(r'--\sinstCount\s[0-9]*', str)
    if match:
        instCount_info = match.group()
        instCount = re.findall(r'\b\d+\b', instCount_info)
        if instCount:
            instCount = int(instCount[0])
        else:
            instCount = -1
    # dynamicKernelIndex
    match = re.search(r'--\sdynamicKernelIndex\s[0-9]*', str)
    if match:
        staticKernelIndex_info = match.group()
        dynamicKernelIndex = re.findall(r'\b\d+\b', staticKernelIndex_info)
        if dynamicKernelIndex:
            dynamicKernelIndex = int(dynamicKernelIndex[0])
        else:
            dynamicKernelIndex = -1
    # staticKernelIndex
    match = re.search(r'--\sstaticKernelIndex\s[0-9]*', str)
    if match:
        staticKernelIndex_info = match.group()
        staticKernelIndex = re.findall(r'\b\d+\b', staticKernelIndex_info)
        if staticKernelIndex:
            staticKernelIndex = int(staticKernelIndex[0])
        else:
            staticKernelIndex = -1

    c.execute('INSERT OR IGNORE INTO Profiling ' \
              'VALUES (%d, %d, %d, %d,%d);'
              % (line_no, thread_index, instCount, dynamicKernelIndex, staticKernelIndex))
    conn.commit()
    return c, conn

# main
def profiling_main(c,conn, benchmark):
    file_path = "/home/baba/rodinia_3.1/cuda/" + benchmark + "/bamboo_fi/bamboo.profile.txt"
    c, conn = process_profile_info(c,conn, file_path)
    return c, conn



