import requests

# Function to get tram info by stop
def get_tram_info_by_stop(stop):
    response = requests.post(f'http://127.0.0.1:5000/tram_info/{stop}')
    if response.status_code == 200:
        tram_info = response.json()
        print(f"Trams stopping at {stop}:")
        for tram in tram_info:
            print(f"Tram ID: {tram['tram_id']}, Route: {tram['route']}, Distance: {tram['distance_to_stop']} stops away")
    else:
        print(f"Failed to retrieve tram info: {response.status_code}")

# Example of requesting trams stopping at stop "a"
get_tram_info_by_stop("a")
