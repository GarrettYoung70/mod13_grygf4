import unittest
from datetime import datetime

def symbol(symbol):
    if(symbol.isupper() == True and len(symbol) <= 6):
        return True
    else:
        return False

def chartType(type):
    if(type != 1 and type != 2):
        return False
    else:
        return True

def timeSeries(input):
    match input:
        case 1:
            return True
        case 2:
            return True
        case 3:
            return True
        case 4:
            return True
        case _:
            return False

def startDate(date):
    datetime_format = datetime.strptime(date, '%Y-%m-%d')
    return datetime_format

def endDate(date):
    datetime_format = datetime.strptime(date, '%Y-%m-%d')
    return datetime_format

class TestStockDataVisualizer(unittest.TestCase):

    def test_symbol(self):
        self.assertTrue(symbol('GOOGL'))
    
    def test_charttype(self):
        self.assertTrue(chartType(1))
        self.assertTrue(chartType(2))
    
    def test_timeseries(self):
        self.assertTrue(timeSeries(1))
        self.assertTrue(timeSeries(2))
        self.assertTrue(timeSeries(3))
        self.assertTrue(timeSeries(4))

    def test_startDate(self):
        self.assertEqual(startDate('2020-01-31'), datetime(2020, 1, 31))
    
    def test_endDate(self):
        self.assertEqual(endDate('2020-12-31'), datetime(2020, 12, 31))


if __name__ == '__main__':
    unittest.main()

