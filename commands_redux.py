# Author: LDT
# Date: 1MAR2019
# Title: commands_redux.py
# Purpose: Redoing the commands program utilizing classes and abstraction

import sys
from abc import ABC, abstractmethod


# Handler Parent Class
class Handler(ABC):
    @abstractmethod
    def on_line(self, handle_line):
        pass

    @abstractmethod
    def on_end(self):
        pass


# cat handler class
class CatHandler(Handler):
    def on_line(self, handle_line):
        print(handle_line, end='')

    def on_end(self):
        pass


# head handler class
class HeadHandler(Handler):
    def __init__(self, lines=3):
        self._lines = lines

    def on_line(self, handle_line):
        if self._lines > 0:
            print(handle_line, end='')
            self._lines -= 1

    def on_end(self):
        pass


# tail handler class
class TailHandler(Handler):
    def __init__(self, lines=4):
        self._stuff = []
        self._lines = lines

    def on_line(self, handle_line):
        self._stuff.append(handle_line)

    def on_end(self):
        for i in self._stuff[-4:]:
            print(i, end='')


# unique handler class
class UniqueHandler(Handler):
    def __init__(self):
        self._stuff = set()

    def on_line(self, handle_line):
        self._stuff.add(handle_line)

    def on_end(self):
        for i in self._stuff:
            print(i, end='')


class SortHandler(Handler):
    def __init__(self):
        self._stuff = []

    def on_line(self, handle_line):
        self._stuff.append(handle_line)

    def on_end(self):
        self._stuff.sort()
        for i in self._stuff:
            print(i, end='')


class CountHandler(Handler):
    def __init__(self):
        self._stuff = {}

    def on_line(self, handle_line):
        if handle_line in self._stuff:
            self._stuff[handle_line] += 1
        else:
            self._stuff[handle_line] = 1

    def on_end(self):
        for i in self._stuff:
            print(i)
            print("\nCount: ")
            print(self._stuff[i])
            print("\n")


if __name__ == "__main__":
    # Determine the command
    if sys.argv[1] == "cat":
        handler = CatHandler()
    elif sys.argv[1] == "head":
        handler = HeadHandler()
    elif sys.argv[1] == "tail":
        handler = TailHandler()
    elif sys.argv[1] == "unique":
        handler = UniqueHandler()
    elif sys.argv[1] == "sort":
        handler = SortHandler()
    elif sys.argv[1] == "count":
        handler = CountHandler()

    # Actual Operations
    for line in sys.stdin:
        handler.on_line(line)
    handler.on_end()
