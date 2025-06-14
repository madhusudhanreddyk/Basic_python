# Read number of test cases
T = int(input("Enter number of test cases: "))

for _ in range(T):
    # Read X and Y for each test case
    X, Y = input().split()

    # Calculate total cost for 3 double rooms and 2 triple rooms
    cost_double = 3 * X
    cost_triple = 2 * Y

    # Use conditional statement to find the minimum cost
    if cost_double < cost_triple:
        print(cost_double)
    else:
        print(cost_triple)
