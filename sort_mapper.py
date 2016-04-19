#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sorted(sys.stdin):
    print(line[:-1])
