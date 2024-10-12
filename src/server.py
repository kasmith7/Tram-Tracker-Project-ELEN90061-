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

# Update tram locations dynamically every 5 seconds based on the POST request by tram
@app.route('/get_info', methods=['POST'])
def update_tram_info():
    data = request.json
    tram_id = data.get("tram_id")
    route = data.get("route")
    current_stop = data.get("current_stop")

    if tram_id and route and current_stop:
        # Update or create tram data
        trams[tram_id] = {
            "tram_id": tram_id,
            "route": route,
            "current_stop": current_stop
        }
        return jsonify({"status": "success", "message": f"Tram {tram_id} updated"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

# Get all tram info at a specific stop
@app.route('/tram_info/<stop>', methods=['POST'])
def get_trams_by_stop(stop):
    relevant_trams = []
    for tram_id, tram in trams.items():
        route = tram["route"]
        route_stops_list = route_stops[route]
        if stop in route_stops_list:
            stop_distance = calculate_stop_distance(route_stops_list, tram["current_stop"], stop)
            relevant_trams.append({
                "tram_id": tram["tram_id"],
                "route": tram["route"],
                "current_stop": tram["current_stop"],
                "distance_to_stop": stop_distance,
            })

    return jsonify(relevant_trams)

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
    app.run(debug=True)