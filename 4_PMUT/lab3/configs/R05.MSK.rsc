/system identity set name=R05.MSK
/user set [find name=admin] password=cfrekby

# IP
/interface bridge add name=lo0
/ip address 
add address=10.0.0.5/32 interface=lo0
add address=10.3.5.2/30 interface=ether2 comment="to R03.LBN"
add address=10.5.6.1/30 interface=ether3 comment="to R06.SPB"

# OSPF
/routing ospf instance set default router-id=10.0.0.5
/routing ospf network
add network=10.0.0.5/32 area=backbone
add network=10.3.5.0/30 area=backbone
add network=10.5.6.0/30 area=backbone

# MPLS
/mpls ldp set enabled=yes lsr-id=10.0.0.5 transport-address=10.0.0.5
/mpls ldp interface 
add interface=ether2
add interface=ether3