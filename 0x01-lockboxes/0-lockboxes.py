#!/usr/bin/python3
"""You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    number_of_boxes = len(boxes)
    keys_available = set(boxes[0])
    boxes_opened = set([0])

    while keys_available:
        new_key = keys_available.pop()
        if new_key not in boxes_opened and new_key < number_of_boxes:
            boxes_opened.add(new_key)
            keys_available.update(boxes[new_key])

    return len(boxes_opened) == number_of_boxes
