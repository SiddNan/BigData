#!/usr/bin/env python
import sys

def main():
    current_word = None
    current_count = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            key, value = line.split('\t', 1)
        except ValueError:
            continue
        if key.startswith("LongValueSum:"):
            key = key[len("LongValueSum:"):]
        try:
            count = int(value)
        except ValueError:
            continue
        if current_word == key:
            current_count += count
        else:
            if current_word is not None:
                print(f"{current_word}\t{current_count}")
            current_word = key
            current_count = count
    if current_word is not None:
        print(f"{current_word}\t{current_count}")

if __name__ == "__main__":
    main()
