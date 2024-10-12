import requests
import time

# Tram data - tram4 (runs on route 6)
tram_id = "tram4"
route = 6
current_stop_index = 2  # Starting at stop 'c' on route 6

# Route stop lists
route_stops = {
    1: ["a", "d", "f"],  # Route 1 stops
    6: ["a", "b", "c", "d", "e"],  # Route 6 stops
}

current_route_stops = route_stops[route]

def update_tram_location():
    global current_stop_index
    while True:
        current_stop = current_route_stops[current_stop_index]
        response = requests.post('http://127.0.0.1:5000/get_info', json={
            "tram_id": tram_id,
            "route": route,
            "current_stop": current_stop
        })
        print(f"Tram {tram_id} at stop {current_stop}, response: {response.status_code}")
        current_stop_index = (current_stop_index + 1) % len(current_route_stops)
        time.sleep(5)

update_tram_location()