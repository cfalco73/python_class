#!/usr/bin/env python


from __future__ import print_function, unicode_literals
from snmp_helper import snmp_get_oid,snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161

MIB_DESC = '1.3.6.1.2.1.1.1.0'
MIB_NAME = '1.3.6.1.2.1.1.5.0'


router_1 = ("184.105.247.70", COMMUNITY_STRING, SNMP_PORT)
router_2 = ("184.105.247.71", COMMUNITY_STRING, SNMP_PORT)

for router_device in (router_1, router_2):
    for oid_info in (MIB_DESC, MIB_NAME):
        snmp_info = snmp_get_oid(router_device, oid=oid_info)
        output = snmp_extract(snmp_info)
        print (output)
print()

