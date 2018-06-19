#Author - Jamie Woods
#https://projecteuler.net/problem=1


import math

def main():
    n = 1000
    sum = 0
    
    for x in range(1, n):
        if((x % 3) == 0 or (x % 5) == 0):
            sum += x
        
    print sum
    
if __name__ == "__main__":
    main()
