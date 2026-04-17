/system identity set name=SW01.L3.01.TEST
/user set [find name=admin] password=wtynh

/interface bridge add name=bridge1 vlan-filtering=yes
/interface bridge port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
/interface bridge vlan
add bridge=bridge1 vlan-ids=10 tagged=ether2,ether3
add bridge=bridge1 vlan-ids=20 tagged=ether2,ether4
