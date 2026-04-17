/system identity set name=R02.LND
/user set [find name=admin] password=cfrekby

# IP
/interface bridge add name=lo0
/ip address 
add address=10.0.0.2/32 interface=lo0
add address=10.2.4.1/30 interface=ether2 comment="to R04.HKI"
add address=10.1.2.2/30 interface=ether3 comment="to R01.NYD"

# OSPF
/routing ospf instance set default router-id=10.0.0.2
/routing ospf network
add network=10.0.0.2/32 area=backbone
add network=10.2.4.0/30 area=backbone
add network=10.1.2.0/30 area=backbone

# MPLS
/mpls ldp set enabled=yes lsr-id=10.0.0.2 transport-address=10.0.0.2
/mpls ldp interface 
add interface=ether2
add interface=ether3