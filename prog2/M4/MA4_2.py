#!/usr/bin/env python3.9

from person import Person
from numba import njit


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
    f.set(25)
    print(f.get())
    age = f.get()
    print("python fib of", age, "is", fib(age))
    print("numba fib of", age, "is", fib_numba(age))
    print("c++ fib of", age, "is", f.fib())


if __name__ == '__main__':
    main()
