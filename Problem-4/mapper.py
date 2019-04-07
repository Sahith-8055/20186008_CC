#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.strip("[").strip("]")
    line = line.replace("\"", "")
    user, friend = line.split(", ")
    print "%s\t%s" % (user, friend)
