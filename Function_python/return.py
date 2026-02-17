def addition(num1, num2):
    total = num1 + num2
    return total

x = addition(10,20)
print(x)

#print(addition(10,20))  


def add(n1, n2):
    total = n1 + n2
    print(total)

x = int(input("Enter number 1 = "))
y = int(input("enter a number:"))
add(x,y)

def add(m2, m1):
    total = m2 + m1
    return total

def check(num):
    if num% 2 == 0:
        print("Even")
    else:
        print("Odd")

x = int(input("Enter number 1 = "))
y = int(input("Enter number 1 ="))
s = add(x , y)
print(f"Total = {s}")
print(check(s))