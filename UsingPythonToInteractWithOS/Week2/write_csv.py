#!/usr/bin/ python3

import csv

list = [["Jacenta","Ursulette","Albania"],["Cissiee","Bollay","French Guiana"],["Jemie","Frodi","Haiti"]]

with open("csv_file2.csv","w") as file:
  writer = csv.writer(file)
  writer.writerows(list)
