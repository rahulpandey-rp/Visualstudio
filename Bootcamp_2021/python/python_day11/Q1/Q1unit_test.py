import unittest
from FileToTest import convert_cel_to_far,convert_far_to_cel


class test_temperature(unittest.TestCase):
    def test_value_error(self):
        with self.assertRaises(TypeError):
            convert_cel_to_far("a")
        with self.assertRaises(TypeError):
            convert_far_to_cel([23,23])

    def test_return_value(self):
        self.assertEqual(convert_cel_to_far(-5), 23)
        self.assertEqual(convert_far_to_cel(23), -5)


if __name__ == "__main__":
    unittest.main()
