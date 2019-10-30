from parser import Parser

parser = Parser("monthly_view.csv")
print(parser.table_dict["Post Title"])
print(parser.table_dict["Status"])
print(parser.table_dict["Publish Date / Time"])
print(parser.table_dict["Issue"])
print(parser.table_dict["Author"])
