#Author - Jamie Woods
#https://projecteuler.net/problem=3

def main():
    target = 15
    if(isPrime(target)):
        print target
    
def isPrime(num):
    if(num <= 2):
        raise ValueError("Number to be checked for prime must be greater than 2")
    for x in range(2, num):
        if(num % x == 0):
            return false
    return true

if __name__ == "__main__":
    main()
