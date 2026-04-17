/system identity set name=SW02.L3.01.TEST
/user set [find name=admin] password=ktdsq

/interface bridge add name=bridge1 vlan-filtering=yes
/interface bridge port
add bridge=bridge1 interface=ether2 
add bridge=bridge1 interface=ether3 pvid=10
/interface bridge vlan
add bridge=bridge1 vlan-ids=10 tagged=ether2 untagged=ether3
add bridge=bridge1 vlan-ids=20 tagged=ether2
