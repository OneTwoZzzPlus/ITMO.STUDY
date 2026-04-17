/system identity set name=R01.TEST
/user set [find name=admin] password=hjenth

/interface vlan 
add name=vlan10 vlan-id=10 interface=ether2
add name=vlan20 vlan-id=20 interface=ether2

/ip address 
add address=192.168.10.1/24 interface=vlan10
add address=192.168.20.1/24 interface=vlan20

/ip pool add name=pool10 ranges=192.168.10.100-192.168.10.253
/ip dhcp-server add name=dhcp10 interface=vlan10 address-pool=pool10
/ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1
/ip dhcp-server enable dhcp10

/ip pool add name=pool20 ranges=192.168.20.100-192.168.20.253
/ip dhcp-server add name=dhcp20 interface=vlan20 address-pool=pool20
/ip dhcp-server network add address=192.168.20.0/24 gateway=192.168.20.1
/ip dhcp-server enable dhcp20
