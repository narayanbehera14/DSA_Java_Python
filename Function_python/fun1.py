def greet():
    print("Hello This is greet")
    print("WE are learning function")
    print("Ok , done")

greet()
greet()


#args is used to count when u dont know parameter
def add(*args, **kwargs):
    print(kwargs)

add(name="Liju",age=100,gender="Male")


def sub(n1,n2,n3,*args,**kwargs):
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")

sub(2,3,4,53,21,name="behera")
