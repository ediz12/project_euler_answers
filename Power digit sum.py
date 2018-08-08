import time
start = time.time()
number = 2**1000
total = 0
for i in str(number):
    total += int(i)
print str(total)
print str(time.time() - start)
