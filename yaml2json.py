#!/usr/bin/env python

import json
import yaml
import sys

with open(sys.argv[1], 'r') as stream:
    y_obj = yaml.safe_load(stream)

print(json.dumps(y_obj))