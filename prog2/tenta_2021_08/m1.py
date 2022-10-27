"""
Solutions to exam tasks for modul 1
Name:
Code:
"""

import random
import time
import math


def count_all(lst, d):
    """ A1: Count all occurencies of d recursively """
    if len(lst) == 0:
        return 0
    if type(lst[0]) == list:
        return count_all(lst[0], d) + count_all(lst[1:], d)
    return (lst[0] == d) + count_all(lst[1:], d)



def c(n):
    if n <= 2:
        return 1
    else:
        return c(n-1) - c(n-3)


def c_mem(n):
    mem = {}
    def _c(n):
        if n<=2:
            return 1
        if n in mem:
            return mem.get(n)
        else:
            mem[n] = _c(n-1) - _c(n-3)
            return mem.get(n)
    return _c(n)


def main():
    print('Test count_all')
    print(count_all([], 1))
    print(count_all([1, 2, 1, 3, [[1], [1, 2, 3]]], 1))

    print('\nTest of c')
    for n in range(25,45,1):
        ts = time.perf_counter()
        c(n)
        te = time.perf_counter()
        print(n,round(te-ts,3))


    print('\nTest of c_mem')
    print('c_mem(3):', c_mem(3))
    print('c_mem(4):', c_mem(4))
    print('c_mem(5):', c_mem(5))
    print('c_mem(9):', c_mem(9))

    print('c_mem(100):', c_mem(100))

    print('\nCode for task B1')


if __name__ == "__main__":
    main()
    print('Over and out')


"""
Answer to task B1:
87694 sekunder eller	24,35 timmar




"""
