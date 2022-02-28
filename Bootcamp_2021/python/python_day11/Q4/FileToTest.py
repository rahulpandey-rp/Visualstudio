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


if __name__ == "__main__":
    pass