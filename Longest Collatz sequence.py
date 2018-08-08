import json, time
start = time.time()
def collatz(n):
    chain_number, real_number = 0, n
    while True:
        chain_number += 1
        if n == 1:
            return real_number, chain_number
        if n%2 == 0:
            n = n/2
        elif n%2 == 1:
            n = 3*n+1

numbers = {}
for i in  range(500000, 1000001):
    number, chain = collatz(i)
    numbers[chain] = number

json.dump(numbers, open("text.txt",'w'))
print "Done: " + str(time.time() - start)

    
