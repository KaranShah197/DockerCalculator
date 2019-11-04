import unittest
from DockerCalculator import DockerCalculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = DockerCalculator()

    def test_instantiate_calculator(self):
        # calculator = DockerCalculator()
        self.assertIsInstance(self.calculator, DockerCalculator)

    def test_property_add(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.add(15, 5), 20)

    def test_property_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 20), 10)
        self.assertEqual(self.calculator.subtract(5, 5), 0)


if __name__ == '__main__':
    unittest.main()
