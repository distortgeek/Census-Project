import csv
from os import remove
x=[]
a = ""
f = open("test.csv","r")
b = f.readline()
f = f.read().split("\n")
print(f)
for i in f:
    for j in i:
        if j == "'":
            f.split("'")
        elif j == ",":
            x.append(a)
            a = ""
        else:
            a = a+j
print(x)