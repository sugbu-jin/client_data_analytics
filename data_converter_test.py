import unittest
from data_converter import DataConverter
import json
import pathlib as pl


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

class SimpleTest(unittest.TestCase):

    def validateJSON(self, jsonData):
        try:
            json.loads(jsonData)
        except ValueError as err:
            return False
        return True


    def test_isInValidFile(self):
        path = pl.Path('data/bad_data.txt')
        self.assertFalse(DataConverter().isValidFile(path))

    def test_isValidFile(self):
        path = pl.Path('data/data.csv')
        self.assertTrue(DataConverter().isValidFile(path))


    def test_jsonDataSuccess(self):
        self.assertTrue(validateJSON(DataConverter().convert_csv2json(filepath = 'data/data.csv')))

    def test_jsonDataFail(self):
        self.assertFalse(validateJSON(DataConverter().convert_csv2json(filepath = 'data/data.csv') + '}'))


if __name__ == '__main__':
   unittest.main()