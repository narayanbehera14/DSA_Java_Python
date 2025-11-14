# Advanced Array Operations

# Find subarray with given sum
def brute_force(arr, target):
    n = len(arr)

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            if total == target:
                return (i, j)
    return -1
