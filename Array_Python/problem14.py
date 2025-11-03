# Delete duplicate elements from sorted array

arr = [1,2,2,4,5]

arr.sort()

arr = set(arr)
arr = list(arr)

print(arr)
