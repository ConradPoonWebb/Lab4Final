#Fibonacci Numbers
'''Create a list of fibonacci numbers
add the even numbers
badda bing, badda boom.'''

def fibonacciNum(): #Create a fibonacci sequence that is under 4 million
    startList = [0,1]
    index = 0
    index2 = 1
    while startList[len(startList)-1] < 4000000:
        nextNum = startList[index] + startList[index2]
        if nextNum < 4000000:
            startList.append(nextNum)
        else:
            break
        index += 1
        index2 += 1

    return startList

def findEvens(numList): #Find all the even numbers in a list
    evenList = []
    for num in numList:
        if num % 2 == 0:
            evenList.append(num)
    
    return evenList

def addingList(numList): #Add numbers in a list
    sum = 0
    for num in numList:
        sum += num
    
    print ('Sum of all even terms under 4 million in the fibonacci sequence is ' + str(sum))

if __name__ == '__main__':
    fibSequence = fibonacciNum()
    print (fibSequence)
    evens = findEvens(fibSequence)
    addingList(evens)
