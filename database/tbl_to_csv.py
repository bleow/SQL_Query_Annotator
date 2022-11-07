import csv
import os

def tbl_to_csv(filename):
    path = os.path.abspath(os.getcwd())
    # prevent csv writer from writing new line after every row
    csv_file = open("".join([path, "\\", filename, ".csv"]), "w+", newline='')
    tbl_file = open("".join([path, "\\", filename, ".tbl"]), "r")
    lines = tbl_file.readlines()
    for line in lines:
        # truncate \n at the end of every line
        csv.writer(csv_file).writerow(line.split('|')[:-1])
    tbl_file.close()
    csv_file.close()


if __name__ == "__main__":
    files = ['customer', 'lineitem', 'nation', 'orders', 'part', 'partsupp', 'region', 'supplier']
    for file in files:
        tbl_to_csv(file)
        break