class CalendarFactory:
    """Creates a markdown calendar from a
    list of dictionaries and outputs to a file"""
    def __init__(self, list_of_rows, out_file):
        self.list_of_rows = list_of_rows
        self.out_file = out_file
        self.calendar = self.make_title_row() + self.make_rows()
        self.write_to_file()

    def make_title_row(self):
        """:returns String of table title row"""
        col_title_string = '<table>\n  <tbody align="left">\n  <tr>\n'
        for col_titles in self.list_of_rows[0].keys():
            col_title_string += "      <th>{}</th>\n".format(col_titles)
        col_title_string += "    </tr>\n"

        return col_title_string

    def make_rows(self):
        """:returns String of table rows"""
        row_string = ""
        for row in self.list_of_rows:
            row_string += "    <tr>\n"
            for value in row.values():
                if value.startswith("http"):
                    start_slice = value.rfind("/") + 1
                    issue_number = value[start_slice:]
                    row_string += '      <td><a href="{}">#{}</a></td>\n'.format(
                        value, issue_number)
                else:
                    row_string += "      <td>{}</td>\n".format(value)
            row_string += "    </tr>\n"
        row_string += "  </tbody>\n</table>"

        return row_string

    def write_to_file(self):
        """Writes the calendar to file"""
        with open(self.out_file + ".md", "w") as f:
            f.write(self.calendar)