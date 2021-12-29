# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 08:51:31 2021

@author: BMSIT
"""

import csv

with open('findsdataset.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

h = ['0', '0', '0', '0', '0', '0']

for entry in your_list:
    print(entry)
    if entry[-1] == "TRUE":
        j = 0
        for parameter in entry:
            if parameter != "TRUE":
                if parameter != h[j] and h[j] == '0':
                    h[j] = parameter
                elif parameter != h[j] and h[j] != '0':
                    h[j] = '?'
                else:
                    pass
            j += 1
print("A Maximally Specific hypothesis is")
print(h)