class UserInterface:
    @staticmethod
    def print_greeting():
        print("\n\n*****************************************")
        print("***** AIRTABLE TO MARKDOWN CALENDAR *****")
        print("*****************************************\n")

    @staticmethod
    def print_goodbye():
        print("\n*****************************")
        print("********** GOODBYE **********")
        print("*****************************\n ")

    @staticmethod
    def get_infile_path():
        while True:
            try:
                csv = input("Enter the relative path of an Airtable csv file: ")
                if not csv.endswith(".csv"):
                    csv += ".csv"
                    print(csv)
                break
            except FileNotFoundError:
                print('''Sorry, there is no file by that name at that path.\n''')
        return csv

    @staticmethod
    def get_outfile_path():
        while True:
            calendar_name = input("Enter the name of your new calendar: ")
            break
        return calendar_name

