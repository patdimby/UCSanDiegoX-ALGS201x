# python3

import queue

def find_mismatch(text):
    opening_brackets_stack = []
    opens = queue.SimpleQueue()
    closes = queue.LifoQueue()
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
