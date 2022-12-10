#It will simulate a router in which we will setup QoS or not
from Packet import *
from Router import *
from Endpoint import *

class router():
    def __init__(self, type):
        self.type = type

    first_priority = []
    second_priority = []
    third_priority = []
    fourth_priority = []

    size_of_first_priority = 100
    size_of_second_priority = 100
    size_of_third_priority = 100
    size_of_fourth_priority = 100

    def no_QoS_forwarding(src_endpoint, dst_endpoint):
        #print('I am in No QoS forwarding function')
        #print(src_endpoint.buffer[0].name)
        sizeofpackets = len(src_endpoint.buffer)
        #print(sizeofpackets)
        for i in range(sizeofpackets):
            out_packet = src_endpoint.buffer[0]
            #print(out_packet.name)
            src_endpoint.buffer.pop(0)
            dst_endpoint.buffer.append(out_packet)

    def QoS_queue_populating(packet, period, router, src):
            if period == 1:
                match packet.type:
                    case 'Sensor':
                        if len(router.first_priority) <= (router.size_of_first_priority - 1):
                            router.first_priority.append(packet)
                        else:
                            print(f'{packet.name} of type : {packet.type} have been dropped')
                            src.resend_buffer.append(packet)
                    case 'VoIP':
                        if len(router.second_priority) <= (router.size_of_second_priority - 1):
                            router.second_priority.append(packet)
                        else:
                            print(f'{packet.name} of type : {packet.type} have been dropped')
                            src.resend_buffer.append(packet)
                    case 'Employee':
                        if len(router.third_priority) <= (router.size_of_third_priority - 1):
                            router.third_priority.append(packet)
                        else:
                            print(f'{packet.name} of type : {packet.type} have been dropped')
                            src.resend_buffer.append(packet)
                    case 'Cameras':
                        if len(router.fourth_priority) <= (router.size_of_fourth_priority - 1):
                            router.fourth_priority.append(packet)
                        else:
                            print(f'{packet.name} of type : {packet.type} have been dropped')
                            src.resend_buffer.append(packet)
            elif period == 2:
                match packet.type:
                    case 'Cameras':
                        if len(router.first_priority) <= (router.size_of_first_priority - 1):
                            router.first_priority.append(packet)
                        else:
                            print(f'{packet.name} of type : {packet.type} have been dropped')
                            src.resend_buffer.append(packet)
                    case 'Sensor':
                        if len(router.second_priority) <= (router.size_of_second_priority - 1):
                            router.second_priority.append(packet)
                        else:
                            print(f'{packet.name} of type : {packet.type} have been dropped')
                            src.resend_buffer.append(packet)
                    case 'VoIP':
                        if len(router.third_priority) <= (router.size_of_third_priority - 1):
                            router.third_priority.append(packet)
                        else:
                            print(f'{packet.name} of type : {packet.type} have been dropped')
                            src.resend_buffer.append(packet)
                    case 'Employee':
                        if len(router.fourth_priority) <= (router.size_of_fourth_priority - 1):
                            router.fourth_priority.append(packet)
                        else:
                            print(f'{packet.name} of type : {packet.type} have been dropped')
                            src.resend_buffer.append(packet)

    def QoS_forwarding(dst_endpoint, router):
        if len(router.first_priority) != 0:
            dst_endpoint.buffer.append(router.first_priority[0])
            router.first_priority.pop(0)
        elif len(router.second_priority) != 0:
            dst_endpoint.buffer.append(router.second_priority[0])
            router.second_priority.pop(0)
        elif len(router.third_priority) != 0:
            dst_endpoint.buffer.append(router.third_priority[0])
            router.third_priority.pop(0)
        elif len(router.fourth_priority) != 0:
            dst_endpoint.buffer.append(router.fourth_priority[0])
            router.fourth_priority.pop(0)

    def show_queue(new_router):
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
        
    def check_congestion(router):
        if len(router.first_priority) == router.size_of_first_priority and len(router.second_priority) == router.size_of_second_priority and len(router.third_priority) == router.size_of_third_priority and len(router.fourth_priority) == router.size_of_fourth_priority:
            print('\n--------------------------------------------------------------------')
            print('Start of congestion mecanism')
            print('--------------------------------------------------------------------')
            return True
        else:
            return False