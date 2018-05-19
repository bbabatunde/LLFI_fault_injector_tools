#!/usr/bin/python
import re
import os


# creates bamboo output filepath
def create_file_path(c, conn, benchmark):
    suite_path = "/home/baba/rodinia_3.1/cuda/"
    err_out_directory = suite_path + benchmark + "/bamboo_fi/err_output/"
    c, conn = process_err_out(c, conn, err_out_directory)
    return c, conn


# process each file
def process_err_out(c, conn, err_out_directory):
    for err_out_file in sorted(os.listdir(err_out_directory)):
        err_out_file_index = int(err_out_file.split("-")[1])
        file_path = err_out_directory + err_out_file
        with open(file_path) as std_out:
            err_out = err_out.readlines()
            for str in err_out:
                # fiThreadIndex
                match = re.search(r'--\sfiThreadIndex:\s[0-9]*', str)
                if match:
                    fi_thread_index_info = match.group()
                    fi_thread_index = re.findall(r'\b\d+\b', fi_thread_index_info)
                    if fi_thread_index:
                        fi_thread_index = int(fi_thread_index[0])
                # fiInstCount
                match = re.search(r'\sfiInstCount:\s[0-9]*', str)
                if match:
                    fiInstCount_info = match.group()
                    fiInstCount = re.findall(r'\b\d+\b', fiInstCount_info)
                    if fiInstCount:
                        fiInstCount = int(fiInstCount[0])

                # fiDynamicKernelIndex
                match = re.search(r'\sfiDynamicKernelIndex:\s[0-9]*', str)
                if match:
                    fiDynamicKernelIndex_info = match.group()
                    fiDynamicKernelIndex = re.findall(r'\b\d+\b', fiDynamicKernelIndex_info)
                    if fiDynamicKernelIndex:
                        fiDynamicKernelIndex = int(fiDynamicKernelIndex[0])

                # fiStaticKernelIndex
                match = re.search(r'\sfiStaticKernelIndex:\s[0-9]*', str)
                if match:
                    fiStaticKernelIndex_info = match.group()
                    fiStaticKernelIndex = re.findall(r'\b\d+\b', fiStaticKernelIndex_info)
                    if fiStaticKernelIndex:
                        fiStaticKernelIndex = int(fiStaticKernelIndex[0])

                # fiBit
                match = re.search(r'\sfiBit:\s[0-9]*', str)
                if match:
                    fiBit_info = match.group()
                    fiBit = re.findall(r'\b\d+\b', fiBit_info)
                    if fiBit:
                        fiBit = int(fiBit[0])

                # fiBambooIndex
                match = re.search(r'\sfiBambooIndex:\s[0-9]*', str)
                if match:
                    fiBambooIndex_info = match.group()
                    fiBambooIndex = re.findall(r'\b\d+\b', fiBambooIndex_info)
                    if fiBambooIndex:
                        fiBambooIndex = int(fiBambooIndex[0])

                # deviceFiThreadIndex
                match = re.search(r'\sdeviceFiThreadIndex:\s[0-9]*', str)
                if match:
                    deviceFiThreadIndex_info = match.group()
                    deviceFiThreadIndex = re.findall(r'\b\d+\b', deviceFiThreadIndex_info)
                    if deviceFiThreadIndex:
                        deviceFiThreadIndex = int(deviceFiThreadIndex[0])

                # deviceFiThreadIndex
                match = re.search(r'\sdeviceFiInstCount:\s[0-9]*', str)
                if match:
                    deviceFiInstCount_info = match.group()
                    deviceFiInstCount = re.findall(r'\b\d+\b', deviceFiInstCount_info)
                    if deviceFiInstCount:
                        deviceFiInstCount = int(deviceFiInstCount[0])

                # devicefiBit
                match = re.search(r'\sfiBit:\s[0-9]*\(.*?\)', str)
                if match:
                    devicefiBit_info = match.group()
                    devicefiBit = re.findall(r'\b\d+\b', devicefiBit_info)
                    if devicefiBit:
                        devicefiBit = int(devicefiBit[0])

                # Original Value
                match = re.search(r'\sOriginal\sValue:\s[0-9]*\s[\*\*]', str)
                if match:
                    original_value_info = match.group()
                    original_value = re.findall(r'\b\d+\b', original_value_info)
                    if original_value:
                        original_value = ''.join(original_value)

                # TODO
                # Corrupted Value
                match = re.search(r'\sCorrupted\sValue:\s', str)
                if match:
                    corrupted_value_info = match.group()
                    corrupted_value = re.findall(r'\sCorrupted\sValue:\s(.*)', corrupted_value_info)
                    if corrupted_value:
                        corrupted_value = ''.join(corrupted_value)

                # Error Detected
                match = re.search(r'Error\sDetected:\s.*$', str)
                if match:
                    error_detected_info = match.group()
                    error_detected = re.findall(r'Error\sDetected:\s(.*)', error_detected_info)
                    if error_detected:
                        error_detected = ''.join(error_detected)

        c.execute('INSERT OR IGNORE INTO ErrorOutput ' \
                  'VALUES (%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,\'%s\',\'%s\',\'%s\');'
                  % (err_out_file_index, fi_thread_index, fiInstCount, fiDynamicKernelIndex,
                     fiStaticKernelIndex, fiBit, fiBambooIndex, deviceFiThreadIndex, deviceFiInstCount,
                     devicefiBit, original_value, corrupted_value, error_detected
                     ))
        conn.commit()
    return c, conn


# main
def err_out_main(c, conn, benchmark):
    c, conn = create_file_path(c, conn, benchmark)
    return c, conn
