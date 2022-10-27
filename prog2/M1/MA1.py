"""
Solutions to module 1
Student: Max Mattsson
Mail: Maximilian.Mattsson.9867@student.uu.se
Reviewed by: Fredrik Hammarberg
Reviewed date: 2022-09-07
"""

import random
import time
from math import log

from tokenize import String


def power(x, n):  # Optional

    if n == 0:
        return 1

    if n < 0:
        return power(1 / x, n)

    return power(x, n - 1) * x


def power_fast(x, n):
    if n == 0:
        return 1
    if n < 0:
        return power_fast(1 / x, n * -1)
    else:
        # if even x^n = (x^n/2)^2 and if odd: x^n = x*(x^n/2)^2
        if n % 2 == 0:
            return power_fast(x, n // 2) * power_fast(x, n // 2)
        else:
            return power_fast(x, n // 2) * power_fast(x, n // 2) * x


def multiply(m, n):  # Compulsory

    if m == 0:
        return 0

    return multiply(m - 1, n) + n


def divide(t, n):  # Optional

    if t < n:
        return 0

    return divide(t - n, n) + 1


def harmonic(n):  # Compulsory

    if n == 0:
        return 0

    return harmonic(n - 1) + 1 / n


def digit_sum(x):  # Optional

    if x == 0:
        return 0

    return digit_sum(x // 10) + x % 10


def get_binary(x):  # Optional

    if x == 0:
        return ""
    return get_binary(x // 2) + str(x % 2)


def reverse(s):  # Optional

    if s == "":
        return ""
    return s[-1] + reverse(s[0:-1])


def largest(a):  # Compulsory
    if len(a) == 1:
        return a[0]
    return largest([a[0] if a[0] > a[1] else a[1]] + a[2:])


def count(x, s):
    if len(s) == 0:
        return 0
    if s[0] == x:
        return count(x, s[1:]) + 1
    elif type(s[0]) == list:
        return count(x, s[0]) + count(x, s[1:])
    else:
        return count(x, s[1:])


def zippa(l1, l2):  # Compulsory
    if len(l1) == 0 or len(l2) == 0:
        return l1 + l2
    return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])


def bricklek(f, t, h, n):  # Compulsory
    if n == 0:
        return []
    else:
        return bricklek(f, h, t, n - 1) + [f"{f}->{t}"] + bricklek(h, t, f, n - 1)


def fib(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibtiming(fib):
    times = []
    print(fib.__name__)
    for n in [30, 31, 32]:
        tstart = time.perf_counter()
        fib(n)
        tstop = time.perf_counter()
        times.append(tstop - tstart)
    print(times[-1] / times[-2])
    return times


def exchange(a, coins):
    if a == 0:
        return 1
    if a < 0:
        return 0
    if len(coins) == 0:
        return 0

    return exchange(a, coins[1:]) + exchange(a - coins[0], coins)


def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    print(f"exchange: {exchange(10, [1, 2])}")
    print(power(3, 4))
    print(power_fast(3, -4))
    print(multiply(2, 2))
    print(divide(10, 2))
    print(harmonic(4))
    print(digit_sum(91))
    print(get_binary(9))
    print(reverse("programmeringsteknik 2"))
    print(largest([0, 3, 2, 3, 4, 95, 3]))
    print('count: ', count(4, [4, 4, 3, 2, [4, 3, [3, 4]], [0, 1, 4]]))
    print(zippa([1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10]))
    print(bricklek('f', 't', 'h', 2))

    ###Exercise 16
    # the time it takes to move n tiles is given by t(n) = 2^n-1
    print(2 ** 50 - 1, 'seconds which equals', (2 ** 50 - 1) / 3600 / 24 // 365, 'years')

    ###Exercise 17
    # Jag verifierade att tiden växt med 1.618^n genom att skapa funktionen fibtiming().
    # Den skriver ut tiden det tar att köra fib() för olika inparametrar n
    # Vid en körning blev tiderna för 32 och 33, 0.647 repsektive 1.03
    # För att se om tiden växer med 1.618^n tar jag och räknar ut c för en av körningarna
    # och sedan ser hur de andra körningarna för andra n passar sig till den "modellen".
    # Jag får c_32 = 1.33*10^-7 och med den konstanten kan jag extrapolera och se om datan passar.
    # estimerad tid för t(34) blir då 1.693 vilket är väldigt nära det faktiska (för denna körning) 1.675
    # t(33) estimeras till 1.047 vilket är nära 1.033. Genom att göra detta med större datamängder,
    # får man högre "säkerhet"
    print(fibtiming(fib))
    c = 1.675 / 1.61 ** 34
    print('t(50) =', c * 1.618 ** 50 / 3600, 'hours')
    print('t(100) =', c * 1.618 ** 100 / 3600 / 24 / 365, 'years')

    ###Exercise 20
    c_merge = 1 / 3000
    c_ins = 1 / 10 ** 6

    t_merge_6 = c_merge * 10 ** 6 * log(10 ** 6)  # nlog(n)
    t_ins_6 = c_ins * (10 ** 6) ** 2  # n^2
    print("merge sort for n = 10^6:", t_merge_6 / 3600, 'hours')
    print("insertion sort for n = 10^6:", t_ins_6 / 3600 / 24, 'days')

    t_merge_9 = c_merge * 10 ** 9 * log(10 ** 9)  # nlog(n)
    t_ins_9 = c_ins * (10 ** 9) ** 2  # n^2
    print("merge sort for n = 10^9", t_merge_9 / 3600 / 24, 'days')
    print("insertion sort for n = 10^9", t_ins_9 / 3600 / 24 / 365, 'years')


if __name__ == "__main__":
    main()

####################################################    

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  
  
  
  
  Exercise 17: Time for Fibonacci:
  
  print(fibtiming(fib)) # this shows that by calculating one more fib numer we need to multiply the time by approx 1.618
  c = 4.69083/1.61**34
  print('t(50) =',c*1.618**50)
  print('t(100) =', c * 1.618 ** 100 / 3600 / 24 / 365, 'years')
  
  
  
  Exercise 20: Comparison sorting methods:
  
  c_merge = 1/3000
  
  c_ins = 1/10**6
  
  't_merge(10**6)' = c_merge*10**6*log(10**6) 
  
  
  
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  algorithm B has time complexity:
  theta(n) = n log(n)
  
  t(n) = c*n*log(n)
  t(10) = 1 => 
  c = 0.1
  when is algorithm A (theta(n) = n) faster than B?
  n = 0.1*n*log(n) algebra gives that when n > 10**10 we have that algorithm A becomes faster
  
  
  
  
  
  





"""
