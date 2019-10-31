import csv


class CalendarDict:
    """
    Takes a csv file and filters the data into a dictionary.
      keys:   Column titles
      values: Column values
    """
    def __init__(self, csv_file):
        self._csv_file = csv_file
        self._count = 0
        self._table_rows = self._fill_dict_by_row()

    def _fill_dict_by_row(self):
        """:returns a list of dictionaries"""
        rows = list()
        with open(self._csv_file, newline="", encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                rows.append(row)
        return rows

    @property
    def table_rows(self):
        """:returns: list of table rows"""
        return self._table_rows
