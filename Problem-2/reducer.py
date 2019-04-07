#!/usr/bin/env python

from sys import stdin
import ast

order = {}
line_item = {}
result = {}

for line in stdin:
	val = line.strip().split(" ", 1)

	record = eval(val[1])

	if (record[0] == "order"):
		order[val[0]] = record
	elif (record[0] == "line_item"):
		if (val[0] in line_item):
			line_item[val[0]].append(record)
		else:
			line_item[val[0]] = [record]

count = 1
for key in line_item:
	for value in line_item[key]:
		result[count] = order[key] + value
		count += 1
	
for keys in result:
 	print result[keys]