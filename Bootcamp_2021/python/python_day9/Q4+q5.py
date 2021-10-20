class Vehicle:
    def __init__(self, make, mileage, capacity):
        self.make = make
        self.mileage = mileage
        self.capacity = capacity

    def get_fare(self):
        raise AttributeError("Please call a class like bus or car")


class Car(Vehicle):
    def get_fare(self):
        self.fare = (self.mileage * self.capacity) + 25 / 100
        return(self.fare)


class Bus(Vehicle):
    def get_fare(self):
        self.fare = (self.mileage * self.capacity) + 15 / 100
        return(self.fare)


c1 = Car("Tata", 70, 5)
b1 = Bus("Mahindra", 25, 70)
print(c1.get_fare())
print(b1.get_fare())
