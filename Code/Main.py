import Packet
import Routeur
from Endpoint import *


src_endpoint = endpoint('192.168.1.1')
#print(src_endpoint.ip_address)

dst_endpoint = endpoint('192.168.1.2')
#print(dst_endpoint.ip_address)

print(f'We are going to send packet from {src_endpoint.ip_address} to {dst_endpoint.ip_address}')

quantity = input('How much packet do you want to generate ? ')
#print(quantity)

packet_list = Packet.genPacket(int(quantity), src_endpoint.ip_address, dst_endpoint.ip_address)
sizeofpacket_list = len(packet_list)
print(sizeofpacket_list)

for iter in range(sizeofpacket_list):
    print(f'{packet_list[iter].name} has for src address {packet_list[iter].src_a} and dst address {packet_list[iter].src_dst} and prio {packet_list[iter].priority} and data length {packet_list[iter].taille} octets')