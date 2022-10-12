#!/usr/bin/env python3.9

from person import Person
from numba import njit
from time import perf_counter as timer


@njit
def fib_numba(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return fib_numba(val - 1) + fib_numba(val - 2)


def fib(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return fib(val - 1) + fib(val - 2)


def main():
    f = Person(20)
    print(f.get())
    f.set(47)
    print(f.get())
    f.fib()
    #ages = [30, 35, 40, 45]
    #for age in ages:
        #f.set(age)
        #s = timer()
        #print("python fib of", age, "is", fib(age))
        #e = timer()
        #print(f"time for fib({age}) is {e - s}s with python")

#        s = timer()
#        print("numba fib of", age, "is", fib_numba(age))
#        e = timer()
#        print(f"time for fib({age}) is {e - s}s with numba")

        #s = timer()
        #print("c++ fib of", age, "is", f.fib())
        #e = timer()
        #print(f"time for fib({age}) is {e - s}s with c++")


if __name__ == '__main__':
    main()
