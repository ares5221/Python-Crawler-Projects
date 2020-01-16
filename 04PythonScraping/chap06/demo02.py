#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import csv
with open('test.csv', 'r',encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)
        print(row[0])


import csv
output_list = ['1', '2','3','4']
with open('test2.csv', 'a+', encoding='utf-8', newline='') as csvfile:
    w = csv.writer(csvfile)
    w.writerow(output_list)