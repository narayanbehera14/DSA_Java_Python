def add_num(n1,n2,n3):
    return n1 + n2 + n3
print(add_num(1,2,3))

num = lambda m1,m2,m3 : m1+m2+m3
print(num(12,21,2))



from typing import*
def sum(x: List[int]):
    print(sum(x))

sum([1,2,3])
sum([100,200])