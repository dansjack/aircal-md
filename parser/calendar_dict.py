import csv
from collections import OrderedDict


class CalendarDict:
    """
    Takes a csv file and filters the data into a dictionary.
      keys:   Column titles
      values: Column values
    """

    def __init__(self, csv_file):
        self.__csv_file = csv_file
        self.__count = 0
        # self.__table_dict_cols = self.fill_dict_by_col()
        self.__table_rows = self.fill_dict_by_row()

    def fill_dict_by_row(self):
        rows = list()
        with open(self.__csv_file, newline="", encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                rows.append(row)
        return rows

    @property
    def table_rows(self):
        """:returns: list of table rows"""
        return self.__table_rows
