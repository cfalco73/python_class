#!/usr/bin/env python

import yaml

test_list = range(5)
test_list.append('yo')
test_list.append({})
test_list[-1]
test_list[-1]['number'] = '1000'
test_list[-1]['stuff'] = 'chicago cubs'


with open("yaml_file.yml", "w") as f:
   f.write(yaml.dump(test_list, default_flow_style=False))


