import socket
import time
import random



base_string = "i understand this is unsafe"


def sendPacket():
    # Configuration
    ip_address = "10.0.0.123"  # Target IP address
    port = 1110               # Target port
    interval = 0.02           # Interval between packets in seconds

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    counter = 0
    try:
        while True:
            # Format the counter as a hexadecimal string, padded with zeros
            counter_hex = format(counter, '04x').upper()
            # The fixed part of the packet as a hexadecimal string
            fixed_data_hex = '010410020e0c060000000000000e000001ffff'
            # Combine counter and fixed data, then convert to bytes
            packet_data = bytes.fromhex(f'{counter_hex}{fixed_data_hex}')
            # Send the packet
            sock.sendto(packet_data, (ip_address, port))
            # Increment the counter, wrapping back to 0 if it exceeds 0xFFFF
            counter = (counter + 1) & 0xFFFF
            # Wait for the specified interval
            time.sleep(interval)
    finally:
        # Close the socket when done
        sock.close()


def randomize_case(s):
    return ''.join(random.choice([char.upper(), char.lower()]) for char in s)


randomized_string = randomize_case(base_string)
print(f"Protocol: DS2024")
print(f"This script is strictly for experiment and COULD CAUSE A RUN AWAY ROBOT. Using this script at an official event could be illegal.")
print(f"")
print(f"Please enter the following phrase exactly as shown to proceed: {randomized_string}")
user_input = input()
if user_input == randomized_string:
    print("Correct input. Proceeding...")
    sendPacket()
else:
    print("Incorrect input. Exiting...")
    quit()