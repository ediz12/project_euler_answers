product = 1
for i in range(1, 101):
    product *= i
    
total = 0
for a in str(product):
    print a + "+",
    total += int(a)
print total
    
