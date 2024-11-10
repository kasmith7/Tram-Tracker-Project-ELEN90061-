# Tram Tracker
Tram Tracker is a RESTful API project by Arief Wibiwo and Kevin Smith for our
Communication Networks ELEN90061 Final Project.

## About our Project
We created the Tram Tracker in order to model a system which uses RESTful APIs in an everyday use case.
We wanted to come up with a connectionless server which could communicate with trams, and with 
passengers, through 2 different APIs.
The current scope of the project includes a HTTP server which contains the information for 2 tram lines,
4 unique trams, and an API for client apps.

Client.py allows for the direct requesting of tram stop data from the server.


We designed it this way to take advantage of the flexibility and reusability offered by RESTful APIs and keep 


## Installation

_Below is an example of how you can install the Tram Tracker project._

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install project dependencies from requirements.txt
   ```bash
   pip install -r /path/to/requirements.txt
   ```

## Usage

1. To start using the Tram Tracker, run "server.py", and the "tramX.py" scripts in seperate terminals from the /src
   directory.

   These tram scripts will communicate via HTTP with the server, sending their locational data to the server.


2. Run the client.py script in a seperate terminal in the '/src' folder using either:
   ```bash
   python client.py
   ```
   or
   ```bash
   python client.py stop_name
   ```
   #
   'client.py' also acts as an API which users can import into their Tram Tracker GUI applications using:
   ```bash
   import client.py
   
   ...
   //rest of TRAM_TRACKER_APP//
   ...
   ```


Valid input for stop_name are the lower case letters 'a' to 'f'.
   

   Calling client.py along with a stop name will return the current tram distances from the inputted stop once 
   before terminating the script.

   Emitting the stop name will make the script loop, allowing you to make multiple calls to the server without ending
   the script.
   
###
More tram lines can be easily added by adding the new line to the route_stops dictionary in server.py,
and making sure that any tram the will run on this new line also has its route_stops updated to include it.

