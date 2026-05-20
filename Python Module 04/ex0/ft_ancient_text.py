#!/usr/bin/env python3
import sys
import typing

def main():
    if (len(sys.argv) == 1):
        print(f"Usage: {sys.argv[0]} <file>")
        return
    elif (len(sys.argv) != 2):
        print("Invalid input quantity! Please retry")
        return
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        f = io.read(file_name)
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    main()