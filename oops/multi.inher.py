class Father:
    def __init__(self):
        self.Father_name = "Narayan"

    def displayFatherName(self):
        print(self.Father_name)

class Mother:
    def __init__(self):
        self.Mother_name = "Pagal"

    def displayMotherName(self):
        print(self.Mother_name)

class Child(Father,Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.Child_name = " raj"
        print("CHILD INIT")

    def displayChildName(self):
        print(self.Child_name)
    

c1 = Child()
c1.displayFatherName()
c1.displayMotherName()
c1.displayChildName()