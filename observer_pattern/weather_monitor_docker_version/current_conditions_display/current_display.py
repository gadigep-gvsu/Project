# current_conditions_display/current_display.py
from flask import Flask, request, jsonify
import requests
import os
import time

app = Flask(__name__)
SUBJECT_URL = os.environ.get('SUBJECT_URL', 'http://subject:5000')

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    print("\n--- Current Conditions ---")
    print(f"Temperature: {data['temperature']}°C")
    print(f"Humidity: {data['humidity']}%")
    print(f"Pressure: {data['pressure']} hPa")
    print("-------------------------")
    return jsonify({"status": "received"}), 200

def register_with_subject():
    max_retries = 5
    for _ in range(max_retries):
        try:
            response = requests.post(
                f"{SUBJECT_URL}/register", 
                json={"url": "http://current-display:5001"}
            )
            if response.status_code == 200:
                print("Successfully registered with subject")
                return
        except Exception as e:
            print(f"Registration failed: {e}")
            time.sleep(3)
    print("Failed to register with subject after multiple attempts")

if __name__ == "__main__":
    time.sleep(5)  # Wait for subject to be ready
    register_with_subject()
    app.run(host='0.0.0.0', port=5001)