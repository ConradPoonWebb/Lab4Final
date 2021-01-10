#Power Digit Sum
'''Sum of all digits in 2**1000
do 2**1000 and use a for loop to add'''

theNumber = 2**1000

def digitSum(num):
    theSum = 0
    for digit in str(num):
        theSum += int(digit)
    return theSum

total = digitSum(theNumber)
print ('The sum of all digits in 2 to the power of 1000 is '+ str(total))
