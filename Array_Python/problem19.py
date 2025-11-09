# # Merging and Splitting
# #Merge two arrays into one

# a = [1,2,3]
# b = [4.5,6,8,7]

# c = a+ b
# print(c)

# #Merge two sorted arrays

# arr = [2,1,5,4,8]
# num = [77,8,7,9,9,44,]

# arr.sort()
# num.sort()

# print(arr+num)

#Split an array into two halves

# crazy = [1,2,5,4,7,8,96,12]
# boy = crazy[:4]
# girl = crazy[4:]

# print(boy)
# print(girl)





# Merge two arrays into one

# arr1 = [1, 2, 3, 4]
# arr2 = [11, 22, 33, 44]

# mergeArr = arr1 + arr2
# print(type(mergeArr))

#Merge multiple arrays into one
# aa = [1,2,5,5]
# bb =  [7,8,9]
# cc = [9,8,7,4]
# print(aa+bb+cc)

# Find intersection and union of two arrays

aa = [1,2,5,5]
bb = [7,8,9]

c = set(aa)
d = set(bb)

e = (c | d)
print(e)

f = (c & d)

print(f)