#!/usr/bin/env python

from sys import stdin
import json

friends = {}

for lines in stdin:
	personA, personB = lines.strip().split('\t', 1)
	if personA not in friends:
		friends[personA] = [personB]
	else:
		friends[personA].append(personB)

for number in friends.keys():
	print "[\"%s\", %d]" % (number, len(friends[number]))