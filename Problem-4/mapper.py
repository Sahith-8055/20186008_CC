#!/usr/bin/env python

from sys import stdin

for line in stdin:
	line = line.strip()
	line = line.strip("[")
	line = line.strip("]")
	line = line.replace("\"","")
	user,friend = line.split(", ")
    print "%s\t%s" % (user, friend)
