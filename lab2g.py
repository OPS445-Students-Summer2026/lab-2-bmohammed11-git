#!/usr/bin/env python3

# Author: Bapi Mohammed
# Author ID: 113151245
# Date Created: 2026/06/19

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')