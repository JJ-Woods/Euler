#Author - Jamie Woods
#https://projecteuler.net/problem=10


LIMIT = 2000000


def main():
    primes = findPrimesBelowLimit(LIMIT)
    sum = 0
    for prime in primes:
        sum += prime
    print("The solution to problem 10 is " + str(sum))


def findPrimesBelowLimit(limit):
    primes = []
    primeLocations = []
    for x in range(0, limit):
        primeLocations.append(True)
    for x in range(2, limit):
        if primeLocations[x]:
            primes.append(x)
            multipleOf = x * 2
            while multipleOf < limit:
                primeLocations[multipleOf] = False
                multipleOf += x
    return primes


if __name__ == "__main__":
    main()
