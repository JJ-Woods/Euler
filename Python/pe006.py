#Author - Jamie Woods
#https://projecteuler.net/problem=6


def main():
    upto = 100
    upto = upto + 1 #correct for loop iterations
    sumOfSquares = findSumOfSquaresUpto(upto)
    sumSquared = findSumUptoSquared(upto)
    diff = abs(sumSquared - sumOfSquares)
    print("The solution to problem 6 is " + str(diff))


def findSumOfSquaresUpto(upto):
    sum = 0
    for x in range(1, upto):
        squared = x ** 2
        sum += squared
    return sum


def findSumUptoSquared(upto):
    sum = 0
    for x in range(1, upto):
        sum += x
    return sum ** 2

if __name__ == "__main__":
    main()
