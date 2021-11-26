# Network-Lab

### Objectives  
- [x] Ping successfully from ubuntu docker to IOU1 and IOU2  
- [ ] Add more hosts eventually  
- [ ] Input firewall rules and test firewall  
- [ ] Create redundancy between devices under AS5000  
- [ ] Add more services above AS4896 e.g. netbox, automation, syslog etc.

### GNS3 Lab setup

Devices:  
6x Cisco IOSv as WAN routers  
2x Cisco IOSvL2 as L3 switches  
2x Cisco IOU L2 as L2 switches  
1x Cisco IOU L3 as "Internet"  
1x PA-VM as firewall because need license to HA. gg 

## Network Diagram  
![alt text](https://github.com/ExactExtra/Network-Lab/blob/main/Diagrams/Network%20Lab%20v1.png)


## Solution Overview  
CPS-1 and CPS-2 will be using LACP between each other since only 4500 and 6500 have VSS  
OSPF will be used as iGP for internal routing for different service emulation    
eBGP with AS4896 towards FISH-2 and FROG-2 to simulate 2 different MPLS  

![alt text](https://github.com/ExactExtra/Network-Lab/blob/main/Diagrams/HQ%20compartment.png)  

FISH-1 and FISH-2 are using iBGP between each other, AS100, simulating MPLS1  
Likewise, FROG-1 and FROG-2 are using iBGP between each other, AS200 simulating MPLS2  
"Internet" will be a standalone AS9000 simulating the internet  
They will all peer with each other using eBGP and all should be pingable to each other  

![alt text](https://github.com/ExactExtra/Network-Lab/blob/main/Diagrams/ISP%20compartment.png)  

T-WAN-1 will be peering with FISH-1 and T-WAN-2 will be peering with FROG-1 for redundancy  
The link between T-WAN-1 and T-WAN-2 will most likely be a L2 vlan for connectivity, remote mgt or otherwise  

![alt text](https://github.com/ExactExtra/Network-Lab/blob/main/Diagrams/Remote%20site%20compartment.png)
