"""
m1.py
"""

import random
import time
import math


def length_longest(lst):
    """Returns the length of the longest (sub-)list in lst"""
    if type(lst) == list:
        biglen = len(lst)
        if all(type(sublist) != list for sublist in lst):
            return len(lst)

        else:

            return max([length_longest(x) for x in lst] + [biglen])
    else:
        return 0

def bubbelsort(aList):
    for i in range(len(aList) - 1):
        for j in range(len(aList) - 1):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]


def foo(n):
    result = 1
    for k in range(3):
        for i in range(n * n):
            result += k * n
    return result


def main():

    print(length_longest(1))  # Should be 0
    print(length_longest([]))  # Should be 0
    print(length_longest([1, 2, 3]))  # Should be 3
    print(length_longest([1, [2, 3]]))  # Should be 2
    print(length_longest([1, [1, 2, 3, 4], 3]))  # Should be 4

    aList = [3, 2, 5, 1, 7]
    bubbelsort(aList)
    print(aList)

    '''
    nums = list(range(2000, 3000, 200))
    times = []
    s = time.perf_counter()
    foo(nums[0])
    e = time.perf_counter()
    base = e - s
    print(base)
    _ests = [(nums[i]/nums[0])**2 for i in range(len(nums))]
    ests = [base*est for est in _ests]
    for num in nums:
        s = time.perf_counter()
        foo(num)
        e = time.perf_counter()
        times.append(e - s)
    print(times)
    print(ests)

    print("const:",[a_i - b_i for a_i, b_i in zip(ests, times)])
    print("foo(1000000) takes", base*((1000000/nums[0])**2))
    '''

if __name__ == "__main__":
    main()

"""
Solution to A2 (Time complexity for bubbelsort):
O(n^2)
loop over list and for each element, loop over again and do operation if if statement is met







Solution to B1 (Time complexity for function foo):
302609
O(n^2)






"""
