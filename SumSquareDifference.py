#Sum Square Difference
'''Create two functions
One returns the sum of all the numbers from 1-100 if each value is squared (1^2 + 2^2+...)
The other one returns the sum of all numbers from 1-100 squared (1+2+3+...)^2
Figure out which one is larger and find the difference'''

def squaredSums(): #Sum of all numbers 1-100 is each value is squared
    finalNum = 0
    for num in range(1,101):
        finalNum += num ** 2
    return finalNum

def theSumSquared():#Summ of all numbers from 1-100 squared
    finalNum = 0
    for num in range(1,101):
        finalNum += num
    return finalNum ** 2

def comparingNums(num1, num2):#Comparing each number and finding the difference
    difference = max(num1, num2) - min(num1,num2)
    print ('The difference between '+ str(num1)+' and '+ str(num2)+' is '+str(difference))

if __name__ == '__main__':#Final set up
    squaredSumTotal = squaredSums()
    sumSquaredTotal = theSumSquared()
    comparingNums(squaredSumTotal,sumSquaredTotal)
