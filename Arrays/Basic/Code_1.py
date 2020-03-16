
# Missing number in array

# Number of test case
T = int(input())
for t in range(T):
    # Number of elements in an array
    N = int(input())
    # Enter the elements of length N
    C = list(map(int,input().split()))
    # If length of C and (N-1) are same
    if len(C) == (N-1):
        # Sum of first N natural number
        sum_arr = N*(N+1)/2
        # Subtract each sum with the present C[i] elements iteratively
        for c in C:
            sum_arr -= c
        # Remaining ones is the left out (missing value)
        print(int(sum_arr))
