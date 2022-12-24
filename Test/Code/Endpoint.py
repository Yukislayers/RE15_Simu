#Class of the first equipment

class endpoint:
    def __init__(self, ip_address):
        self.ip_address = ip_address
    buffer = []
    resend_buffer = []

    def show_buffer(self, equipment):
        sizeofbuffer = len(equipment.buffer)
        for iter in range(sizeofbuffer):
            print(f'{equipment.buffer[iter].name} : {equipment.buffer[iter].type} | src address: {equipment.buffer[iter].src_a} | dst address: {equipment.buffer[iter].src_dst} | priority: {equipment.buffer[iter].priority} | data length: {equipment.buffer[iter].taille} octets')