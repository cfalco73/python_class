#!/usr/bin/env python

import json

test_list = range(5)
test_list.append('yo')
test_list.append({})
test_list[-1]
test_list[-1]['number'] = '1000'
test_list[-1]['stuff'] = 'chicago cubs'


with open("json_file.json", "w") as f:
  json.dump(test_list, f)


