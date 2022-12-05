from Packet import *
from Router import *
from Endpoint import *


src_endpoint = endpoint('192.168.1.1')
#print(src_endpoint.ip_address)

dst_endpoint = endpoint('192.168.1.2')
#print(dst_endpoint.ip_address)

print(f'We are going to send packet from {src_endpoint.ip_address} to {dst_endpoint.ip_address}')

quantity = input('How much packet do you want to generate ? ')
#print(quantity)

period = input('Do you want to simulate for the day (1) or the night (2) ? ')
#print(period)

QoS = input('Do you want to simulate QoS: Yes or No ? ')
#print(QoS.lower())

#Packet generation
src_endpoint.buffer = genPacket(int(quantity), src_endpoint.ip_address, dst_endpoint.ip_address, int(period))
sizeofpacket_list = len(src_endpoint.buffer)

for iter in range(sizeofpacket_list):
        print(f'{src_endpoint.buffer[iter].name} : {src_endpoint.buffer[iter].type} | src address: {src_endpoint.buffer[iter].src_a} | dst address: {src_endpoint.buffer[iter].src_dst} | priority: {src_endpoint.buffer[iter].priority} | data length: {src_endpoint.buffer[iter].taille} octets')

if QoS.lower() == 'no':
    router_type = 1 #1 is for a router which has only 1 queue
    new_router = router(router_type)
    #print(new_router.type)
 
    router.no_QoS_forwarding(src_endpoint, dst_endpoint)

    sizeOfDestBuffer = len(dst_endpoint.buffer)
    #print(sizeOfDestBuffer)

    print('\nThe order of arrival of the previous packet in the second equipment is :')
    for iter in range(sizeOfDestBuffer):
        print(f'{dst_endpoint.buffer[iter].name} : {dst_endpoint.buffer[iter].type} | src address: {dst_endpoint.buffer[iter].src_a} | dst address: {dst_endpoint.buffer[iter].src_dst} | priority: {dst_endpoint.buffer[iter].priority} | data length: {dst_endpoint.buffer[iter].taille} octets')

else:
    router_type = 2 #2 is for a router which has QoS implemented
    new_router = router(router_type)

    if len(src_endpoint.buffer) != 0:
        for iter in range(len(src_endpoint.buffer)):
            router.QoS_queue_populating(src_endpoint.buffer[0], int(period), new_router)
            src_endpoint.buffer.pop(0)

    print('\nPacket in the first priority queue')
    if len(new_router.first_priority) != 0:
        for iter in range(len(new_router.first_priority)):
            print(f'{new_router.first_priority[iter].name} : {new_router.first_priority[iter].type} | src address: {new_router.first_priority[iter].src_a} | dst address: {new_router.first_priority[iter].src_dst} | priority: {new_router.first_priority[iter].priority} | data length: {new_router.first_priority[iter].taille} octets')
    else:
        print('There is no packet')

    print('\nPacket in the second priority queue')
    if len(new_router.second_priority) != 0:
        for iter in range(len(new_router.second_priority)):
            print(f'{new_router.second_priority[iter].name} : {new_router.second_priority[iter].type} | src address: {new_router.second_priority[iter].src_a} | dst address: {new_router.second_priority[iter].src_dst} | priority: {new_router.second_priority[iter].priority} | data length: {new_router.second_priority[iter].taille} octets')
    else:
        print('There is no packet')

    print('\nPacket in the third priority queue')
    if len(new_router.third_priority) != 0:
        for iter in range(len(new_router.third_priority)):
            print(f'{new_router.third_priority[iter].name} : {new_router.third_priority[iter].type} | src address: {new_router.third_priority[iter].src_a} | dst address: {new_router.third_priority[iter].src_dst} | priority: {new_router.third_priority[iter].priority} | data length: {new_router.third_priority[iter].taille} octets')
    else:
        print('There is no packet')

    print('\nPacket in the fourth priority queue')
    if len(new_router.fourth_priority) != 0:
        for iter in range(len(new_router.fourth_priority)):
            print(f'{new_router.fourth_priority[iter].name} : {new_router.fourth_priority[iter].type} | src address: {new_router.fourth_priority[iter].src_a} | dst address: {new_router.fourth_priority[iter].src_dst} | priority: {new_router.fourth_priority[iter].priority} | data length: {new_router.fourth_priority[iter].taille} octets')
    else:
        print('There is no packet')

'''
for iter in range(sizeofpacket_list):
        print(f'{src_endpoint.buffer[iter].name} : {src_endpoint.buffer[iter].type} | src address: {src_endpoint.buffer[iter].src_a} | dst address: {src_endpoint.buffer[iter].src_dst} | priority: {src_endpoint.buffer[iter].priority} | data length: {src_endpoint.buffer[iter].taille} octets')
'''