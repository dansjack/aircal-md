from parser import CalendarDict

"""
 - Get csv file path from user
 - Get desired name of output file user
 - Initialize parser object with path
 - Loop through OrderedDict and fill markdown table template
"""

calendar_dict = CalendarDict("../monthly_view.csv").table_rows


class MarkdownCalendar:
    def __init__(self, list_of_rows):
        self.list_of_rows = list_of_rows
        self.calendar = self.make_col_titles()

    def make_col_titles(self):
        header_string = "<tr>\n"
        for col_titles in self.list_of_rows[0].keys():
            header_string += "  <th>{}</th>\n".format(col_titles)
        header_string += "</tr>"

        return header_string

    def make_row(self, dict_row):
        row_string = "<tr>\n"
        for values in dict_row.values():
            row_string += "  <td>{}</td>\n".format(values)
        row_string += "</tr>"

        return row_string


print(MarkdownCalendar(calendar_dict).calendar)
