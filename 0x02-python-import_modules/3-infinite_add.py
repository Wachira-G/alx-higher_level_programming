#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    total = 0
    if not args:
        pass
    else:
        for item in args:
            total += int(item)
    print(total)
