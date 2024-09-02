from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"current_time": current_time})

@app.route('/welcome', methods=['GET'])
def welcome():
    return jsonify({
        "message": "Welcome to Shotlet!",
        "description": "Your gateway to seamless short-term rentals.",
        "features": [
            "Easy booking process",
            "Wide range of properties",
            "Secure transactions",
            "24/7 customer support"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)