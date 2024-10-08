from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def return_stop_info():
    data = request.get_json()
    print('data received')
    return jsonify({"response": 'this is a successful HTTP request to server'})



if __name__ == '__main__':
    app.run(port=5001)
