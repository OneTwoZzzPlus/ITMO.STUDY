/system identity set name=R03.LBN
/user set [find name=admin] password=cfrekby

# IP
/interface bridge add name=lo0
/ip address 
add address=10.0.0.3/32 interface=lo0
add address=10.3.5.1/30 interface=ether2 comment="to R05.MSK"
add address=10.3.4.1/30 interface=ether3 comment="to R04.HKI"
add address=10.1.3.2/30 interface=ether4 comment="to R01.NYD"

# OSPF
/routing ospf instance set default router-id=10.0.0.3
/routing ospf network
add network=10.0.0.3/32 area=backbone
add network=10.3.5.0/30 area=backbone
add network=10.3.4.0/30 area=backbone
add network=10.1.3.0/30 area=backbone

# MPLS
/mpls ldp set enabled=yes lsr-id=10.0.0.3 transport-address=10.0.0.3
/mpls ldp interface 
add interface=ether2
add interface=ether3
add interface=ether4