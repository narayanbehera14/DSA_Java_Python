a = [1,2,3,4,5]
b = ['apple','banana','cherry']
c = [1,'hello',3.14,True]

print(a)
print(b)
print(c)

d = list((1,2,4,'apple',2.4))
print(a)

e = list("GFG")
print(e)

a = [3]*5
p = [33]*5

print(a)
print(p)

a = [10,03,40,55,45]
print(a[3])
print(a[-1])
print(a[1:3])


a.append(400)
print("After append (10):",a)

a.insert(0,3)
print("after insert(0,3):",a)

a.extend([14,20,30])
print("After extend ([13,21,25]):",a)

a.clear()
print("after clear():",a)

a = [10,20,30,40,50,60]
a[1] = 15
print(a)

a = [1,2,3,4,5,6,7]

a.remove(2)
print("after remove(2)",a)

popped_val = a.pop(1)
print("poped element:",a)
print("after pop(1):",a)

del a[0]
print("after del a[0]:",a)

a = ['apple','mango','cherry','orange']
for item in a:
    print(item)


matrix = [[
    1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][2])


square = [x**2 for x in range(1,5)]
print(square)


a = [12,556,"GFG",True]
print(a)
print(a[0])
print(a[1])
print(a[2])
