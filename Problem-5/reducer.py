#!/usr/bin/env python

from operator import itemgetter
from sys import stdin

myList = []
for line in stdin:
	line = line.strip()
	line = line.strip("\"")
	length = len(line)
	#length = length - 10
	line = line[0: length - 10]
	if line not in myList:
		myList.append(line)
        print "%s" % line
