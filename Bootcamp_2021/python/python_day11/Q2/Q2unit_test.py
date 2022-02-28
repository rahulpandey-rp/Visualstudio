import unittest
from FileToTest import sum_of_digit


class TestSum(unittest.TestCase):
    def test_value_error(self):
        with self.assertRaises(TypeError):
            sum_of_digit("a")

    def test_correct_value(self):
        self.assertEqual(sum_of_digit(132),6)

if __name__ == "__main__":
    unittest.main()