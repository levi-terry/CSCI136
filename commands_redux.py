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
    def on_line(self, handle_line):
        count = 0
        while count < 3:
            print(handle_line, end='')
            count += 1

    def on_end(self):
        pass


# tail handler class
class TailHandler(Handler):
    def on_line(self, handle_line):
        pass

    def on_end(self):
        pass


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
