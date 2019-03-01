# Author: LDT
# Date: 27FEB2019
# Description: This program consists of various functions and classes utilizing abstraction.

from abc import ABC, abstractmethod


class ArrayTransform(ABC):

    @abstractmethod
    def transform(self, user_array):
        pass


class Truncate(ArrayTransform):
    def __init__(self, length):
        self._length = length

    def transform(self, user_array):
        new_array = []
        i = 0
        while i < self._length:
            new_array.append(user_array[i])
            i += 1
        return new_array
