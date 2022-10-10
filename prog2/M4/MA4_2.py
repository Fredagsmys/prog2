#!/usr/bin/env python3.9

from person import Person
from numba import njit
from time import perf_counter as toc

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
    f.set(35)
    print(f.get())
    age = f.get()
    start = toc()
    print("python fib of", age, "is", fib(age))
    end = toc()
    print("time for python:",end-start,"s")
    start = toc()
    print("numba fib of", age, "is", fib_numba(age))
    end = toc()
    print("time for numba:",end-start,"s")
    start = toc()
    print("c++ fib of", age, "is", f.fib())
    end = toc()
    print("time for c++:",end-start,"s")

if __name__ == '__main__':
    main()
