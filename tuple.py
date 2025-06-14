lower = int(input())
upper = int(input())

for i in range(lower , upper+1):
    list = [i,i**2]
    tuples = tuple(list)
    print(tuples)
