# Enter the number of test case
T = int(input())
# Iterate over each test case
for test in range(T):
    # Enter the input string
    inp = input()
    # Separate input into list of string separated by ' . '
    result = inp.split('.')
    # Create output variable
    out_ = ''
    # Starting iterate over last to second index
    for i in range(len(result)-1,0,-1):
        out_ = out_ + result[i] + '.'
    # Append the first index
    out_ = out_ + result[0]
    # Display output
    print(out_)
