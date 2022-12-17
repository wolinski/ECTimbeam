import csv

class CsvReader:
    def __init__(self, path):
        self.csv_path = path

    def is_comment(self, line):
        return line.startswith("#")

    def is_whitespace(self, line):
        return line.isspace()

    def decomment(self, csvfile):
        for row in csvfile:
            if self.is_comment(row) is False and self.is_whitespace(row) is False:
                yield row

    def get_key_value(self, key_name = "name", key_value = "C24", prop_name = "E_0mean"):
        with open(self.csv_path) as file:
            reader = csv.DictReader(self.decomment(file))

            result = {}
            for d in reader:
                if d[key_name] == key_value:
                    result[d[key_name]] = d[prop_name]
            return(result[key_value])


if __name__ == "__main__":
    csvreader = CsvReader(path="data\wood_classes.csv")
    print(csvreader.get_key_value())
