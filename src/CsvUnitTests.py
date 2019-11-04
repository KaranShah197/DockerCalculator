import unittest
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.csvReader = CsvReader('./src/Unit_Test_Addition.csv')

    def test_instantiate_csvReader(self):
        self.assertIsInstance(self.csvReader, CsvReader)


if __name__ == '__main__':
    unittest.main()
