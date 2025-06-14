string  = input()
upper_count = 0
lower_count = 0
for char in string:
    if char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count +=1
print(upper_count)
print(lower_count)
