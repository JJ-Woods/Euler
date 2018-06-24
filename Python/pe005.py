#Author - Jamie Woods
#https://projecteuler.net/problem=5

def main():
    divisibleUpto = 20
    sol = findNumberDivisibleUpto(divisibleUpto)
    print("The solution to problem 5 is " + str(sol))


def findNumberDivisibleUpto(divUpto):
    attempt = 1
    while True:
        breakFlag = False
        for x in range(1, divUpto):
            if attempt % x != 0:
                breakFlag = True
                break
        if breakFlag:
            attempt += 1
            continue
        else:
            return attempt


if __name__ == "__main__":
    main()
