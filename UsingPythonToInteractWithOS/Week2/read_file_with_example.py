#!/usr/bin/env python3

with open("LoremIpsum.txt") as file:
    print("\n Reading from the with block \n*********************************************\n")
    print(file.read())
