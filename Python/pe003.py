#Author - Jamie Woods
#https://projecteuler.net/problem=3

TARGET = 600851475143

def main():
    print("The solution to problem 3 is " + findLargestPrimeFactor())


def findLargestPrimeFactor():
    for num in range(2, TARGET):
        if TARGET % num == 0:
            factor = TARGET // num
            if isPrime(factor):
                return str(factor)
    return "No solution found"


def isPrime(potentialPrime):
    for x in range(2, potentialPrime - 1):
        if potentialPrime % x == 0:
            return False
    return True


if __name__ == "__main__":
    main()
