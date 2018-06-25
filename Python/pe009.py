#Author - Jamie Woods
#https://projecteuler.net/problem=9


import math

TARGET = 1000


def main():
    answer = findProductOfTriplet()
    print("The solution to problem 9 is " + str(answer))


def findProductOfTriplet():
    for a in range(1, TARGET):
        for b in range(1, TARGET):
            aSquared = a ** 2
            bSquared = b ** 2
            cSquared = aSquared + bSquared
            c = math.sqrt(cSquared)
            sumOfTriplet = a + b + c
            if sumOfTriplet == 1000:
                productOfTriplet = a * b * c
                return int(productOfTriplet)


if __name__ == "__main__":
    main()
