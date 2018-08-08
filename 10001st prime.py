# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

pN = 1
i = 1

while pN != 10001:
    i += 2
    if i % 2 == 1:
         b = 0
         for a in range(1,i + 1):
             if i % a == 0:
                 b += 1

         if b <= 2:
             pN += 1
             print "%d - %d" % (pN, i)

