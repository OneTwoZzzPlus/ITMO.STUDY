/system identity set name=R06.SPB
/user set [find name=admin] password=cfrekby

# IP
/interface bridge add name=lo0
/ip address 
add address=10.0.0.6/32 interface=lo0
add address=10.5.6.2/30 interface=ether3 comment="to R05.MSK"
add address=10.4.6.2/30 interface=ether4 comment="to R04.HKI"

# OSPF
/routing ospf instance set default router-id=10.0.0.6
/routing ospf network
add network=10.0.0.6/32 area=backbone
add network=10.5.6.0/30 area=backbone
add network=10.4.6.0/30 area=backbone

# MPLS
/mpls ldp set enabled=yes lsr-id=10.0.0.6 transport-address=10.0.0.6
/mpls ldp interface 
add interface=ether3
add interface=ether4

# EoMPLS (VPLS) to R01.NYD (10.0.0.1)
/interface vpls add name=vpls_to_NYD remote-peer=10.0.0.1 vpls-id=10:60 disabled=no

# Bridge to PC1
/interface bridge add name=bridge_eompls
/interface bridge port
add bridge=bridge_eompls interface=ether2
add bridge=bridge_eompls interface=vpls_to_NYD