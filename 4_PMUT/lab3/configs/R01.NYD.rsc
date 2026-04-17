/system identity set name=R01.NYD
/user set [find name=admin] password=cfrekby

# IP
/interface bridge add name=lo0
/ip address 
add address=10.0.0.1/32 interface=lo0
add address=10.1.2.1/30 interface=ether2 comment="to R02.LND"
add address=10.1.3.1/30 interface=ether3 comment="to R03.LBN"

# OSPF
/routing ospf instance set default router-id=10.0.0.1
/routing ospf network
add network=10.0.0.1/32 area=backbone
add network=10.1.2.0/30 area=backbone
add network=10.1.3.0/30 area=backbone

# MPLS
/mpls ldp set enabled=yes lsr-id=10.0.0.1 transport-address=10.0.0.1
/mpls ldp interface 
add interface=ether2
add interface=ether3

# EoMPLS (VPLS) to R06.SPB (10.0.0.6)
/interface vpls add name=vpls_to_SPB remote-peer=10.0.0.6 vpls-id=10:60 disabled=no

# Bridge to SGI
/interface bridge add name=bridge_eompls
/interface bridge port
add bridge=bridge_eompls interface=ether4
add bridge=bridge_eompls interface=vpls_to_SPB
