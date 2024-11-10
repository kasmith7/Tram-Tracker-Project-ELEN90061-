import requests
import sys


# Function to get tram info by stop
# In command line use "import client; client.get_stop('a')" to get the current info for stop 'a'
def get_stop(stop):
    response = requests.get(f'http://127.0.0.1:5000/tram_info/{stop}')

    # response = requests.post(f'http://192.168.1.137:5000/tram_info/{stop}')
    ## ^this should be updated if using remote address
    if response.status_code == 200:
        tram_info = response.json()
        print(f"Trams stopping at {stop}:")
        for tram in tram_info:
            print(f"Tram ID: {tram['tram_id']}, Route: {tram['route']}, "
                  f"Fare: ${tram['fare']}")
            if tram.get("points_of_interest"):
                print("Points of Interest along the route:")
                for poi in tram["points_of_interest"]:
                    print(f" - {poi}")
    else:
        print(f"Failed to retrieve tram info: {response.status_code}")


# Example of requesting trams stopping at stop "a"
# get_stop("a")
if __name__ == '__main__':

    if len(sys.argv) < 2:
        while True:
            addr = input("\nEnter a stop name to change stop (or type \"exit\" to exit): ")
            if addr == "exit":
                break
            if addr == "help":
                print("\nUseful Information:")
                print("_______________________________")
                print("type 'exit' to stop the program")
                print("type '<stop>' to get the current tram times for that stop. e.g. 'a' ")
                print("current list of tram stops are: a, b, c, d, e, f")
                print("this file can also be used from the command line by typing \"python client.py <stop>\"\n")
            else:
                get_stop(addr)
    else:
        get_stop(sys.argv[1])
