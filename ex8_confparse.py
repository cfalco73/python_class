#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from __future__ import unicode_literals, print_function

cisco_config = CiscoConfParse("cisco_ipsec.txt")
crypto_map = cisco_config.find_objects(r"^crypto map CRYPTO")

for c in crypto_map:
  print ()
  print (c.text)
  for child in c.children:
      print(child.text)
  print()

