from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


def request_stop_info(stop_number):
    url = 'http://localhost:5001/api'
    res = requests.post(url, json=stop_number)
    data = json.dumps(res.json())
    print(res.response)


@app.route('/receive_stop_info', methods=['POST'])
def receive_stop_info():
    data = request.get_json()
    print(data.response)
    return


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    request_stop_info(5)
