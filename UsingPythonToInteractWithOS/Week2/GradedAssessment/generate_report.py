#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):

    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    file = open(csv_file_location)
    employee_file = csv.DictReader(file, dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    file.close()
    return employee_list

def process_data(employee_list):

    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in department_list:
        department_data[department_name] = department_list.count(department_name)
    return department_data

def write_report(dictionary, report_file):

    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()


employee_list = read_employees("/home/student-04-7b304cee17ce/data/employees.csv")
department_data = process_data(employee_list)
write_report(department_data,"/home/student-04-7b304cee17ce/test_report.txt")
