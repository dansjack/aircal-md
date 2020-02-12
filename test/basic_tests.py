import unittest
from collections import OrderedDict
from cal.calendar_dict import CalendarDict


class InputTests(unittest.TestCase):

    def setUp(self):
        self.data = '../test_infile.csv'
        self.table_rows = CalendarDict("../test_infile.csv").table_rows

    def test_cal_headers(self):
        self.assertEqual(list(self.table_rows[0].keys()),
                         ['Headline', 'Status', 'Section', 'Author',
                          'Draft due', 'Publish date', 'Link', 'Social posts'])

    def test_calendar_dict(self):
        """
        Tests whether a CalendarDict Instance's table_rows variable is a list
        of dictionaries
        """
        print()
        self.assertIsInstance(self.table_rows, list)
        for row in range(len(self.table_rows) - 1):
            self.assertIsInstance(self.table_rows[row], OrderedDict)

