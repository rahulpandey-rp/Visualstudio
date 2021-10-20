import unittest
from OopsQ3 import Point

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(3,4)
    def test_init(self):
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)
    
    def test_repr(self):
        self.assertEqual(self.p1.__repr__(), '(3, 4)')

    def test_add(self):
        self.p2 = Point(2,6)
        self.p3 = self.p1.__add__(self.p2)
        self.assertEqual(self.p3.__repr__(),'(5, 10)')


if __name__ == "__main__":
    unittest.main()