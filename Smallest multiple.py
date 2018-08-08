no = 2520
divisor = 20
while True:
    if no % divisor == 0:
        divisor -= 1
        if divisor == 1:
            print no
            break
    else:
        no += 10
        divisor = 20
