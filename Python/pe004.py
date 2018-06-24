#Author - Jamie Woods
#https://projecteuler.net/problem=4

NUM_DIGITS = 3

def main():
    lowerLimit = 10 ** (NUM_DIGITS - 1)
    upperLimit = (10 ** NUM_DIGITS) - 1
    largestPalindrome = findLargestPalindromeInRange(lowerLimit, upperLimit)
    print("The solution to problem 4 is " + str(largestPalindrome))


def findLargestPalindromeInRange(lowerLimit, upperLimit):
    allPalindromesInRange = findAllPalindromesInRange(lowerLimit, upperLimit)
    if len(allPalindromesInRange) > 0:
        return max(allPalindromesInRange)
    else:
        return "No palindrome found in range"


def findAllPalindromesInRange(lowerLimit, upperLimit):
    palindromes = []
    for outer in range(lowerLimit, upperLimit):
        for inner in range(lowerLimit, upperLimit):
            product = outer * inner
            if isPalindrome(product):
                palindromes.append(product)
    return palindromes


def isPalindrome(potentialPalindrome):
    potentialPalindrome = str(potentialPalindrome)
    length = len(potentialPalindrome)
    if length % 2 == 0:
        halfWay = length // 2
        firstHalf = potentialPalindrome[:halfWay]
        secondHalf = potentialPalindrome[halfWay:]
    else:
        middle = ((length - 1) // 2) + 1
        firstHalf = potentialPalindrome[:middle - 1]
        secondHalf = potentialPalindrome[middle:]
    secondHalf = secondHalf[::-1] #reverse secondHalf
    if firstHalf == secondHalf:
        return True
    else:
        return False


def testIsPalindrome(pal):
    if isPalindrome(pal):
        print(str(pal) + " is a palindrome")
    else:
        print(str(pal) + " is not a palindrome")


if __name__ == "__main__":
    main()
