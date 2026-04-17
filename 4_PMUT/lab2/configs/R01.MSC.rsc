/system identity set name=R01.MSC
/user set [find name=admin] password=vjcrdf

/ip address 
add address=172.16.13.1/30 interface=ether2
add address=172.16.12.1/30 interface=ether3
add address=192.168.10.1/24 interface=ether4

/ip route 
add dst-address=192.168.20.0/24 gateway=172.16.12.2
add dst-address=192.168.30.0/24 gateway=172.16.13.2

/ip pool add name=poolM ranges=192.168.10.10-192.168.10.253
/ip dhcp-server add name=dhcpM interface=ether4 address-pool=poolM
/ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1
/ip dhcp-server enable dhcpM
