#!/usr/bin/python
import re
import os


def create_file_path(benchmark):
    suite_path = "/home/baba/rodinia_3.1/cuda/"
    std_out_directory = suite_path + benchmark + "/bamboo_fi/std_output/"
    process_std_out(std_out_directory)


def process_std_out(std_out_directory):
    for std_out_file in sorted(os.listdir(std_out_directory)):
        std_out_file_index = int(std_out_file.split("-")[1])
        file_path = std_out_directory + std_out_file
        process_file(file_path)


def process_file(file_path):
    with open(file_path) as std_out:
        std_out = std_out.readlines()
        for line in std_out:
            process_line(line)


# process each line with bamboo index
def process_line(str):
    # fiThreadIndex
    match = re.search(r'--\sfiThreadIndex:\s[0-9]*', str)
    if match:
        fi_thread_index_info = match.group()
        fi_thread_index = re.findall(r'\b\d+\b', fi_thread_index_info)
        if fi_thread_index:
            fi_thread_index = int(fi_thread_index[0])
        else:
            fi_thread_index = -1

    # fiInstCount
    match = re.search(r'\sfiInstCount:\s[0-9]*', str)
    if match:
        fiInstCount_info = match.group()
        fiInstCount = re.findall(r'\b\d+\b', fiInstCount_info)
        if fiInstCount:
            fiInstCount = int(fiInstCount[0])
        else:
            fiInstCount = -1

    # fiDynamicKernelIndex
    match = re.search(r'\sfiDynamicKernelIndex:\s[0-9]*', str)
    if match:
        fiDynamicKernelIndex_info = match.group()
        fiDynamicKernelIndex = re.findall(r'\b\d+\b', fiDynamicKernelIndex_info)
        if fiDynamicKernelIndex:
            fiDynamicKernelIndex = int(fiDynamicKernelIndex[0])
        else:
            fiDynamicKernelIndex = -1

    # fiStaticKernelIndex
    match = re.search(r'\sfiStaticKernelIndex:\s[0-9]*', str)
    if match:
        fiStaticKernelIndex_info = match.group()
        fiStaticKernelIndex = re.findall(r'\b\d+\b', fiStaticKernelIndex_info)
        if fiStaticKernelIndex:
            fiStaticKernelIndex = int(fiStaticKernelIndex[0])
        else:
            fiStaticKernelIndex = -1

    # fiBit
    match = re.search(r'\sfiBit:\s[0-9]*', str)
    if match:
        fiBit_info = match.group()
        fiBit = re.findall(r'\b\d+\b', fiBit_info)
        if fiBit:
            fiBit = int(fiBit[0])
        else:
            fiBit = -1

    # fiBambooIndex
    match = re.search(r'\sfiBambooIndex:\s[0-9]*', str)
    if match:
        fiBambooIndex_info = match.group()
        fiBambooIndex= re.findall(r'\b\d+\b', fiBambooIndex_info)
        if fiBambooIndex:
            fiBambooIndex = int(fiBambooIndex[0])
        else:
            fiBambooIndex = -1

    # deviceFiThreadIndex
    match = re.search(r'\sdeviceFiThreadIndex:\s[0-9]*', str)
    if match:
        deviceFiThreadIndex_info = match.group()
        deviceFiThreadIndex= re.findall(r'\b\d+\b', deviceFiThreadIndex_info)
        if deviceFiThreadIndex:
            deviceFiThreadIndex = int(deviceFiThreadIndex[0])
        else:
            deviceFiThreadIndex = -1

    # deviceFiThreadIndex
    match = re.search(r'\sdeviceFiInstCount:\s[0-9]*', str)
    if match:
        deviceFiInstCount_info = match.group()
        deviceFiInstCount = re.findall(r'\b\d+\b', deviceFiInstCount_info)
        if deviceFiInstCount:
            deviceFiInstCount = int(deviceFiInstCount[0])
        else:
            deviceFiInstCount = -1

    # devicefiBit
    match = re.search(r'\sfiBit:\s[0-9]*\(.*?\)', str)
    if match:
        fiBit_info = match.group()
        fiBit = re.findall(r'\b\d+\b', fiBit_info)
        if fiBit:
            fiBit = int(fiBit[0])
        else:
            fiBit = -1

    # Original Value
    match = re.search(r'\sOriginal\sValue:\s[0-9]*\s[\*\*]', str)
    if match:
        original_value_info = match.group()
        original_value = re.findall(r'\b\d+\b', original_value_info)
        if original_value:
            original_value = ''.join(original_value)
        else:
            original_value = ""

    # Corrupted Value
    match = re.search(r'\sCorrupted\sValue:\s', str)
    if match:
        corrupted_value_info = match.group()
        corrupted_value = re.findall(r'^[^0-9a-zA-Z]+$', corrupted_value_info)
        print corrupted_value
        if corrupted_value:
            corrupted_value = ''.join(corrupted_value)
        else:
            corrupted_value = ""


def database_insert(thread_index, instCount, dynamicKernelIndex, staticKernelIndex):
    print "hey"

# main
def main():
    benchmark = "gaussian"
    create_file_path(benchmark)


if __name__ == "__main__":
    main()
