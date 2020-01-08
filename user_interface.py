from pathlib import Path
from cal.calendar_dict import CalendarDict
from cal.calendar_factory import CalendarFactory


class UserInterface:
    @staticmethod
    def print_greeting():
        print("\n\n*****************************************")
        print("*************   AIRCAL-MD   *************")
        print("*****************************************\n")

    @staticmethod
    def print_goodbye():
        print("\n*****************************")
        print("********** GOODBYE **********")
        print("*****************************\n ")

    @staticmethod
    def validate_infile(file):
        """:return boolean. true if file exists at path. false if not """
        try:
            f = open(str(file))
            f.close()
            return True
        except FileNotFoundError:
            return False

    @staticmethod
    def main():
        UserInterface.print_greeting()
        user_infile = input("Enter the relative path of an Airtable csv "
                           "file: ")
        while True:
            if user_infile.lower().startswith("q"):  # user quits loop
                break

            if not user_infile.endswith(".csv"):
                user_infile += ".csv"

            user_infile = (Path(__file__).parent / user_infile).resolve()

            if UserInterface.validate_infile(user_infile):  # infile valid
                user_outfile = input("Enter the name of your new cal: ")

                if str(user_infile).lower().startswith("q"):  # user quits loop
                    break

                rows = CalendarDict(user_infile).table_rows
                CalendarFactory(rows, user_outfile)
                break
            else:
                print("File not found at '{}', please try again".format(user_infile))
                user_infile = input("Enter the relative path of an Airtable csv "
                                   "file: ")

        UserInterface.print_goodbye()
