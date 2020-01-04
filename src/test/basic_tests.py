from collections import OrderedDict
from src.cal.calendar_dict import CalendarDict
import unittest


class InputTests(unittest.TestCase):

    def test_calendar_dict(self):
        """
        Tests whether a CalendarDict Instance's table_rows variable is a list
        of dictionaries
        """
        table_rows = CalendarDict("test_infile.csv").table_rows
        self.assertIsInstance(table_rows, list)
        for row in range(len(table_rows) - 1):
            self.assertIsInstance(table_rows[row], OrderedDict)

