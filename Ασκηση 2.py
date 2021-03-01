from random import randrange,seed
from datetime import datetime
import math
import sys 

seed(None)

def fibonacci(n):
    fibo0 = 0
    fibo1 = 1
    fiboResult = 0
    for loop in range(n):
        fiboResult = fibo0 + fibo1
        fibo0 = fibo1
        fibo1 = fiboResult
    return fiboResult

def makesRandomNumberUnique(randomNumber,fibonacciResult,listOfRandomNumbers):
    while (True):
        for oldRandomNumber in listOfRandomNumbers:#if we got a randomNumber that were given again 
            if randomNumber == oldRandomNumber:
                randomNumber = randrange(2 , fibonacciResult)
                break
        else:
            break
    return randomNumber

def userInput():
    while(1):
        try:
            print("\n-----------------------------------------------")
            n = int(input("Give the n number of the fibonacci sequence :"))
            if n>-1:
                break
        except:
            sys.exit(0)
    return n


def main():
    n = userInput()
    fibonacciResult = fibonacci(n)

    if fibonacciResult == 0 or fibonacciResult == 1:
        print(f"the fibonacci({n}) = {fibonacciResult} prime numbers can only be numbers > 1 ")        
    else:
        listOfRandomNumbers = []
        loops = fibonacciResult
        if fibonacciResult > 23:
            loops = 22
        for loop in range(loops - 2):
            randomNumber = randrange(2 , fibonacciResult)
            randomNumber = makesRandomNumberUnique(randomNumber,fibonacciResult,listOfRandomNumbers)
            listOfRandomNumbers.append(randomNumber)
            
            if ( pow(randomNumber, fibonacciResult, fibonacciResult) != randomNumber%fibonacciResult):#that means that the fibonacci number is not prime
                print(f"\nthe fibonacci({n}) = {fibonacciResult} is not prime ")
                sys.exit(0)
                
        print(f"\nthe fibonacci({n}) = {fibonacciResult} is prime ")
        

main()