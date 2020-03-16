# Enter the number of test case
T = int(input())
# Iterate over each test case
for test in range(T):
    # Enter the number of input entered string
    N = int(input())
    # Intialize maximum length of string to 0
    max_length = 0
    # Iterate over each input string over N times input
    for n in range(N):
        # Enter the string
        inp_str = input()
        # If length of inputted string is greater than previous maximum length
        if len(inp_str) > max_length:
            # Update long string to another variable
            long_str = inp_str
            # Update the maximum length variable
            max_length = len(inp_str)
    # Print the output
    print(long_str)
