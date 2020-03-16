# Enter number of test case
T = int(input())
# Iterate over each test case
for test in range(T):
    # Enter size of the array element
    N = int(input())
    # Enter the input of array within size N and map it into integer type
    A = list(map(int,input().split()))
    # Print there sum of array
    print(sum(A))
