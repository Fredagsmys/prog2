import random as rand
import math
import matplotlib.pyplot as plt
import functools as ftools
import concurrent.futures as future
from time import perf_counter as pc


def calc_pi(n):
    inside = 0
    xcor_c = []
    ycor_c = []
    xcor_s = []
    ycor_s = []

    for _ in range(n):
        x = rand.uniform(-1, 1)
        y = rand.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            xcor_c.append(x)
            ycor_c.append(y)
            inside += 1
        else:
            xcor_s.append(x)
            ycor_s.append(y)

    return inside, xcor_c, ycor_c, xcor_s, ycor_s


def approx_pi():
    # n = [x**10 for x in range(2, 6)]
    # pis = [4*calc_pi(n)/n for n in n]
    n = 10 ** 4
    res, xcor_c, ycor_c, xcor_s, ycor_s = calc_pi(n)
    picalc = 4 * res / n
    print("math.pi:", math.pi, "vs montecarlo pi:", picalc)
    plt.plot(xcor_c, ycor_c, 'b.', xcor_s, ycor_s, 'r.')
    plt.show()


def hypersphere(n, dim):
    inside = get_inside(n, dim)
    return inside / n * (2 * r) ** dim  # 2**d is the volume of the d-dimensional "square" with sides 2*r


r = 1


def get_inside(n, dim):
    sum = lambda x, y: x + y
    square = lambda x: x ** 2
    within = 0
    for _ in range(n):
        cords = [rand.uniform(-r, r) for _ in range(dim)]  # list comprehension

        dist = ftools.reduce(sum, map(square,
                                      cords))  # double lambda function because I could not have one lambda function which sum the squares of each element
        if dist < r ** 2:  # outside
            within += 1
    return within


def para_hypersphere(n, dim, cores):
    inside = 0
    with future.ProcessPoolExecutor() as ex:
        processes = []
        results = []
        div = n // cores

        for _ in range(cores):
            processes.append(ex.submit(get_inside, div, dim))
        for pro in processes:
            results.append(pro.result())
        for res in results:
            inside += res

    return inside / n * (2 * r) ** dim  # 2**d is the volume of the d-dimensional "square" with sides 2*r


def main():
    #    approx_pi()
    n = 1000000
    d = 11
    cores = 6
    #    print(hypersphere(n, d))
    #    print()
    #    n = 100000
    #    d = 11
    #    print(hypersphere(n, d))
    start = pc()
    print(f"volume is esitmated: {para_hypersphere(n, d, cores)}")
    stop = pc()
    t1 = stop - start
    print(f"Time for parallell: {round(t1, 3)}s")
    start = pc()
    print(f"volume is esitmated: {hypersphere(n, d)}")
    stop = pc()
    t2 = stop - start
    print(f"Time for non-parallell: {round(t2, 3)}s")
    print(f"Time difference is a factor of {t2 / t1} when using {cores} cores.")
    # The time is not improved linearly with
    # ammount of cores becuase the cores still need to communicate with each other which slows down

    vol_analytic = (math.pi ** (d / 2) * r ** d) / (math.gamma(d / 2 + 1))
    print(f"Analytical volume is: {vol_analytic}")


if __name__ == "__main__":
    main()
