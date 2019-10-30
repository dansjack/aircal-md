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
        self.__table_dict_cols = self.fill_dict_by_col()
        self.__table_dict_rows = self.fill_dict_by_row()

    def fill_dict_by_col(self):
        """
        Read and sort a csv file into a dictionary
        :returns: dictionary
        """
        table_dict = OrderedDict()
        with open(self.__csv_file, newline="", encoding='utf-8-sig') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if self.__count < 1:
                    for j in range(len(row)):
                        table_dict[row[j].strip()] = list()
                else:
                    self.__count = 1

                    for key in table_dict.keys():
                        table_dict[key].append(row[self.__count - 1].strip())
                        self.__count += 1

                self.__count += 1
        return table_dict

    def fill_dict_by_row(self):
        rows = list()
        with open(self.__csv_file, newline="", encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                rows.append(row)
        return rows

    @property
    def table_dict_cols(self):
        """:returns: dictionary of table columns"""
        return self.__table_dict_cols

    @property
    def table_dict_rows(self):
        """:returns: list of table rows"""
        return self.__table_dict_rows

    def __str__(self):
        return ''.join('{}{}'.format(key, val) for key, val in
                       self.table_dict_cols.items())
