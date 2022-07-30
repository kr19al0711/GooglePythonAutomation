#!/usr/bin/env python3

import areas

radius = 4
base = 3
height = 6
length = 5
breadth = 7


print("Area of Circle with radius {} is {:.4f}".format(radius, areas.circle(radius)))

print("Area of Triangle with base {}  and height {} is {}".format(base, height ,areas.triangle(base,height)))

print("Area of Rectangle with length {}  and breadth {} is {}".format(length, breadth ,areas.rectangle(length,breadth)))
