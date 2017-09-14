#!/usr/bin/env python
import os
import sys

search_string = sys.argv[1]
directory = sys.argv[2]

for root, dirs, files in os.walk(directory):
    for name in files:
        if name.find(search_string)!=-1:
            print(os.path.join(root, name))
