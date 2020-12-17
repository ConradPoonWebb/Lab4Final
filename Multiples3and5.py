#Lab 4 [Project Euler]
#Conrad Poon
#12/17/2020

#Multiples of 3 and 5 [Problem 1]
'''
Task: Find all the multiples of 3 and 5 in a range of numbers
Add these numbers up and print the output
'''

def find3n5(rangeMax): #Finds all the multiples of 3 and 5 in a given range
  numList = []
  for num in range(1,rangeMax):
    if num%3 == 0 or num%5 == 0:
      numList.append(num) #Add number to the outputting list
    else:
      continue
  return numList

def addingList(numList): #Add all the numbers together in a list
  sum = 0
  for num in numList:
    sum += num
  print ('Sum of all multiples of 3 and 5 below ' + str(maxRange) + ' is ' + str(sum))
  
if __name__ == '__main__': #Making the gears turn
  maxRange = int(input('What is the highest number in the range? '))
  threeNfive = find3n5(maxRange)
  addingList(threeNfive)
