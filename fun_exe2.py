def print_pattern(num):
    for i in range(num+1):
        s = ''
        for j in range(i):
            s += '*'
        print(s)
print_pattern(3)
