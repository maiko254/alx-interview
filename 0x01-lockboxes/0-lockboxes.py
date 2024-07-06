#!/usr/bin/python3
"""
Module implementing a function that checks if all boxes in a list
can be opened
"""


def canUnlockAll(boxes):
    """
    Function taking a list of list of boxes with keys(positive integer) that
    open other boxes in the list and returns True if all boxes can be opened,
    False otherwise
    The first box in the list is already opened
    """
    if not boxes:
        return False
    if not isinstance(boxes, list):
        return False
    if not boxes[0]:
        return False
    if not isinstance(boxes[0], list):
        return False
    if len(boxes) == 1:
        return True
    
    keys = [0]

    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)

    if len(keys) == len(boxes):
        return True
    return False
