from calendar import CalendarDict, CalendarFactory
from ui import UserInterface
from collections import OrderedDict
import unittest

# CalendarFactory(CalendarDict(
#
#  UserInterface.get_infile_path()).table_rows,
#   UserInterface.get_outfile_path())


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

    def test_ui_infile(self):
        """
        Tests whether a UserInterface Instance receives proper input types
        """

