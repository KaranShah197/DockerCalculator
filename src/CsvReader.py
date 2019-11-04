import csv
from pathlib import Path


def classFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


def absolutePath(filepath):
    relative = Path(filepath)
    return relative.absolute()


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []

        with open(absolutePath(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(classFactory(class_name, row))
        return objects

