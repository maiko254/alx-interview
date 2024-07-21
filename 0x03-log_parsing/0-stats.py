#!/usr/bin/python3
import sys
import re
import signal


pattern = r'^\S+\s*-\s*\[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\S+) (\d+)$'
match_count = 0

size = 0
count_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def print_stats():
    global size, count_codes
    print(f"File size: {size}")
    for code in sorted(count_codes.keys()):
        if count_codes[code] > 0:
            print(f"{code}: {count_codes[code]}")


def handle_interrupt(signal, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line = line.strip()
        match = re.match(pattern, line)
        if match:
            match_count += 1
            status_code = match.group(1)
            size = int(match.group(2))
            count_codes[status_code] = count_codes.get(status_code, 0) + 1
            if match_count % 10 == 0:
                print_stats()
        else:
            continue
except Exception as e:
    print(f"Error: {e}")

print_stats()
