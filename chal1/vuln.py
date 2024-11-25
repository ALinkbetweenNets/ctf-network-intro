import socket
import random
random.seed()

UDP_IP = input("Which IP should I send the flag to?").strip()

UDP_PORT = random.randint(3000, 5000)

print(f"Once you tell me you are ready I will send the flag to you on UDP port {UDP_PORT}", flush=True)

print("Send me something to indicate, that you are ready!")

input()

print("You are ready? Transmitting flag now!")

MESSAGE = b"FLAG_PLACEHOLDER"

# print("UDP target IP: %s" % UDP_IP)
# print("UDP target port: %s" % UDP_PORT)
# print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

print("I hope you got it!")
