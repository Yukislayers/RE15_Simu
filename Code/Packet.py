import random

#Simulation of a QoS packet with wifi 802.11e

class packet:
    name = ''
    src_a = ''
    src_dst = ''
    type = ''
    priority = 0
    taille = 0

def genPacket(n, src_a, src_dest, period):
    packets_list = []
    for i in range(n):
        prio = random.randrange(0, 4)
        data = random.randrange(0, 255)
        new_packet = packet()
        new_packet.name = 'packet' + str(i)
        new_packet.src_a = src_a
        new_packet.src_dst = src_dest
        new_packet.priority = prio
        new_packet.taille = data
        if (period == 1):
            match prio:
                case 0:
                    new_packet.type = 'Sensor'
                case 1:
                    new_packet.type = 'VoIP'
                case 2:
                    new_packet.type = 'Employee'
                case 3:
                    new_packet.type = 'Cameras'
        elif period == 2:
            match prio:
                case 0:
                    new_packet.type = 'Cameras'
                case 1:
                    new_packet.type = 'Sensor'
                case 2:
                    new_packet.type = 'VoIP'
                case 3:
                    new_packet.type = 'Employee'
        packets_list.append(new_packet)
    else:
        print(f'{n} packets have been generated')
    return packets_list

'''
list = genPacket(5, '192.168.1.1', '192.168.1.2')

sizeoflist = len(list)
#print(sizeoflist)

for iter in range(sizeoflist):
    print(f'{list[iter].name} has for src address {list[iter].src_a} and dst address {list[iter].src_dst} and prio {list[iter].priority} and data length {list[iter].taille} octets')
'''