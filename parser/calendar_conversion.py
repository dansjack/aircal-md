from parser import CalendarDict

"""
 - Get csv file path from user
 - Get desired name of output file user
 - Initialize parser object with path
 - Loop through OrderedDict and fill markdown table template
 - MAKE ALL COLUMNS LEFT ALIGNED
 - ADD ANCHOR TAGS FOR EACH LINK
"""

calendar_dict = CalendarDict("../monthly_view.csv").table_rows


class MarkdownCalendar:
    def __init__(self, list_of_rows):
        self.list_of_rows = list_of_rows
        self.calendar = self.make_col_titles() + self.make_rows()

    def make_col_titles(self):
        col_title_string = "<table>\n  <tbody>\n  <tr>\n"
        for col_titles in self.list_of_rows[0].keys():
            col_title_string += "      <th>{}</th>\n".format(col_titles)
        col_title_string += "    </tr>\n"

        return col_title_string

    def make_rows(self):
        row_string = ""
        for row in self.list_of_rows:
            row_string += "    <tr>\n"
            for values in row.values():
                row_string += "      <td>{}</td>\n".format(values)
            row_string += "    </tr>\n"
        row_string += "  </tbody>\n</table>"

        return row_string


print(MarkdownCalendar(calendar_dict).calendar)
