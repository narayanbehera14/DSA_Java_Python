tup = ()
print(tup)

tup = ('Geeks','For')
print(tup)

li = [1,2,3,4,5,6]
print(tuple(li))

tup = tuple('Geeks')
print(tup)

tup = (4,'Welcome',5,'Geeks')
print(tup)

tup1 = (1,2,3,4,44)
tup2 = ('python','Geek')
tup3 = (tup1,tup2)
print(tup3)

tup1 = ('Geeks',)*3
print(tup1)

tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)

tup = tuple("Geeks")
print(tup[0])

print(tup[1:4])
print(tup[:3])

tup = ("Geeks","For","Geeks")

a, b, c = tup
print(a)
print(b)
print(a,c)

tup1 = (2,3,4,5)
tup2 = ('Geeks','For','Geeks')
tup3 = tup1+tup2
print(tup3)


tup = tuple('GEEKSFORGEEKS')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])

tup = (1,2,3,4,32,55)
del tup
print(tup)

tup = (1,2,3,4,5,55)
a , *b, c = tup
print(a)
print(b)
print(c)
