def digits(num):
    counter = 0
    while num > 1:
        counter = counter + 1
        num = num/10
    return counter
