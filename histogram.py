#!/usr/bin/env python3
# 
# Takes multiple lines of repetitive output and returns a freq list/histogram
# Vivek Sant <vsant@hcs.harvard.edu>
# 2016 Sept 21
# 

import sys

dict = {}
input = sys.stdin.read().strip().split('\n')

for i in input:
  if i in list(dict.keys()):
    dict[i] += 1
  else:
    dict[i] = 1

output = []

for i in list(dict.keys()):
  output.append("(%d) %s" % (dict[i], i))

output.sort()

for i in output:
  print(i)
