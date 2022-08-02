#!/usr/bin/env python3

file = open("LoremIpsum.txt")

print("Reading a single line from the file \n ************************************************* \n")
print(file.readline())

print("Reading till the end of the file \n ************************************************* \n")
print(file.read())

file.close()
