# Take input for list size
N = int(input("List size = "))

# Ensure the list size is greater than 0
if N <= 0:
    print("Invalid list size. It should be greater than 0.")
    exit()

# Initialize an empty list
numbers = []

# Take input for list elements
print("Enter list elements:")
for _ in range(N):
    num = int(input())
    numbers.append(num)

# Calculate cumulative sum
cumulative_sum = []
current_sum = 0

for num in numbers:
    current_sum += num
    cumulative_sum.append(current_sum)

# Print result
print("Sum =", cumulative_sum)

