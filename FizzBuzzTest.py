import unittest
import FizzBuzz


class FissBuzzTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_normal(self):
        self.assertEqual(1, FizzBuzz.fizzbuzz(1))

    def test_fizz(self):
        self.assertEqual("Fizz", FizzBuzz.fizzbuzz(3))

    def test_buzz(self):
        self.assertEqual("Buzz", FizzBuzz.fizzbuzz(5))

    def test_fizzbuzz(self):
        self.assertEqual("FizzBuzz", FizzBuzz.fizzbuzz(15))


if __name__ == "__main__":
    unittest.main()
