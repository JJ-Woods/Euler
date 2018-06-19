#Author - Jamie Woods
#https://projecteuler.net/problem=2

def main():
    limit = 4000000
    sum = 2
    fib0 = 1
    fib1 = 2
    while(fib1 < limit):
        nextFib = fib0 + fib1
        if(nextFib % 2 == 0):
            sum += nextFib
        fib0 = fib1
        fib1 = nextFib
    print sum
            
if __name__ == "__main__":
    main()
