# Rotate Array

# Number of test cases
T = int(input())
for t in range(T):
  # N: Number of elements in array
  # D: Number of size of rotating
  N,D = list(map(int,input().split()))
  # Enter elememts of size N
  arr = list(map(int,input().split()))
  # Store the rest of all elements except first D's elements of an array
  result = arr[D:]
  # Take first D elements from the list and extend them (which will added them to the last)
  result.extend(arr[:D])
  # Print the output
  print (' '.join(map(str, result)))
