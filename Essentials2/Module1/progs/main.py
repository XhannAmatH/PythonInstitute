#   Author  :   XhannAmatH

from sys import path

path.append('../modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(zeroes)
print(ones)
print(module.sum1(zeroes))
print(module.prod1(ones))
