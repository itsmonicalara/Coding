#!/bin/python3

import math
import os
import random
import re
import sys


def num_to_binary(num):
    binary_list = []
    current = 0
    longest = 0
    while int(num) > 0:
        remainder = num % 2
        num = num / 2
        binary_list.insert(0, int(remainder))

    for ele in binary_list:
        if ele == 1:
            current += 1
        else:
            longest = max(current, longest)
            current = 0
    print(max(current, longest))


if __name__ == '__main__':
    n = int(input().strip())
    num_to_binary(n)
