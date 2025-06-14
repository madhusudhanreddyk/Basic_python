# Read input strings
string1 = input()
string2 = input()

# Initialize a counter
count = 0

# Iterate through each character in string1
for char in string1:
    if char in string2:
        count += 1
      # remove the matched char

# Print the result
print(count)
