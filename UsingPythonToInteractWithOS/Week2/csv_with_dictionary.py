#!/usr/bin/ python3

import csv

with open("csv_file3.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("First Name : {:<10s} Last Name : {:<15s}".format(row["firstname"],row["lastname"]))
        

list_csv = [{"name" : "Kripal","age": 23 ,"city": "Mapusa" },
{"name" : "Enaki","age": 18,"city": "London"},
{"name" : "Messi","age": 34,"city": "Buenos Aires" },
{"name" : "Iniesta","age": 35 ,"city": "Barcelona" }]

list_keys = ["name","age","city"]

with open("csv_file4.csv","w",newline = '') as file:
    writer = csv.DictWriter(file,fieldnames = list_keys)
    writer.writerows(list_csv)
    