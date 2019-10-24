import unittest
from DockerCalculator import DockerCalculator

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = DockerCalculator()
        self.assertIsInstance(calculator, DockerCalculator)


if __name__ == '__main__':
    unittest.main()
