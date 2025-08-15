import unittest


def add_numbers(x, y):
    return x + y

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(2, 2), 4)

    def test_add_numbers2(self):
        self.assertEqual(add_numbers(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
    n = input("test")
