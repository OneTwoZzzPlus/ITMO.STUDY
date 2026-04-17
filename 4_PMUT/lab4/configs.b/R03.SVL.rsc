/system identity set name=R03.SVL
/user set [find name=admin] password=cfrekby

# IP
/interface bridge add name=lo0
/ip address
add address=10.0.0.30/32 interface=lo0
add address=10.33.30.2/30 interface=ether2 comment="to R03.LBN"

# OSPF
/routing ospf instance set default router-id=10.0.0.30
/routing ospf network
add network=10.0.0.30/32 area=backbone
add network=10.33.30.0/30 area=backbone

# MPLS
/mpls ldp set enabled=yes transport-address=10.0.0.30 lsr-id=10.0.0.30
/mpls ldp interface add interface=ether2

# iBGP
/routing bgp instance set default as=65000 router-id=10.0.0.30
/routing bgp peer add name=to_RR_LBN remote-address=10.0.0.33 remote-as=65000 \
    update-source=lo0 address-families=vpnv4,l2vpn

# VPLS BGP Setup
/interface bridge add name=br-vpls
/interface bridge port add bridge=br-vpls interface=ether3

/interface vpls bgp-vpls add name=vpls_bgp bridge=br-vpls site-id=30 \
    route-distinguisher=65000:100 export-route-targets=65000:100 import-route-targets=65000:100