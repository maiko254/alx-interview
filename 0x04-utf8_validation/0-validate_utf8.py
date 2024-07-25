#!/usr/bin/python3
"""Module checking if a dataset is represents a valid UTF-8 encoding"""
def validUTF8(data):
    """Validate UTF-8 encoding of a sequence of characters
    """
    num_bytes = 0
    for byte in data:
        byte = byte & 0xFF
        if num_bytes:
            if byte >> 6 != 2:
                return False
            num_bytes -= 1
            continue
        while (1 << abs(7 - num_bytes)) & byte:
            num_bytes += 1
        if num_bytes == 1 or num_bytes > 4:
            return False
        num_bytes = max(num_bytes - 1, 0)
    return num_bytes == 0
