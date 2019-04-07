#!/usr/bin/env python

from sys import stdin
import json

words = []
resultant = {}

for line in stdin:
	words = line.strip().split(" ",1)
	
	if (words[0] in resultant):
		resultant[words[0]].append(words[1])
	else:
		resultant[words[0]] = []
		resultant[words[0]].append(words[1])

jsonencoder = json.JSONEncoder()

for item in resultant:
	print(item), (resultant[item])
