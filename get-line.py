#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE

stdin = sys.stdin.read().split('\n')

if len(sys.argv) == "1":
	sys.exit(0)

for i in sys.argv[1:]:
	print stdin[int(i)-1]
