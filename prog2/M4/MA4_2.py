#!/usr/bin/env python3.9

from person import Person


def fib(n):
    print("hej")
    if n <= 1:
        return n

    else:
        return fib(n - 1) + fib(n - 2)




def main():
    f = Person(20)
    print(f.get())
    f.set(15)
    print(f.get())
    print(fib(f.get()))


if __name__ == '__main__':
    main()
