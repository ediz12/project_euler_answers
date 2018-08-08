def Pandigital(n):
    if len(n) != 9:
        return False
    count = 0
    for i in range(1,10):
        if str(i) in n:
            count += 1
    if count == 9:
        return True
    else:
        return False

Plist = []
number = 0
while True:
    number += 1
    result = ""
    for product in range(1, 10):
        result = str(number*product)
        if len(result) > 8:
            break
    if len(result) == 9 and Pandigital(result):
        print result
        Plist.append(result)

    
