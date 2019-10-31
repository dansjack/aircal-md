from calendar import CalendarDict, CalendarFactory

print("\n\n*****************************************")
print("***** AIRTABLE TO MARKDOWN CALENDAR *****")
print("*****************************************\n")

csv = input("Enter the relative path of an Airtable csv file: ")
calendar_name = input("Enter the name of your new calendar: ") + ".md"

calendar_dict = CalendarDict(csv).table_rows
CalendarFactory(calendar_dict, calendar_name)

print("\n*****************************")
print("********** GOODBYE **********")
print("*****************************")
