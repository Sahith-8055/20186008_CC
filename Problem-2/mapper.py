#!/usr/bin/env python

from sys import stdin
import json

index = {}

def mapper(record):

	order_id = record[1]
	index.setdefault(order_id, [])
	index[order_id] = record
	print order_id, index[order_id]

for line in stdin:
	record = json.loads(line)
	mapper(record)