#Find the sum and average of array elements

num = [1,5,7,8,6]
sum = 0
avg = 0
for i in num :
    sum = sum + i 
print(sum)
    
avg = sum / len(num)


print(avg)