import os
from aoc_utils import aoc_utils
from collections import defaultdict
import time

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': 'D2FE28', 'output': 6},
    {'level': 1, 'input': '38006F45291200', 'output': 9},
    {'level': 1, 'input': 'EE00D40C823060', 'output': 14},
    {'level': 1, 'input': '8A004A801A8002F478', 'output': 16},
    {'level': 1, 'input': '620080001611562C8802118E34', 'output': 12},
    {'level': 1, 'input': 'C0015000016115A2E0802F182340', 'output': 23},
    {'level': 1, 'input': 'A0016C880162017C3686B18A3D4780', 'output': 31},
]

def hexidecimal_to_binary(hexadecimal_string):
    end_length = len(hexadecimal_string) * 4
    hex_int = int(hexadecimal_string, 16)
    hex_binary = bin(hex_int)[2:] # bin() will add '0b' to the front of the binary.
    return hex_binary.zfill(end_length)


def read_packets(bin_str, start_i, end_i, version_total):
    # get packet headers
    packet_version = bin_str[:3]
    version_total[0] += int(packet_version, 2)
    type_id = bin_str[3:6]
    print(packet_version, type_id)
    time.sleep(0.5)

    # get packet body
    body_start_index = 6

    if int(type_id, 2) == 4:
        # read literal value
        print("IN 4:")
        packet_end_index = 0
        for i in range(body_start_index, len(bin_str), 5):
            cur_bits = bin_str[i:i+5]
            print(cur_bits)
            packet_end_index = i+5
            if cur_bits[0] == '0':
                print("AT END")
                break
        print(packet_end_index)
        if packet_end_index < len(bin_str) - 1 and len(bin_str) - packet_end_index > 6:
            # not at end
            read_packets(bin_str[packet_end_index:], version_total)
    else:
        # read with operator
        length_type_id = bin_str[body_start_index]
        print("IN NOT 4:")
        if length_type_id == '0':
            sub_packet_bit_length = int(bin_str[body_start_index+1:body_start_index+16], 2) # 15 bits
            print("IN 0:", bin_str[body_start_index+1:body_start_index+16])
            sub_packets_start_index = body_start_index+16
            sub_packets = bin_str[sub_packets_start_index:sub_packets_start_index+sub_packet_bit_length]
            read_packets(sub_packets, version_total)
        else: # bit is 1
            sub_packet_num = int(bin_str[body_start_index+1:body_start_index+12], 2) # 11 bits
            print("IN 1:", bin_str[body_start_index+1:body_start_index+12])
            sub_packets = bin_str[body_start_index+12:]
            read_packets(sub_packets, version_total)


def answer(problem_input, level, test=None):
    hex_str = problem_input.split('\n')[0]
    bin_str = hexidecimal_to_binary(hex_str)

    if level == 1 or level == 2:
        version_total = [0]
        read_packets(bin_str, version_total)
        return version_total[0]

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
