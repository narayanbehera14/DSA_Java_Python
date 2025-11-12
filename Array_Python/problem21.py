# Combination Operations (Multiple Steps)
# Insert an element, then delete another
arr = [1,2,3,5,4]
arr.append(55)
print(arr)
arr.pop(1)
print(arr)

# Merge, then sort
num = [5,4,77,8,9]
sum = [100,1,2,3,6,4]
merge = num + sum
print(merge)

merge.sort()
print(merge)

# Remove duplicates, then find max
 
dup = [1,2,3,5,4,8,1,2,3,2]

ii = set(dup)
print(ii)

iii = max(ii)
print(iii)

# ----------------different approach -------

ram = [1,2,3,2,1,45,4,1,2,1]

nam = []
for i in ram:
    if i not in nam:
        nam.append(i)
print(nam)

print(max(nam))

