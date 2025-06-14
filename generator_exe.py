def square():
    i = 1
    while True:
        yield i*i
        i += 1
for sq in square():
    if sq>25:
        break
    print(sq)
