#! /usr/bin/env python
#The module argparse is used to input the values in the terminal by the user using set of steps.
#The module scapy is used to send and receive packets and it works both in python2 and 3.
#Officially coded by Dot Intro
import argparse
import scapy.all as scapy
def scapypart(ip):
    arp_req=scapy.ARP(pdst=ip)
    bc=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    bc_arp_req=bc/arp_req
    result=scapy.srp(bc_arp_req,timeout=3,verbose=0)[0]
    print("The result is")
                               
    print("IP ADDRESS \t\t\t MAC ADDRESS \n-------------------------------------")
    for i in result:
      print(i[1].psrc+"\t\t\t"+i[1].hwsrc)

print("Dnetcapturer")
def parsy():
  parser=argparse.ArgumentParser()
  parser.add_argument("-ip","--ipscan",dest="ip",help="Target IP range or IP") 
  opts=parser.parse_args()
  return opts
opts=parsy()
ipscapy=scapypart(opts.ip)



