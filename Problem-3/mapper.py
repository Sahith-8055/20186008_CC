#!/usr/bin/env python

from sys import stdin
import json

def mapper(record):
    personA = record[0]
    personB = record[1]
    print "%s\t%s" % (personA, personB)


for line in stdin:
	lis = json.loads(line)
	mapper(lis)