class Vehicle:
    def __init__(self, wheels, max_speed):
        self.wheels = wheels
        self.max_speed = max_speed
        self._model = wheels + max_speed

    def _model_no(self):
        return(self._model)

    def validate(self, valid):
        if(self.wheels + self.max_speed == valid):
            return(f"The model no is {self._model_no()}")
        else:
            return("Entered Wrong credentials")


car = Vehicle(4, 230)
print(car.validate(4))
