#!/usr/bin/env python3.9

from person import Person


def fib(_val):
    cache = {0: 0, 1: 1}

    def _fib(val):
        if val in cache:
            return cache.get(val)

        cache[val] = _fib(val - 1) + _fib(val - 2)
        return cache[val]

    return _fib(_val)


def main():
    f = Person(20)
    print(f.get())
    f.set(25)
    print(f.get())
    print(fib(f.get()))


if __name__ == '__main__':
    main()
