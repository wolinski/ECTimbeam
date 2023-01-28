import csv

class CsvReader:
    """
    Class which reads csv file.
    """
    def __init__(self, path):
        """
        Parameters:
        -----------
        path: string
            path of csv file
        """
        self.csv_path = path

    def __is_comment(self, line):
        """
        Checks if line in csv is comment.
        Parameters:
        -----------
        line: string
        """
        return line.startswith("#")

    def __is_whitespace(self, line):
        """
        Checks if line in csv is whitespace.
        Parameters:
        -----------
        line: string
        """
        return line.isspace()

    def __decomment(self, csvfile):
        """
        Allows to ignore all comments and whitelines in csv file.
        Parameters:
        -----------
        csvfile: object
            path to csv file 
        """
        for row in csvfile:
            if self.__is_comment(row) is False and self.__is_whitespace(row) is False:
                yield row

    def get_key_value(self, key_name = "name", key_value = "C24", prop_name = "E_0mean"):
        """
        Reurns value of property name (prop_name) for given category name.
        For instance: returns E_0mean value for C24 class 
        Parameters:
        -----------
        key_name: string
            name of column with names for each row.
        key_value: string
            name of searched row.
        prop_name: string
            name of column with searched property
        Returns:
        -----------
        string with value of searched property
        """
        with open(self.csv_path) as file:
            reader = csv.DictReader(self.__decomment(file))

            result = {}
            for d in reader:
                if d[key_name] == key_value:
                    result[d[key_name]] = d[prop_name]
            return(result[key_value])


if __name__ == "__main__":
    csvreader = CsvReader(path="data\wood_classes.csv")
    print(csvreader.get_key_value())
