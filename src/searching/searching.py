def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    low = 0
    high = len(arr)-1
    while low <= high:
      # determine midpoint
        midpoint = (low+high)//2
        if target < arr[midpoint]:
            high = midpoint-1
        elif target > arr[midpoint]:
            low = midpoint+1
        else:
            return midpoint
    return -1  # not found


test_array = [1, 14, 17, 18, 19, 20, 24]

print(linear_search(test_array, 4))
print(binary_search(test_array, 20))
