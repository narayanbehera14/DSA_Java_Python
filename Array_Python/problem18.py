#Update / Modification Operations
#Replace a value at a given index

arr = [1,2,3,4,5]
arr[2:3] = [10,24]
print(arr)

#Increment each element by 1

arr2 = [1,2,3,4,5]
for i in range(len(arr2)):

   arr2[i] = arr2[i]+1
print(arr2)
    
#Multiply all even elements by 2

num = [1,2,3,4,5,6,8,7,9,10]

for i in range(len(num)):
   if num[i] % 2 == 0 :
      num[i]= num[i]*2

print(num)
  
#Update all negative numbers to 0

var = [1,2,-5,-8,4,-90,10,9,-8,]
for i in range(len(var)):
   if var[i] < 0  :
      
    var[i] = 0
print(var)

#Update array elements based on another array

let = [1,5,4,7,8,9]
new_let = [10,20,120,30,40]

for i in range(len(let)):
   let[i] = new_let[i]
print(let)
   
  
