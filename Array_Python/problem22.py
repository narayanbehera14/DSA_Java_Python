# Rotate an array (left/right) by k positions

arr = [1,2,3,4,5,6,7]
arr1=arr[0:3]
arr2 = arr[3:8]
arr3 = arr2 + arr1
print(arr3)

# Shift all zeroes to the end while maintaining order
arr = [0,0,0,4,5,6,7]
arr1=arr[0:3]
arr2 = arr[3:8]
arr3 = arr2 + arr1
print(arr3)

# -----------------------------------------------
# different approach 

no = [0,0,0,1,2,3]
noo = []
nooo = []

for i in no:
    if i != 0:
        noo.append(i)
    else:
        nooo.append(i)
noooo = noo + nooo

print(noooo)