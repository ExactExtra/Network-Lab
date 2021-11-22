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
![alt text](https://github.com/fawnorange/Network-Lab/blob/main/Network%20Lab%20v1.png)

## Solution Overview  
CPS-1 and CPS-2 will be using LACP between each other since only 4500 and 6500 have VSS  
eBGP with AS4896 towards FISH-2 and FROG-2 to simulate 2 different MPLS  

![alt text](https://github.com/fawnorange/Network-Lab/blob/main/HQ%20compartment.png)  
