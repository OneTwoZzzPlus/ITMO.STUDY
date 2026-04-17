/system identity set name=R04.HKI
/user set [find name=admin] password=cfrekby

# IP
/interface bridge add name=lo0
/ip address 
add address=10.0.0.4/32 interface=lo0
add address=10.2.4.2/30 interface=ether2 comment="to R02.LND"
add address=10.3.4.2/30 interface=ether3 comment="to R03.LBN"
add address=10.4.6.1/30 interface=ether4 comment="to R06.SPB"

# OSPF
/routing ospf instance set default router-id=10.0.0.4
/routing ospf network
add network=10.0.0.4/32 area=backbone
add network=10.2.4.0/30 area=backbone
add network=10.3.4.0/30 area=backbone
add network=10.4.6.0/30 area=backbone

# MPLS
/mpls ldp set enabled=yes lsr-id=10.0.0.4 transport-address=10.0.0.4
/mpls ldp interface 
add interface=ether2
add interface=ether3
add interface=ether4