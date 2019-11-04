import unittest

from CsvReader import CsvReader
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

        csvData = CsvReader('./src/Unit_Test_Addition.csv').data
        for row in csvData:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_property_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 20), 10)
        self.assertEqual(self.calculator.subtract(5, 5), 0)
        csvData = CsvReader('./src/Unit_Test_Subtraction.csv').data
        for row in csvData:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_property_multiply(self):
        self.assertEqual(self.calculator.multiply(4, 4), 16)
        self.assertEqual(self.calculator.multiply(7, 8), 56)
        csvData = CsvReader('./src/Unit_Test_Multiplication.csv').data
        for row in csvData:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_property_divide(self):
        self.assertEqual(self.calculator.divide(2, 4), 2)
        self.assertEqual(self.calculator.divide(3, 12), 4)
        csvData = CsvReader('./src/Unit_Test_Division.csv').data
        for row in csvData:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']) )
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_property_square(self):
        self.assertEqual(self.calculator.square(5), 25)
        self.assertEqual(self.calculator.square(12), 144)
        csvData = CsvReader('./src/Unit_Test_Square.csv').data
        for row in csvData:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']) )
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_property_squareRoot(self):
        self.assertEqual(self.calculator.squareRoot(36), 6)
        self.assertEqual(self.calculator.squareRoot(100), 10)


if __name__ == '__main__':
    unittest.main()
