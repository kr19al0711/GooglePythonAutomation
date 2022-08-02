#!/usr/bin/env python3

print("*" * 30)
print("Iterating over file lines using a for loop")
print("*" * 30)

with open("lyrics.txt") as file:
    for line in file:
        print(line)

print("*" * 30)
print("Iterating over file using list")
print("*" * 30)

file = open("lyrics.txt")
lines = file.readlines()

print(lines)

for line in lines:
    print(line.strip())
