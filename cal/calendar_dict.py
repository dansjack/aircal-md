import csv


class CalendarDict:
    """
    Takes a csv file and puts the data in a list of dicts.
    """

    def __init__(self, csv_file):
        """

        :param csv_file:
        """
        self._csv_file = csv_file
        self._count = 0
        self._table_rows = self._fill_list()

    def _fill_list(self):
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
