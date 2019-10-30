from parser import CalendarDict

"""
 - Get csv file path from user
 - Get desired name of output file user
 - Initialize parser object with path
 - Loop through OrderedDict and fill markdown table template
"""

calendar_dict = CalendarDict("../monthly_view.csv").table_dict_rows


def make_col_titles(list_of_dicts):
    header_string = "<tr>\n"
    for headers in list_of_dicts[0].keys():
        header_string += "  <th>{}</th>\n".format(headers)
    header_string += "<tr>"

    print(header_string)

make_col_titles(calendar_dict)
