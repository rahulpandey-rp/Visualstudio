class Vehicle:
    def __init__(self, no_of_wheels):
        self.no_of_wheels = no_of_wheels
        self.current_speed = 0

    def start(self):
        return(f"The engine has been started of {self}")

    def stop(self):
        self.current_speed = 0
        return(f"The engine has been stopped of {self}")

    def accelerate(self):
        self.current_speed += 10
        return(self.current_speed)

    def breaking(self):
        self.current_speed -= 10
        return(self.current_speed)


car = Vehicle(4)
bike = Vehicle(2)
car.accelerate()
bike.accelerate()
car.accelerate()
bike.accelerate()
car.accelerate()
car.breaking()
bike.breaking()
print(car.current_speed, bike.current_speed)
