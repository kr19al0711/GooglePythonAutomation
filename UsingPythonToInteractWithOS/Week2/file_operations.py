#!/usr/bin/env python3

import os
import datetime

print("Checking if file named \"text.txt\" exist ")

print(os.path.exists("text.txt"))    

print("Creating a file named \"text.txt\" ")

with open("text.txt","w") as file:
	file.write("Writing some random stuff")
	
print(os.path.exists("text.txt"))

print("Renaming file to \"test.txt\" ")

os.rename("text.txt","test.txt")

with open("test.txt") as file:
    for line in file:
        print(line)
        

        
file_size = os.path.getsize("test.txt")
print("{} bytes".format(file_size))

abs_path = os.path.abspath("test.txt")
print(abs_path)

time_stamp = os.path.getmtime("test.txt")
print(time_stamp)

time_stamp_formatted = datetime.datetime.fromtimestamp(time_stamp)
print(time_stamp_formatted)


os.remove("test.txt")

