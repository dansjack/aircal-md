from parser import CalendarDict

# c_dict1 = CalendarDict("jane_table/monthly_view.csv") # command line
# print(c_dict1.table_dict_cols["Post Title"])
# print(c_dict1.table_dict_cols["Status"])
# print(c_dict1.table_dict_cols["Publish Date / Time"])
# print(c_dict1.table_dict_cols["Issue"])
# print(c_dict1.table_dict_cols["Author"])

"""
 - Get csv file path from user
 - Get desired name of output file user
 - Initialize parser object with path
 - Loop through OrderedDict and fill markdown table template
"""

c_dict2 = CalendarDict("monthly_view.csv")  # IDE
# print(c_dict2.table_dict_cols["Post Title"])
# print(c_dict2.table_dict_cols["Status"])
# print(c_dict2.table_dict_cols["Publish Date / Time"])
# print(c_dict2.table_dict_cols["Issue"])
# print(c_dict2.table_dict_cols["Author"])

print(c_dict2.table_dict_rows)
