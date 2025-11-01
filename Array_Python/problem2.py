arr = [1,2,5,8,9]

maxvalue = arr[0]
minvalue = arr[0]

for i in arr :

    if maxvalue < i:
        maxvalue = i


    if minvalue > i:
        minvalue = i
    
print("minimum value is ", minvalue)
print("maximum value is", maxvalue)

