#Distinct Powers
'''Using 2 for commands, test all possibilities for a and b
2 <= a <= 100 and 2<=b<=100
show all unique/distict numbers'''

def distinctPowers():
    disNum = []
    for a in range(2,101):
        for b in range(2,101):
            powerNum = a**b
            if powerNum in disNum:
                continue
            else:
                disNum.append(powerNum)
    print (len(disNum))

distinctPowers()
