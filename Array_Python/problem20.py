# Sorting Operations
# Sort an array in ascending order
arr = [12,5,4,8,5]
arr.sort()
print(arr)

# Sort an array in descending order

num = [2,5,7,8,444,5,44]
num.sort()
num.reverse()
print(num)

# Sort an array of 0s, 1s, and 2s

liju = [0,1,0,1,0,1,0,1,2,1,2,1,2,0,1]
liju.sort()
print(liju)


# Find kth smallest/largest element
rr = [1, 2, 5, 8, 9]

max_value = rr[0]
min_value = rr[0]

for i in rr:
    if max_value < i:
        max_value = i
    if min_value > i:
        min_value = i

print(max_value)
print(min_value)



