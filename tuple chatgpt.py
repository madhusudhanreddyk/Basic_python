# Take input from the user
lower = int(input())
upper = int(input())

# Create list of tuples using list comprehension
squared_list = [(num, num ** 2) for num in range(lower, upper + 1)]

# Convert list to tuple
result = tuple(squared_list)

# Print result
print(result)
