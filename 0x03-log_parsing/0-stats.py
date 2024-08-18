#!/usr/bin/python3

import sys


def print_stats(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size = 0
status_code = 0
counter = 0
dict_status_code = {"200": 0,
                    "301": 0,
                    "400": 0,
                    "401": 0,
                    "403": 0,
                    "404": 0,
                    "405": 0,
                    "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                file_size += int(parsed_line[0])
                status_code = parsed_line[1]

                if (status_code in dict_status_code.keys()):
                    dict_status_code[status_code] += 1

            if (counter == 10):
                print_stats(dict_status_code, file_size)
                counter = 0

finally:
    print_stats(dict_status_code, file_size)
