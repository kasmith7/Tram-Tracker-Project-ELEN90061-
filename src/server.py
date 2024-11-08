from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

# Tram data: A dictionary to store tram information by tram_id
trams = {}

# Routes and stops
route_stops = {
    1: ["a", "d", "f"],  # Route 1 stops
    6: ["a", "b", "c", "d", "e"],  # Route 6 stops
}

# Fare rates for each stop
STOP_FARE_RATES = {
    1: {"a": 3.00, "d": 4.00, "f": 5.00},  # Fares for stops on route a
    6: {"a": 3.50, "b": 2.50, "c": 4.50, "d": 4.00, "e": 5.50},  # Fares for stops on route d
}

# Points of Interest for each route
ROUTE_POIS = {
    1: ["Federation Square", "Melbourne Museum", "Carlton Gardens"],
    6: ["Federation Square", "Queen Victoria Market", "Lygon Street", "Melbourne Central"]
}

# Update tram locations dynamically every 5 seconds based on the POST request by tram
@app.route('/get_info', methods=['POST'])
def update_tram_info():
    data = request.json
    tram_id = data.get("tram_id")
    route = data.get("route")
    current_stop = data.get("current_stop")
    sequence = data.get("sequence")  # Sequence number of the packet

    if tram_id and route and current_stop:
        # Update or create tram data
        trams[tram_id] = {
            "tram_id": tram_id,
            "route": route,
            "current_stop": current_stop,
            "sequence": sequence
        }
        print(f"Received update from {tram_id} at stop {current_stop} with sequence {sequence}. Sending ACK.")
        return jsonify({"status": "success", "ack": sequence}), 200  # Send ACK with sequence number
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400


# Get all tram info at a specific stop
@app.route('/tram_info/<stop>', methods=['GET'])
def get_trams_by_stop(stop):
    relevant_trams = []
    for tram_id, tram in trams.items():
        route = tram["route"]
        route_stops_list = route_stops[route]
        if stop in route_stops_list:
            stop_distance = calculate_stop_distance(route_stops_list, tram["current_stop"], stop)
            fare = calculate_fare(route, stop)
            points_of_interest = ROUTE_POIS.get(route, [])
            relevant_trams.append({
                "tram_id": tram["tram_id"],
                "route": tram["route"],
                "current_stop": tram["current_stop"],
                "distance_to_stop": stop_distance,
                "points_of_interest": points_of_interest,
                "fare": fare
            })

    return jsonify(relevant_trams)

# Function to get the fare based on the stop within the route
def calculate_fare(route, stop):
    return STOP_FARE_RATES.get(route, {}).get(stop, 3.00)  # Default fare if stop not found

# Function to calculate the distance (in number of stops) between the tram and the requested stop
def calculate_stop_distance(route_stops, current_stop, target_stop):
    current_index = route_stops.index(current_stop)
    target_index = route_stops.index(target_stop)
    distance = (target_index - current_index) % len(route_stops)
    return distance


# Endpoint to get all the tram data (for debugging or management)
@app.route('/all_trams', methods=['GET'])
def get_all_trams():
    return jsonify(trams), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
