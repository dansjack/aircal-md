import csv
from collections import OrderedDict


class Parser:
    """

    """
    def __init__(self, csv_file):
        self.__csv_file = csv_file
        self.__count = 0
        self.__table_dict = self.fill_dict()

    def fill_dict(self):
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

    @property
    def table_dict(self):
        """:returns: dictionary"""
        return self.__table_dict

    def __str__(self):
        return ''.join('{}{}'.format(key, val) for key, val in
                       self.table_dict.items())
