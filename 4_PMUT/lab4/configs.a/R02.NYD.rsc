/system identity set name=R02.NYD
/user set [find name=admin] password=cfrekby

# IP
/interface bridge add name=lo0
/ip address
add address=10.0.0.20/32 interface=lo0
add address=10.22.20.2/30 interface=ether2 comment="to R02.LND"

# OSPF
/routing ospf instance set default router-id=10.0.0.20
/routing ospf network
add network=10.0.0.20/32 area=backbone
add network=10.22.20.0/30 area=backbone

# MPLS
/mpls ldp set enabled=yes transport-address=10.0.0.20 lsr-id=10.0.0.20
/mpls ldp interface add interface=ether2

# iBGP
/routing bgp instance set default as=65000 router-id=10.0.0.20
/routing bgp peer add name=to_RR_LND remote-address=10.0.0.22 remote-as=65000 update-source=lo0 address-families=vpnv4

# VRF
/ip route vrf add routing-mark=VRF_DEVOPS interfaces=ether3 route-distinguisher=65000:1 import-route-targets=65000:1 export-route-targets=65000:1
/ip address add address=192.168.20.1/24 interface=ether3

# BGP VRF
/routing bgp instance vrf add routing-mark=VRF_DEVOPS instance=default redistribute-connected=yes