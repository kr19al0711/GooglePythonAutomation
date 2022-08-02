#!/usr/bin/ python3

import csv

with open("csv_file1.csv") as file:
    
    file_csv_reader = csv.reader(file)
    for row in file_csv_reader:
        id,first_name,last_name,email,profession = row
        print("ID: {} First Name: {:<15s} Last Name: {:<15s} Email:{:<35s} Profession:{}".format(id,first_name,last_name,email,profession)  )