"""numberList = []
for number in range(2,101):
    for power in range(2,101):
        result = number**power
        if not result in numberList:
            numberList.append(result)
print len(numberList)"""

c = [a**b for a in range(2,101) for b in range(2,101)]
print c
        
    
    
