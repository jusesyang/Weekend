
import csv
import os


def read(filename):

    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/" + filename)
    result = []
    with open(path, "r") as file:
        data_table = csv.reader(file)
        for row in data_table:
            result.append(row)
    return result

    file.close()



if __name__ == '__main__':
    read("member_info.csv")
