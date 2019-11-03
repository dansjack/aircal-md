import csv, sys


class CalendarDict:
    """
    Takes a csv file and filters the data into a dictionary.
      keys:   Column titles
      values: Column values
    """
    def __init__(self, csv_file):
        self._csv_file = csv_file
        self._count = 0
        self._table_rows = self._fill_list()

    def _fill_list(self):
        """:returns a list of dictionaries"""
        rows = list()
        while True:
            if self._csv_file.lower()[0] is "q":
                sys.exit()
            try:
                with open(self._csv_file, newline="",
                          encoding='utf-8-sig') as csv_file:
                    reader = csv.DictReader(csv_file)
                    for row in reader:
                        rows.append(row)
                break
            except FileNotFoundError:
                print('''Sorry, there's no file by that name at that path.\n''')
                self._csv_file = input(
                    "Try another path or (q)uit: ")
        return rows

    @property
    def table_rows(self):
        """:returns: list of table rows"""
        return self._table_rows
