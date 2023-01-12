#!/bin/python3

import math
import os
import random
import re
import sys


def array_sum(array, row, column):
    temp_sum = 0
    # top row
    temp_sum += array[row][column]
    temp_sum += array[row][column + 1]
    temp_sum += array[row][column + 2]
    # center row
    temp_sum += array[row + 1][column + 1]
    # bottom row
    temp_sum += array[row + 2][column]
    temp_sum += array[row + 2][column + 1]
    temp_sum += array[row + 2][column + 2]

    return temp_sum


if __name__ == '__main__':

    arr = []

    # To fill the array
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -63
    for i in range(4):
        for j in range(4):
            current_sum = array_sum(arr, i, j)
            if current_sum > max_sum:
                max_sum = current_sum
    print(max_sum)


