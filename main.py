#
import math
import os
import random
import re
import sys

def avg(*nums):
    nums_len = len(nums)
    sum = 0
    for i in nums:
        sum += i
    return sum/nums_len

if __name__ == '__main__':
    # python basic certificate test
    nums = (2,5)
    res = avg(2,5)
    print(res)
    print('%.2f' % res + '\n')
