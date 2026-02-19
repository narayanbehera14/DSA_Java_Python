class Student:
    roll_no = 0
    name = " Raj"
    age = 9
    gender = " Female"
    address = " Mumbai"


    def info(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender= {self.gender}")

    def set_info(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter your age = "))
        self.gender = input("Enter your gender = ")
        self.roll_no = int(input("Enter roll number ="))


s1 = Student()
s2 = Student()

# s1.gender = "Male"
# s1.name = " Narayan"

s1.info()

# s1.age = 55
# print(s1.age)
# print(s1.name)
# print("-----")
# print(s2.name)
# print(s2.age)

s2.set_info()  