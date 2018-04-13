

import pyeapi


pynet_sw3 = pyeapi.connect_to("pynet-sw3")

show_int = pynet_sw3.enable("show interfaces")
show_int = show_int[0]
show_int = show_int["result"]
show_int = show_int["interfaces"]

int_stats = {}
for int, int_values in show_int.items():
    counters = int_values.get('interfaceCounters', {})
    int_stats[int] = (counters.get('inOctets'), counters.get('outOctets'))


print("\n{} {} {}".format("interface:", "inOctets", "outOctets"))
for intf, octets in sorted(int_stats.items()):
    print ("{} {} {}".format(intf, (octets[0]), (octets[1])))

print()
