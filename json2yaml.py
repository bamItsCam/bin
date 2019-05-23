#!/usr/bin/env python

import json
import yaml
import sys

with open(sys.argv[1], 'r') as stream:
    j_obj = json.load(stream)

print(yaml.dump(j_obj))