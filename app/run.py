#!/usr/bin/python

import os.path
import sys

# value = input("Input value: ")

cwd = os.getcwd()
name = (cwd  + "/db/output.txt")

f = open(name, "w")
f.write("The program was run with value: " + sys.argv[1])
f.close()
