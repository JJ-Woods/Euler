#Author - Jamie Woods
#https://projecteuler.net/problem=12

import time
import math

NUM_FACTORS = 500


def main():
    start = time.time()
    current_number = 0
    current_triangle = 0
    while True:
        current_number += 1
        current_triangle += current_number
        if current_triangle <= NUM_FACTORS:  #no point searching below the number
            continue
        num_factors = find_num_factors(current_triangle)
        print("T(" + str(current_number) + "): " + str(current_triangle) + " has " + str(num_factors) + " factors")
        if num_factors > NUM_FACTORS:
            break
    end = time.time()
    elapsed = end - start
    print("The solution to problem 12 is " + str(current_triangle) + " and it took " + str(elapsed) + " seconds to find the solution")


def find_num_factors(num):
    num_factors = 0
    for x in range(1, int(math.ceil(math.sqrt(num)))):
        if num % x == 0:
            num_factors += 2
    return num_factors


if __name__ == "__main__":
    main()
