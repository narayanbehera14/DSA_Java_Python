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


# sorting techniques

arr = [(2,3),(1,5),(4,1)]
print(sorted(arr,key=lambda x: x[1]))


#Use: Sort by frequency, value, or index.

# ----------------------------------------------------

# collection module

from collections import Counter,deque,defaultdict

print(Counter("leetcode"))
dq = deque([1,2,3]);dq.appendleft(0);dq.pop()
d = defaultdict(int);d['a'] += 1

# Use: Frequency count, fast queue.

# ------------------------------------------------------


# Heap / priority queue

import heapq
nums = [2,5,4]
heapq.heapify(nums)
heapq.heappush(nums,1)
print(heapq.heappushpop(nums))

#Use: Top K problems, Dijkstra’s algorithm.

# ------------------------------------------------

# itertools

from itertools import combinations,permutations
print(list(combinations([1,2,3],2)))
print(list(permutations([12,3,2],300)))

#Use: Backtracking, subset generation.

# -----------------------------------------


# recursion

def fact(n):
    return 1 if n==0 else n*fact(n-1)

#Use: DFS, tree traversal.

# --------------------------------------
# Complexity Analysis

# Example:

# for loop → O(n)

# Nested loop → O(n²)

# Binary search → O(log n)
# Use: Time-optimized solutions.


# --------------------------------------------

# LEVEL 3 — Advanced Python for DSA

# Binary Search Template

def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid]==target: return mid
        elif arr[mid]<target: l = mid+1
        else: r = mid-1

# ---------------------------------------------------


# Advanced Built-ins

from functools import lru_cache
@lru_cache(None)
def fib(n): return n if n<2 else fib(n-1)+fib(n-2)

import bisect
nums = [1,3,4,7]
bisect.insort(nums,5)

# 💡 Use: Memoization, sorted insertion.
# -----------------------------------------------------

# Decorators

def deco(func):
    def inner():
        print("Before")
        func()
        print("After")
    return inner

@deco
def hello(): print("Hi")
hello()


# ---------------------------------------------------


# Object-Oriented Programming
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


#Use: Linked list, tree nodes.

# ---------------------------------------------------

# Type Hints

def add(a: int, b: int) -> int:
    return a + b


# ----------------------------------

# Pythonic Tricks

a, b = b, a  # swap
res = "Yes" if a > b else "No"
for _ in range(3): print("loop")



# -------------------------------------------------

# Memory Optimization

def gen_nums():
    for i in range(10**6): yield i

# 💡 Use: Large dataset handling.


# ---------------------------------



# Useful Modules
# Module	Use
# math	gcd, sqrt
# heapq	priority queue
# collections	Counter, deque
# itertools	combinations
# functools	lru_cache, reduce
# bisect	binary search
# operator	itemgetter


#Fast I/O

import sys
input = sys.stdin.readline


# -------------------------------------

# Common DSA Patterns

# Two Pointers

l, r = 0, len(nums)-1
while l < r:
    if nums[l]+nums[r] == target: break

# ----------------------------------------------


#  Sliding Window

window = sum(nums[:k])
for i in range(k, len(nums)):
    window += nums[i] - nums[i-k]


# ------------------------------------------------

# Prefix Sum

prefix = [0]
for n in nums:
    prefix.append(prefix[-1]+n)


# --------------------------------------------------


# Debugging & Tricks

assert len(arr)>0, "Array is empty"
from pprint import pprint
pprint({"a":1,"b":2})


# -------------------------------------------------

# LEVEL 4 — Practice Strategy

# Start with Easy DSA topics:

# Arrays, Strings, HashMap, Stack, Queue

# Move to Medium:

# Two Pointers, Binary Search, Recursion, Backtracking

# Advance to Hard:

# Trees, Graphs, DP