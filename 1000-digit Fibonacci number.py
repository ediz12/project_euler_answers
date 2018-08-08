a, b, term = 0, 1, 0
while True:
    if len(str(a))== 1000:
        print term
        break
    a, b, term = b, a + b, term+1
