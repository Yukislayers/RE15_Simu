from Packet import *
from Router import *
from Endpoint import *
import time


src_endpoint = endpoint('192.168.1.1')
#print(src_endpoint.ip_address)

dst_endpoint = endpoint('192.168.1.2')
#print(dst_endpoint.ip_address)

print(f'We are going to send packet from {src_endpoint.ip_address} to {dst_endpoint.ip_address}')

quantity = input('How much packet do you want to generate ? ')
#print(quantity)

period = input('Do you want to simulate for the day (1) or the night (2) ? ')
#print(period)

QoS_str = input('Do you want to simulate QoS: 1 (Yes) or 2 (No) ? ')
Qos = int(QoS_str)
#print(QoS.lower())

#Packet generation
src_endpoint.buffer = genPacket(int(quantity), src_endpoint.ip_address, dst_endpoint.ip_address, int(period))
sizeofpacket_list = len(src_endpoint.buffer)

for iter in range(sizeofpacket_list):
        print(f'{src_endpoint.buffer[iter].name} : {src_endpoint.buffer[iter].type} | src address: {src_endpoint.buffer[iter].src_a} | dst address: {src_endpoint.buffer[iter].src_dst} | priority: {src_endpoint.buffer[iter].priority} | data length: {src_endpoint.buffer[iter].taille} octets')

if Qos == 2:
    router_type = 1 #1 is for a router which has only 1 queue
    new_router = router(router_type)
    #print(new_router.type)
 
    router.no_QoS_forwarding(src_endpoint, dst_endpoint)

    print('\n--------------------------------------------------------------------')
    print('The order of arrival of the previous packet in the second equipment is :')
    dst_endpoint.show_buffer(dst_endpoint)

    print('\nEnd of the simulation !')

else:

    str_entry_rate = input(f'\nWhat entry rate do you want (between 1 and {quantity}) ? ')
    str_output_rate = input(f'What output rate do you want (between 1 and {quantity}) ? ')

    entry_rate = int(str_entry_rate)
    output_rate = int(str_output_rate)

    router_type = 2 #2 is for a router which has QoS implemented
    new_router = router(router_type)

    queue_size_str = input(f'Do you want to put a max lenght for the different priority queue : 1 (Yes) or 2 (No) ? ')
    queue_size = int(queue_size_str)

    if queue_size == 2:

        while (len(src_endpoint.buffer)) != 0 and (len(src_endpoint.buffer)) > entry_rate:

            print('\n--------------------------------------------------------------------')

            for iter in range(entry_rate):
                router.QoS_queue_populating(src_endpoint.buffer[0], int(period), new_router, src_endpoint)
                src_endpoint.buffer.pop(0)
            
            router.show_queue(new_router)

            for iter2 in range(output_rate):
                router.QoS_forwarding(dst_endpoint, new_router)
            
            print('\nAt this point, the destination buffer is composed of')
            dst_endpoint.show_buffer(dst_endpoint)

        else:

            print('\n--------------------------------------------------------------------')
            for iter in range(len(src_endpoint.buffer)):
                router.QoS_queue_populating(src_endpoint.buffer[0], int(period), new_router, src_endpoint)
                src_endpoint.buffer.pop(0)

            router.show_queue(new_router)
            for iter2 in range(output_rate):
                router.QoS_forwarding(dst_endpoint, new_router)

            print('\nAt this point, the destination buffer is composed of')
            dst_endpoint.show_buffer(dst_endpoint)
            
        while len(new_router.first_priority) != 0 or len(new_router.second_priority) != 0 or len(new_router.third_priority) != 0 or len(new_router.fourth_priority) != 0:
            router.QoS_forwarding(dst_endpoint, new_router)

        print('\n--------------------------------------------------------------------')
        print('The order of arrival of the previous packet in the second equipment is :')
        dst_endpoint.show_buffer(dst_endpoint)

        print('\nEnd of the simulation !')

    else:

        prio_queue_str = input('Do you want to put the same size for all the queue : 1 (Yes) or 2 (No) ? ')
        prio_queue = int(prio_queue_str)

        if prio_queue == 1:
            size_of_prio_queue_str = input('What length do you want for all the queue ? ')
            size_of_prio_queue = int(size_of_prio_queue_str)
            new_router.size_of_first_priority = size_of_prio_queue
            new_router.size_of_second_priority = size_of_prio_queue
            new_router.size_of_third_priority = size_of_prio_queue
            new_router.size_of_fourth_priority = size_of_prio_queue

            while (len(src_endpoint.buffer)) != 0 and (len(src_endpoint.buffer)) > entry_rate:

                print('\n--------------------------------------------------------------------')

                for iter in range(entry_rate):
                    router.QoS_queue_populating(src_endpoint.buffer[0], int(period), new_router, src_endpoint)
                    src_endpoint.buffer.pop(0)
                
                router.show_queue(new_router)
                
                if router.check_congestion(new_router):
                    while len(new_router.first_priority) != 0 or len(new_router.second_priority) != 0 or len(new_router.third_priority) != 0 or len(new_router.fourth_priority) != 0:
                        router.QoS_forwarding(dst_endpoint, new_router)
                        time.sleep(2)
                else:
                    for iter2 in range(output_rate):
                        router.QoS_forwarding(dst_endpoint, new_router)
                
                print('\nAt this point, the destination buffer is composed of')
                dst_endpoint.show_buffer(dst_endpoint)

            else:

                print('\n--------------------------------------------------------------------')
                for iter in range(len(src_endpoint.buffer)):
                    router.QoS_queue_populating(src_endpoint.buffer[0], int(period), new_router, src_endpoint)
                    src_endpoint.buffer.pop(0)

                router.show_queue(new_router)
                if router.check_congestion(new_router):
                    while len(new_router.first_priority) != 0 or len(new_router.second_priority) != 0 or len(new_router.third_priority) != 0 or len(new_router.fourth_priority) != 0:
                        router.QoS_forwarding(dst_endpoint, new_router)
                        time.sleep(2)
                else:
                    for iter2 in range(output_rate):
                        router.QoS_forwarding(dst_endpoint, new_router)

                print('\nAt this point, the destination buffer is composed of')
                dst_endpoint.show_buffer(dst_endpoint)


            print('\nWe resend the packets that have been dropped')

            #resend packet that have been dropped
            while len(src_endpoint.resend_buffer) != 0:
                if len(src_endpoint.resend_buffer) <= entry_rate:
                    delta = len(src_endpoint.resend_buffer)
                else:
                    delta = entry_rate

                for iter in range(delta):
                    router.QoS_queue_populating(src_endpoint.resend_buffer[0], int(period), new_router, src_endpoint)
                    src_endpoint.resend_buffer.pop(0)

                for iter2 in range(output_rate):
                    router.QoS_forwarding(dst_endpoint, new_router)


            while len(new_router.first_priority) != 0 or len(new_router.second_priority) != 0 or len(new_router.third_priority) != 0 or len(new_router.fourth_priority) != 0:
                router.QoS_forwarding(dst_endpoint, new_router)

            print('\n--------------------------------------------------------------------')
            print('The order of arrival of the previous packet in the second equipment is :')
            dst_endpoint.show_buffer(dst_endpoint)
                
            print('\nEnd of the simulation !')

        else:
            size_of_first_queue_str = input('What length do you want for the first queue ? ')
            size_of_first_queue = int(size_of_first_queue_str)
            new_router.size_of_first_priority = size_of_first_queue   

            size_of_second_queue_str = input('What length do you want for the second queue ? ')
            size_of_second_queue = int(size_of_second_queue_str)
            new_router.size_of_second_priority = size_of_second_queue 

            size_of_third_queue_str = input('What length do you want for the third queue ? ')
            size_of_third_queue = int(size_of_third_queue_str)
            new_router.size_of_third_priority = size_of_third_queue 

            size_of_fourth_queue_str = input('What length do you want for the fourth queue ? ')
            size_of_fourth_queue = int(size_of_fourth_queue_str)
            new_router.size_of_fourth_priority = size_of_fourth_queue 

            #print(new_router.size_of_first_priority) 
            #print(new_router.size_of_second_priority) 
            #print(new_router.size_of_third_priority) 
            #print(new_router.size_of_fourth_priority)

            while (len(src_endpoint.buffer)) != 0 and (len(src_endpoint.buffer)) > entry_rate:

                print('\n--------------------------------------------------------------------')

                for iter in range(entry_rate):
                    router.QoS_queue_populating(src_endpoint.buffer[0], int(period), new_router, src_endpoint)
                    src_endpoint.buffer.pop(0)
            
                router.show_queue(new_router)

                if router.check_congestion(new_router):
                    while len(new_router.first_priority) != 0 or len(new_router.second_priority) != 0 or len(new_router.third_priority) != 0 or len(new_router.fourth_priority) != 0:
                        router.QoS_forwarding(dst_endpoint, new_router)
                        time.sleep(2)
                else:
                    for iter2 in range(output_rate):
                        router.QoS_forwarding(dst_endpoint, new_router)
            
                print('\nAt this point, the destination buffer is composed of')
                dst_endpoint.show_buffer(dst_endpoint)

            else:

                print('\n--------------------------------------------------------------------')
                for iter in range(len(src_endpoint.buffer)):
                    router.QoS_queue_populating(src_endpoint.buffer[0], int(period), new_router, src_endpoint)
                    src_endpoint.buffer.pop(0)

                router.show_queue(new_router)

                if router.check_congestion(new_router):
                    while len(new_router.first_priority) != 0 or len(new_router.second_priority) != 0 or len(new_router.third_priority) != 0 or len(new_router.fourth_priority) != 0:
                        router.QoS_forwarding(dst_endpoint, new_router)
                        time.sleep(2)
                else:
                    for iter2 in range(output_rate):
                        router.QoS_forwarding(dst_endpoint, new_router)

                print('\nAt this point, the destination buffer is composed of')
                dst_endpoint.show_buffer(dst_endpoint)


            print('\nWe resend the packets that have been dropped')

            #resend packet that have been dropped
            while len(src_endpoint.resend_buffer) != 0:
                if len(src_endpoint.resend_buffer) <= entry_rate:
                    delta = len(src_endpoint.resend_buffer)
                else:
                    delta = entry_rate

                for iter in range(delta):
                    router.QoS_queue_populating(src_endpoint.resend_buffer[0], int(period), new_router, src_endpoint)
                    src_endpoint.resend_buffer.pop(0)

                for iter2 in range(output_rate):
                    router.QoS_forwarding(dst_endpoint, new_router)


            while len(new_router.first_priority) != 0 or len(new_router.second_priority) != 0 or len(new_router.third_priority) != 0 or len(new_router.fourth_priority) != 0:
                router.QoS_forwarding(dst_endpoint, new_router)

            print('\n--------------------------------------------------------------------')
            print('The order of arrival of the previous packet in the second equipment is :')
            dst_endpoint.show_buffer(dst_endpoint)
                
            print('\nEnd of the simulation !')
            #test