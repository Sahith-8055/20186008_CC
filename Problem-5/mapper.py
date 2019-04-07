#!/usr/bin/env python

from sys import stdin

for line in stdin:
    line = line.strip()
    line = line.strip("[")
    line = line.strip("]")
    text = line.split(", ")
    print "%s" % text[1]
