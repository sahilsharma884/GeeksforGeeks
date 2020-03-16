# Enter the number of test case
T = int(input())
# Iterate over number of test case
for test in range(T):
    # Enter the size of the elements
    N = int(input())
    # Enter the elemets in the array
    a = list(map(int, input().split()))
    # Take left half array
    left_half = sum(a[:N//2])
    # Take right half array
    right_half = sum(a[N//2:N])
    # Print the output
    print(abs(left_half-right_half))
