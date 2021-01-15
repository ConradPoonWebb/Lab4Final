#Factorial Digit Sum
'''Write a function that does num! (num * num-1 * num-2*....)
add up each of the digits up in a seperate function
output the answer'''

def factorial(num): #Find the factorial of any number
    productOutput = 1
    for value in range(2,num+1):
        productOutput *= value
    return productOutput

def digitSum(num): #Adds up all the digits in a number
    sumOutput = 0
    for digit in str(num):
        sumOutput += int(digit)
    return str(sumOutput)

fact100 = factorial(100)
print ('The sum of all digits in 100! is ' + digitSum(fact100))
