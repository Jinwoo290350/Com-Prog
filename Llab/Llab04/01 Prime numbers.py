def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True
    
def printAllPrimes(limit):
    listOfPrimes = []
    for i in range(2, limit + 1):
        if isPrime(i):
            listOfPrimes.append(i)
    if len(listOfPrimes) == 0:
        exit()
    else:
        for j in range(len(listOfPrimes)):
            print(listOfPrimes[j], end=' ')

number = int(input("Input n: "))
printAllPrimes(number)
