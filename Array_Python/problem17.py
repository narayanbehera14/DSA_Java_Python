#Find first and last occurrence of an element
arr = [1, 2, 3, 5, 4, 6, 8, 0, 2, 1, 2]
key = 2

first = -1
last = -1

for i in range(len(arr)):
    if arr[i] == key:
        if first == -1:
            first = i
        last = i

if first != -1:
    print("First occurrence:", first)
    print("Last occurrence:", last)
else:
    print("Element not found")

        

    