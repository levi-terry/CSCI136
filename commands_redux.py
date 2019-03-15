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
    def on_line(self, handle_line):
        pass

    def on_end(self):
        pass


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

    # Actual Operations
    for line in sys.stdin:
        handler.on_line(line)
    handler.on_end()
