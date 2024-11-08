import requests
import time
import random

# Tram data - tram4 (runs on route 6)
tram_id = "tram4"
route = 6
current_stop_index = 2  # Starting at stop 'c' on route 6
sequence_number = 0  # Initial sequence number for packets
timeout = 5  # Timeout in seconds for ACK
max_retries = 3  # Maximum number of retransmissions

# Route stop lists
route_stops = {
    1: ["a", "d", "f"],  # Route 1 stops
    6: ["a", "b", "c", "d", "e"],  # Route 6 stops
}

current_route_stops = route_stops[route]

def send_packet(tram_id, route, current_stop, sequence):
    """Send a packet with a sequence number and wait for ACK."""
    data = {
        "tram_id": tram_id,
        "route": route,
        "current_stop": current_stop,
        "sequence": sequence
    }

    for attempt in range(max_retries):
        try:
            # Simulate packet loss by skipping the POST request randomly
            if random.random() < 0.2:  # 20% packet loss simulation
                print(f"Simulated packet loss: Tram {tram_id} failed to send update for stop {current_stop}")
                continue

            response = requests.post('http://127.0.0.1:5000/get_info', json=data, timeout=timeout)
            if response.status_code == 200:
                ack = response.json().get("ack")
                if ack == sequence:
                    print(f"ACK received for sequence {sequence}. Packet delivered successfully.")
                    return True
            print(f"No ACK received for sequence {sequence}. Retrying...")
        except requests.exceptions.Timeout:
            print(f"Timeout occurred for sequence {sequence}. Retrying...")

        time.sleep(1)  # Wait a bit before retrying

    print(f"Failed to receive ACK for sequence {sequence} after {max_retries} attempts.")
    return False

def update_tram_location():
    global current_stop_index, sequence_number
    while True:
        current_stop = current_route_stops[current_stop_index]
        if send_packet(tram_id, route, current_stop, sequence_number):
            # Only move to the next stop if packet was acknowledged
            current_stop_index = (current_stop_index + 1) % len(current_route_stops)
            sequence_number += 1  # Increment sequence number for the next packet
        time.sleep(5)

update_tram_location()