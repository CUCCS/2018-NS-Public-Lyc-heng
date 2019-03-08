#!/usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "192.168.56.103"
client_port = 8888 
dst_port=80

second_server_response = sr1(IP(dst=dst_ip)/TCP(sport=8888,dport=dst_port,flags="S"),timeout=10)
third_client_seq   = second_server_response.ack;
third_client_ack   = second_server_response.seq+1;
if(str(type(second_server_response))==""):
    print "Closed"
elif(second_server_response.haslayer(TCP)):
    if(second_server_response.getlayer(TCP).flags == 0x12):
        send_rst = sr(IP(dst=dst_ip)/TCP(sport=8888,dport=dst_port,seq=third_client_seq,ack=third_client_ack,flags="AR"),timeout=10)
        print "Open"
elif(second_server_response.getlayer(TCP).flags == 0x14):
    print "Closed"