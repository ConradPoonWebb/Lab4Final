#Special Pythag Triplet
'''Check numbers from 1 to 999 to see if there are pythag triplets
a should be all numbers between 1 and 999, b should be the range from 1 to a
c should be 1000 - a - b to make sure that a + b + c = 1000
test if a^2 + b^2 = c^2
If they can, find the product'''

def pythagTrip(): #Test all possible combinations and output product
    for a in range(1,1000):
        for b in range(1,a+1):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print (a,b,c)
                print (a*b*c)
            else:
                continue

pythagTrip()
