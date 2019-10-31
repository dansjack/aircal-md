from calendar import CalendarDict, CalendarFactory

"""
 - Get csv file path from user
 - Get desired name of output file user
 - Initialize calendar object with path
 - Loop through OrderedDict and fill markdown table template
"""
print("*****************************************")
print("***** AIRTABLE TO MARKDOWN CALENDAR *****")
print("*****************************************\n")

csv = input("Enter the relative path of an Airtable csv file: ")
calendar_name = input("Enter the name of your new calendar: ")

calendar_dict = CalendarDict(csv).table_rows
CalendarFactory(calendar_dict, calendar_name)

# open_file = input("Open file? (y/n)")
# if open_file is "y":
#     open(calendar_name)
