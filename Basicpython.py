# Python for DSA + LeetCode: Full Topic + Example Guide
# LEVEL 1 — Python Core Foundations

# Variable & Data Types
# Definition: Containers for storing data of various types.

a = 10                 # int
b = 3.5               # float
c = "hello"          #string
d = True             #boolean
e = [1,2,3,4]       #list
f = (1,2)          #tuple
g = {1,2,30}      #set

#Use in DSA: Representing arrays, flags, and mappings (like frequency counts).

# -------------------------------#


# operator

#Definition: Perform computations or comparisons.


#Arithmetic

print( 5+4 , 8-8 , 7/8 , 9%30 )

# Comparion

print(5 > 2 , 5 == 4 , 5 != 5)

# Logical

print(True and False , True or False , not True)

# Bitwise
print( 5 & 2 , 3 | 4, 5 ^ 7 , 5 << 1)

# Membership
print(2 in [1,2,3])

#Use in DSA: Bit manipulation, conditional logic.


# --------------------------------------------------#

# 3.Conditional Statements

# Definition: Execute code based on conditions.

x = 10
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else :
    print("Negative")

#Use in DSA: Decision-making during algorithm flow.

# -------------------------------------------------

# Loops

# Definition: Repeat a block of code.

for i in range(5):
    print(i)

n = 3
while n > 0:
    print(n)
    n -= 1

#Use in DSA: Iterating arrays, BFS/DFS, traversal.

# --------------------------------------------------



# Functions

# Definition: Block of code executed when called.

def add(a,b):
    return a+b
print(add(5,3))

#Use in DSA: Recursive or helper functions.


# ----------------------------------------------------


# Input / Output

name = input("enter name:")
print("hello",name)

#Use in DSA: Taking user or test input.

# ----------------------------------------------

# String Operations

s = "leetcode"
print(s[0], s[-1], s[2:5])
print(s.upper(),s.lower())
print(s.replace('e','E'))
print(s[::-1])        #reverse

#Use in DSA: Palindrome checks, substring search.

# --------------------------------------------------



# Lists

nums = [1,2,3]
nums.append(4)
nums.pop()
nums.sort()
print(nums[1:3])

#Use in DSA: Dynamic arrays, sliding window, prefix sums.


# -----------------------------------------------------------------


#9.Tuples, Sets, Dictionaries

t = (1,2,3)
s = {1,2,3}
d = {'a':1,'b':3}
print(d['a'])

#Use in DSA: Hash-based lookup, key-value mappings.


# ---------------------------------------------------


#Exception Handling

try:
    print(10/0)
except ZeroDivisionError:
    print("cannot divide by zero")

#Use in DSA: Handling invalid inputs or edge cases.

# ------------------------------------------------------------


# LEVEL 2 — Python for DSA (Intermediate)

# List Comprehensions

square = [x*x for x in range(6) if x%2==0]
print(squares)

# Use: Compact array creation, filtering.

# -----------------------------------------------------------


#Lambda, Map, Filter, Reduce

from functools import reduce
nums = [1,2,3,4]
print(list(map(lambda x: x*x,nums)))
print(list(filter(lambda x : x%2==0,nums)))
print(reduce(lambda x , y: x+y,nums))

# Use: Clean one-liners for transformations.

#-------------------------------------





# Iterators and Generators

def gen():
    for i in range(3):
        yield i
for num in gen():
    print(num)

#Use: Efficient memory for large sequences.

# -------------------------------------


#Enumerate and Zip

for i , val in enumerate(['a','b','c']):
    print(i,val)

a = [1,2,3]
b = [4,5,6]
print(list(zip(a,b)))

#Use: Pairing indices or arrays.

# ---------------------------------------------------


#Built-in Functions

nums = [1,2,3]
print(len(nums),max(nums),min(nums),sum(nums))


# --------------------------------------------------
