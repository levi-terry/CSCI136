# Author: LDT
# Date: 27FEB2019
# Description: This program consists of various functions and classes utilizing abstraction.

from abc import ABC, abstractmethod


# Parent Class
class ArrayTransform(ABC):
    # This method should do nothing, it is an abstract method which much be implemented
    # via other classes
    @abstractmethod
    def transform(self, user_array):
        pass


# Child Class
class Truncate(ArrayTransform):
    def __init__(self, length):
        self._length = length

    # This method fully implements the transform abstract method inherited from parent class
    def transform(self, user_array):
        new_array = []
        i = 0
        while i < self._length:
            new_array.append(user_array[i])
            i += 1
        return new_array
