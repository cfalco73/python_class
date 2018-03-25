#!/usr/bin/env python


from __future__ import unicode_literals, print_function
from ciscoconfparse import CiscoConfParse

cisco_config = CiscoConfParse("cisco_ipsec.txt")
crypto_map = cisco_config.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")

for c in crypto_map:
  print ()
  print (c.text)
  for child in c.children:
      print(child.text)
  print()


