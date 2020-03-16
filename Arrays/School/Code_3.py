# Enter the number of test case
T = int(input())
# Iterate over each test case
for test in range(T):
    # Enter the size of the array
    N = int(input())
    # Enter the elements in the array
    a = list(map(int, input().split()))
    # Declare maximum element as 0 initially
    max_ele = 0
    # Iterate over every element inside the array
    for i in a:
        # If element is greater than current maximum element
        if max_ele < i:
            # Update the maximum element
            max_ele = i
    # Print the output
    print(max_ele)
