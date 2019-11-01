from calendar import CalendarDict, CalendarFactory
from ui import UserInterface


UserInterface().print_greeting()
in_file = UserInterface.get_infile_path()
rows = CalendarDict(in_file).table_rows
CalendarFactory(rows, UserInterface.get_outfile_path())

UserInterface().print_goodbye()
