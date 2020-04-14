import csv

file = open("csv_file.txt")
file = csv.reader(file)
for row in file:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
