__author__ = 'edy'

import integrator
import numpy, math
import stat
import emafit
import math
import smaFeat
import timeit


def main():

    x = timeit.default_timer()
    loop_me()
    y = timeit.default_timer()

    print(y-x)


def loop_me():

    for i in range(0,1000000):
        x = i


if __name__ == '__main__':
    main()






