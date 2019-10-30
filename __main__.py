from parser import Parser

# parser = Parser("jane_table/monthly_view.csv") # command line
# print(parser.table_dict["Post Title"])
# print(parser.table_dict["Status"])
# print(parser.table_dict["Publish Date / Time"])
# print(parser.table_dict["Issue"])
# print(parser.table_dict["Author"])

"""
 - Get csv file path from user
 - Get desired name of output file user
 - Initialize parser object with path
 - Loop through OrderedDict and fill markdown table template
"""

parser2 = Parser("monthly_view.csv") # IDE
print(parser2.table_dict["Post Title"])
print(parser2.table_dict["Status"])
print(parser2.table_dict["Publish Date / Time"])
print(parser2.table_dict["Issue"])
print(parser2.table_dict["Author"])
