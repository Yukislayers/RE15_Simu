import random

#Simulation of a QoS packet with wifi 802.11e

class packet:
    name = ''
    src_a = ''
    src_dst = ''
    priority = 0
    taille = 0

def genPacket(n, src_a, src_dest):
    packets_list = []
    for i in range(n):
        prio = random.randrange(0, 4)
        data = random.randrange(0, 255)
        test = packet()
        test.name = 'packet' + str(i)
        test.src_a = src_a
        test.src_dst = src_dest
        test.priority = prio
        test.taille = data
        #print(f'{test.name} has for src address {test.src_a} and dst address {test.src_dst} and prio {test.priority} and data length {test.taille} octets')
        packets_list.append(test)
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