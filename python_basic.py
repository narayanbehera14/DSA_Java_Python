a = 10
b = 3.4
c = "hello"
d = True
e = [1,2,3,4,5]
f = (1,2)
g = {1,2.34,4}

print(4+3,3-5,4/8,55*4,2%3)
print(8>8, 8==5, 9!=5)
print(True and False,True or False , not True)
print(5&5,8|5,5^9,5<<1)

print(2 in [1,2,3])

x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else :
    print ("Negative")


for i in range(4):
    print(i)

n = 3
while n > 0:
    print(n)
    n -= 2


def add(a,b):
    return a+b
print(add(5,3))

name = input("enter name:")
print("hello",name)

s = "leetcode"
print(s[0],s[-1],s[2:3])
print(s.upper(),s.lower())
print(s.replace('e','E'))

print(s[::-1])

nums = [1,2,23]
nums.append(4)
nums.pop()
nums.sort()
print(nums[1:4])

t = (2,3,4.5)
s = {1,2,3,4}
d = {'s':1 , 'f':3}
print(d['a'])

try:
    print(10/40)
except ZeroDivisionError:
    print("cannot divide by zero")


square = [x*x for x in range(6) if x%2==0]
print(square)

from functools import reduce
nums = [1,2,3,4]
print(list(map(lambda x: x*x,nums)))
print(list(filter(lambda x : x%2==0)))
print(reduce(filter(lambda x , y: x+y,nums)))


def gen():
    for i in range(3):
        yield i

for num in gen():
    print(num)


for i , val in enumerate(['a','b','d','e']):
    print(i,val)

a = [1,2,3]
b = [5,6,7]
print(list(zip(a,b)))

nums = [1,2,3]
print(len(nums),max(nums),min(nums),sum(nums))

#what is exception handling ?

try :
    lst = [4,5,6,7,22,11,112]
    print(lst[1])
    print(lst[22])
    print(lst[4])
    print(lst[5])
    print(lst[11])
except:
    print("some error occurred")

print("Done")
print("Bye")

try:
    my_list = [2,4,6,77,6,3]
    print(my_list[76])
    print(my_list[0]/my_list[-1])
except IndexError:
    print("Invaild Index")
except:
    print("some error occurred")
finally :
    print("this is a clause")

 