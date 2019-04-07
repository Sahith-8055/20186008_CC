#!/usr/bin/env python

from sys import stdin
from operator import itemgetter

relations = []
for line in stdin:
	line = line.strip()
	data = line.split('\t', 1)
	normaldata = [data[0], data[1]]
	if normaldata not in relations:
		relations.append(normaldata)
	else:
		relations.remove(normaldata)
	reversedata = [data[1], data[0]]
	if reversedata not in relations:
		relations.append(reversedata)
	else:
		relations.remove(reversedata)
for relation in relations:
	print '%s' % relation
