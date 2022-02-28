import unittest
from FileToTest import Vehicle,Car,Bus


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.veh=Vehicle("Tata",70,5)
    def test_vehicle_init(self):
        self.assertEqual(self.veh.make,"Tata")
        self.assertEqual(self.veh.mileage,70)
        self.assertEqual(self.veh.capacity,5)
    def test_getfare(self):
        with self.assertRaises(AttributeError):
            self.veh.get_fare()


class TestCar(unittest.TestCase):
    def setUp(self):
        self.c1=Car("Tata",70,5)
    def test_getFare(self):
        self.assertEqual(self.c1.get_fare(),350.25)


class TestBus(unittest.TestCase):
    def setUp(self):
        self.b1=Bus("Mahindra",25,70)
    def test_getFare(self):
        self.assertEqual(self.b1.get_fare(),1750.15)


if __name__ == "__main__":
    unittest.main()