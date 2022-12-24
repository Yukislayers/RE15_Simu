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

    str_entry_rate = input(f'\nWhat entry rate do you want (between 1 and {quantity}) ? ')
    str_output_rate = input(f'What output rate do you want (between 1 and {quantity}) ? ')

    entry_rate = int(str_entry_rate)
    output_rate = int(str_output_rate)

    router_type = 2 #2 is for a router which has QoS implemented
    new_router = router(router_type)

    while (len(src_endpoint.buffer)) != 0 and (len(src_endpoint.buffer)) > entry_rate:

        print('\n--------------------------------------------------------------------')

        for iter in range(entry_rate):
            router.QoS_queue_populating(src_endpoint.buffer[0], int(period), new_router)
            src_endpoint.buffer.pop(0)
        
        router.show_queue(new_router)

        for iter2 in range(output_rate):
            router.QoS_forwarding(dst_endpoint, new_router)
        
        print('\nAt this point, the destination buffer is composed of')
        dst_endpoint.show_buffer(dst_endpoint)

    else:

        print('\n--------------------------------------------------------------------')
        for iter in range(len(src_endpoint.buffer)):
            router.QoS_queue_populating(src_endpoint.buffer[0], int(period), new_router)
            src_endpoint.buffer.pop(0)

        router.show_queue(new_router)
        for iter2 in range(output_rate):
            router.QoS_forwarding(dst_endpoint, new_router)

        print('\nAt this point, the destination buffer is composed of')
        dst_endpoint.show_buffer(dst_endpoint)
        
    while len(new_router.first_priority) != 0 or len(new_router.second_priority) != 0 or len(new_router.third_priority) != 0 or len(new_router.fourth_priority) != 0:
        router.QoS_forwarding(dst_endpoint, new_router)


    sizeOfDestBuffer = len(dst_endpoint.buffer)
    #print(sizeOfDestBuffer)

    print('\n--------------------------------------------------------------------')
    print('The order of arrival of the previous packet in the second equipment is :')
    dst_endpoint.show_buffer(dst_endpoint)

    print('\nEnd of the simulation !')