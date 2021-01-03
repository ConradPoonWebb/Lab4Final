#Smallest Multiple (problem 5)
'''2520 is the smalled multiple of all numbers between 1-10
Test all numbers >2520
Check to see if that number can be divisable by numbers:
5, 7, 9(multiples of 3), 11, 13, 16(multiples of 2,4,8), 17, and 19
output number'''

def numCheck(num):
    if num %5 ==0 and num%7==0 and num%9==0 and num%11==0 and num%13==0 and num%16==0 and num%17==0 and num%19==0:
        return True
    else:
        return False

def smallMult():
    startNum = 2520
    while startNum >= 2520:
        theCheck = numCheck(startNum)
        if theCheck == False:
            startNum += 10
            continue
        else:
            return startNum
            break

if __name__ == '__main__':
    answer = smallMult()
    print ('The smallest positive number with multiples of all numbers between 1-20 is ' + str(answer))
