#It will simulate a router in which we will setup QoS or not
from Packet import *
from Router import *
from Endpoint import *

class router():
    def __init__(self, type):
        self.type = type

    queue = []

    first_priority = []
    second_priority = []
    third_priority = []
    fourth_priority = []

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

    def QoS_queue_populating(packet, period, router):
            if period == 1:
                match packet.type:
                    case 'Sensor':
                        router.first_priority.append(packet)
                    case 'VoIP':
                        router.second_priority.append(packet)
                    case 'Employee':
                        router.third_priority.append(packet)
                    case 'Cameras':
                        router.fourth_priority.append(packet)
            elif period == 2:
                match out_packet.type:
                    case 'Cameras':
                        router.first_priority.append(packet)
                    case 'Sensor':
                        router.second_priority.append(packet)
                    case 'VoIP':
                        router.third_priority.append(packet)
                    case 'Employee':
                        router.fourth_priority.append(packet)

    def QoS_forwarding(router):
        print('Not implemented')