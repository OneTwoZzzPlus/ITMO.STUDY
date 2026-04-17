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
/routing bgp peer add name=to_RR_LBN remote-address=10.0.0.33 remote-as=65000 update-source=lo0 address-families=vpnv4

# VRF
/ip route vrf add routing-mark=VRF_DEVOPS interfaces=ether3 route-distinguisher=65000:1 import-route-targets=65000:1 export-route-targets=65000:1
/ip address add address=192.168.30.1/24 interface=ether3

# BGP VRF
/routing bgp instance vrf add routing-mark=VRF_DEVOPS instance=default redistribute-connected=yes