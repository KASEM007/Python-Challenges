from collections import defaultdict
from itertools import chain

grades = {}
firstname = {}
lastname = {}
with open ("Grades.txt") as f:
    for line in f:
        firstname, lastname, score = line.split (" , , ")
        grades [firstname, lastname] = int (score)

for firstname, lastname in grades:
    print(firstname, lastname, grades [firstname, lastnamee], sep=": ")

print("Total average (student average):",
      sum(grades.values ()) / len(grades))