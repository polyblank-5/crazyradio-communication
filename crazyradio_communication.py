# chatgpt test
import time
from cflib.crazyradio import Crazyradio

def setup_crazyradio(cr, channel, data_rate):
    cr.set_channel(channel)
    cr.set_data_rate(data_rate)
    cr.set_address((0xE7, 0xE7, 0xE7, 0xE7, 0xE7))
    cr.set_ack_enable(True)
    return cr

def send_message(cr, message):
    cr.send_packet(list(message.encode()))

def receive_message(cr):
    packet = cr.receive_packet()
    if packet:
        return bytes(packet[0]).decode()
    return None

# Setup two Crazyradios (crazyradio1 and crazyradio2) on the same channel and data rate
channel = 42
data_rate = Crazyradio.DR_2MPS

crazyradio1 = setup_crazyradio(Crazyradio(), channel, data_rate)
crazyradio2 = setup_crazyradio(Crazyradio(), channel, data_rate)

# Example sending and receiving messages
send_message(crazyradio1, "Hello from Crazyradio 1")
time.sleep(1)
message = receive_message(crazyradio2)
if message:
    print("Crazyradio 2 received:", message)

