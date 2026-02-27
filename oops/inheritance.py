class Car:
    # def __init__(
    #     self, color:str, type:str, mileage:float, seat_capacity:int
    # ) -> None:
         
    #    self.color = color
    #    self.type = type
    #    self.mileage = mileage
    #    self.seat_capacity = seat_capacity

    def set_info(self):
        self.color = input("Enter car color = ")
        self.type = input("Enter type = ")
        self.mileage = float(input("Enter mileage = "))
        self.seat_capacity = int(input("Enter seat capacity = "))


    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"mileage = {self.mileage}")
        print(f"seat_capacity = {self.seat_capacity}")

class Audi(Car):
    def set_audi_info(self):
        self.set_info()
        self.electric = input("Enter electric = ")
        self.city = input("Enter city = ")
    #         self,
    #         color:str,
    #         type:str,
    #         mileage: float,
    #         seat_capacity: int,
    #         electric: bool,
    #         city: str,
    # ):
        # self.set_info(color, type, mileage, seat_capacity)
        
    # def set_audi_info(self, electric: bool, city: str):
    #     self.electric = electric
    #     self.city = city

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"City = {self.city}")

    # def __init(self) -> None:
    #     print("Audi Init")

    def show_full_info(self):
        self.base_info()
        self.audi_info()


c1 = Audi()
c1.set_audi_info()
# c1.set_info()
# c1.base_info()
# c1.set_audi_info()
c1.show_full_info

# c1.set_info("Black","petrol",12.2,4)
# c1.set_audi_info("Black","petrol",12.2,4,True, "Mumbai")
# c1.base_info()
# c1.audi_info()
# c1.color = "Black"
# c1.mileage = 12
# c1.seat_capacity = 6
# c1.type = "petrol"
# c1.base_info()