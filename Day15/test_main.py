import unittest

from main import check_resources, report

class TestCoffee(unittest.TestCase):
    def test_check_resources(self):
        self.assertEqual(check_resources('espresso'), {
             "water": 50,
            "coffee": 18,
        })

    def test_report(self):
        self.assertEqual(report(), ['Water: 300ml\n', 'Milk: 200ml\n', 'Coffee: 100g\n', 'Money: $0\n'])


if __name__ == '__main__':
    unittest.main()