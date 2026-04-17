/system identity set name=R01.FRT
/user set [find name=admin] password=ahfyraehn

/ip address 
add address=172.16.23.1/30 interface=ether2
add address=172.16.12.2/30 interface=ether3
add address=192.168.20.1/24 interface=ether4

/ip route 
add dst-address=192.168.10.0/24 gateway=172.16.12.1
add dst-address=192.168.30.0/24 gateway=172.16.23.2

/ip pool add name=poolM ranges=192.168.20.10-192.168.20.253
/ip dhcp-server add name=dhcpM interface=ether4 address-pool=poolM
/ip dhcp-server network add address=192.168.20.0/24 gateway=192.168.20.1
/ip dhcp-server enable dhcpM
