# Enter number of test case
T = int(input())
# Iterate over test case
for test in range(T):
    # Enter number of elements in the array and desired sum
    N,S = list(map(int, input().split()))
    # Enter the elements in the array
    A = list(map(int, input().split()))
    # Intial starting index
    start = 0
    # Intialize windows size
    end = 1
    # Store current sum
    current_sum = A[0]
    flag = False
    
    while end <= N:
        # If current sum greater than desired target, just start removing from starting index
        while current_sum > S and start < end-1:
            current_sum -= A[start]
            start += 1
        # If current sum equal to desired sum, just print and break
        if current_sum == S:
            print(start+1,end)
            flag = True
            break
        
        # If end index is less than size of elements, then add the current sum
        if end < N:
            current_sum += A[end]
        
        # Increment every end index value
        end += 1
    
    # In that case not found any desired sum, just print -1
    if not flag:
        print('-1')
