class Student:
    # method
    def __init__(self):#initializer

        self.name = input("Enter your Name =")
        self.age = int(input("Enter your Age = "))
        self.Gender = input("Enter your gender =")
        self.roll_no = int(input("Enter your no. = "))

    def info(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"Gender = {self.Gender}")

s1 = Student()
s1.info()

s2 = Student()
s2.info()