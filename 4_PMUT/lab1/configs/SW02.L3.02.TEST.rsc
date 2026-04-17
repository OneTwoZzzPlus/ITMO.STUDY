/system identity set name=SW02.L3.02.TEST
/user set [find name=admin] password=ghfdsq

/interface bridge add name=bridge1 vlan-filtering=yes
/interface bridge port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3 pvid=20
/interface bridge vlan
add bridge=bridge1 vlan-ids=10 tagged=ether2
add bridge=bridge1 vlan-ids=20 tagged=ether2 untagged=ether3
