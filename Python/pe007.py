#Author - Jamie Woods
#https://projecteuler.net/problem=7


FIND_PRIME = 10001


def main():
    nthPrime = findNthPrime(FIND_PRIME)
    print("The solution to problem 7 is " + str(nthPrime))
    return 0


def findNthPrime(n):
    belowCeiling = 10000000
    while True:
        primesBelow = findPrimesBelow(belowCeiling)
        if len(primesBelow) < n:
            belowCeiling *= 10
            continue
        return primesBelow[n - 1]


def findPrimesBelow(limit):
    primeLocations = []
    primes = []
    for x in range(0, limit):
        primeLocations.append(True)
    for x in range(2, limit):
        if primeLocations[x]:
            primes.append(x)
            multiplesOf = x + x
            while multiplesOf < limit:
                primeLocations[multiplesOf] = False
                multiplesOf += x
    return primes


if __name__ == "__main__":
    main()
