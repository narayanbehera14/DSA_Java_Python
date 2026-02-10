s1 = 'GFG'
s2 = "GFG"
print(s1)
print(s2)

s = """I am Learning
Python String on GeeksForGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

s = "GeeksForGeeks"
print(s[0])
print(s[4])

s = "GeeksforGeeks"
print(s[-10])
print(s[-5])

s = "GeeksforGeeks"
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[::-1])

s = "python"
for char in s:
    print(char)


s = "geeksforGeeks"
s ="G" + s[1:]
print(s)


s = "GFG"
del s

s = "hello geeks"
s1 = "H" + s[1:]
s2 = s.replace("geeks", "GeeksforGeeks")
print(s1)
print(s2)

s = "GeeksforGeeks"
print(len(s))

s = "Hello World"
print(s.upper())
print(s.lower())

s = "   GFG   "
print(s.strip())

s = "python is fun"
print(s.replace("fun","awsome"))

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

s = "Hello"
print(s * 3)

name = "Alice"
age = 22
print(f"Name: {name} , Age:{age}")


s = "My name is {} and I am {} year old.".format("Alice",22)
print(s)


s = "GeeksforGeeks"
print("Geeks"in s)
print("GFG" in s)
