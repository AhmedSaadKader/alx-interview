#!/usr/bin/python3
"""Prime Game"""


def isWinner(rounds, nums):
    """isWinner function"""
    if rounds <= 0 or nums is None:
        return None
    if rounds != len(nums):
        return None

    ben = 0
    maria = 0

    one_list = [1] * (sorted(nums)[-1] + 1)

    one_list[0], one_list[1] = 0, 0
    for i in range(2, len(one_list)):
        for j in range(2, len(one_list)):
            try:
                one_list[i * j] = 0
            except (ValueError, IndexError):
                break

    for i in nums:
        if sum(one_list[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"

    if maria > ben:
        return "Maria"

    return None
