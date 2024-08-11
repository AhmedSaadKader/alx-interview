#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 75
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 84
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
