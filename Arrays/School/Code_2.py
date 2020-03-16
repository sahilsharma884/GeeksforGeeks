# Enter number of test case
T = int(input())
# Iterate over each test case
for test in range(T):
    # Enter the size of the array
    N = int(input())
    # Enter the element inside the array
    A = list(map(int, input().split()))
    # Store into result variable with reverse direction of array A
    result = A[::-1]
    # Print the output
    print(' '.join(map(str, result)))
