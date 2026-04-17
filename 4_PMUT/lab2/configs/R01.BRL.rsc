/system identity set name=R01.BRL
/user set [find name=admin] password=,thkby

/ip address 
add address=172.16.13.2/30 interface=ether2
add address=172.16.23.2/30 interface=ether3
add address=192.168.30.1/24 interface=ether4

/ip route 
add dst-address=192.168.10.0/24 gateway=172.16.13.1
add dst-address=192.168.20.0/24 gateway=172.16.23.1

/ip pool add name=poolM ranges=192.168.30.10-192.168.30.253
/ip dhcp-server add name=dhcpM interface=ether4 address-pool=poolM
/ip dhcp-server network add address=192.168.30.0/24 gateway=192.168.30.1
/ip dhcp-server enable dhcpM
