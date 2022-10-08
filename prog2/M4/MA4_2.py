#!/usr/bin/env python3.9

from person import Person


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
    print("fib of",f.get(),"is", fib(f.get()))


if __name__ == '__main__':
    main()
