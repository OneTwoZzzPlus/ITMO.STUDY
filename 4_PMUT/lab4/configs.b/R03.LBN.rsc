/system identity set name=R03.LBN
/user set [find name=admin] password=cfrekby

# IP
/interface bridge add name=lo0
/ip address
add address=10.0.0.33/32 interface=lo0
add address=10.11.33.2/30 interface=ether2 comment="to R01.HKI"
add address=10.22.33.2/30 interface=ether3 comment="to R02.LND"
add address=10.33.30.1/30 interface=ether4 comment="to R03.SVL"

# OSPF
/routing ospf instance set default router-id=10.0.0.33
/routing ospf network
add network=10.0.0.33/32 area=backbone
add network=10.11.33.0/30 area=backbone
add network=10.22.33.0/30 area=backbone
add network=10.33.30.0/30 area=backbone

# MPLS
/mpls ldp set enabled=yes transport-address=10.0.0.33 lsr-id=10.0.0.33
/mpls ldp interface 
add interface=ether2
add interface=ether3
add interface=ether4

# iBGP RR
/routing bgp instance set default as=65000 router-id=10.0.0.33 redistribute-connected=yes client-to-client-reflection=yes

/routing bgp peer
# Cluster RR
add name=to_HKI remote-address=10.0.0.11 remote-as=65000 update-source=lo0 address-families=vpnv4,l2vpn
add name=to_LND remote-address=10.0.0.22 remote-as=65000 update-source=lo0 address-families=vpnv4,l2vpn
# Client (SVL)
add name=to_SVL remote-address=10.0.0.30 remote-as=65000 update-source=lo0 route-reflect=yes address-families=vpnv4,l2vpn