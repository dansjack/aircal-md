from calendar import CalendarDict, CalendarFactory
from collections import OrderedDict
import unittest


class InputTests(unittest.TestCase):
    def setUp(self):
        self.table_rows = CalendarDict("test_infile.csv").table_rows
        self.out_file = "test_outfile.md"

    def test_calendar_dict(self):
        """
        Tests whether a CalendarDict Instance's table_rows variable is a list
        of dictionaries
        """

        # CalendarDict's table_rows returns a list
        self.assertIsInstance(self.table_rows, list)
        for row in range(len(self.table_rows) - 1):
            # Each row in the list is an OrderedDict
            self.assertIsInstance(self.table_rows[row], OrderedDict)

    def test_calendar_factory(self):
        """
        Tests whether the CalendarFactory creates a markdown calendar
        """
        CalendarFactory(self.table_rows, self.out_file)

    def test_ui_infile(self):
        """
        Tests whether a UserInterface Instance receives proper input types
        """

