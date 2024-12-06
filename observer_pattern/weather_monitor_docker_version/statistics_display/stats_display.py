# statistics_display/stats_display.py
from flask import Flask, request, jsonify
import requests
import os
import time
import statistics

app = Flask(__name__)
SUBJECT_URL = os.environ.get('SUBJECT_URL', 'http://subject:5000')

class WeatherStatistics:
    def __init__(self):
        self.temperatures = []
        self.humidities = []
        self.pressures = []

    def update(self, temperature, humidity, pressure):
        self.temperatures.append(temperature)
        self.humidities.append(humidity)
        self.pressures.append(pressure)

        print("\n--- Weather Statistics ---")
        print(f"Avg Temperature: {statistics.mean(self.temperatures):.1f}°C")
        print(f"Avg Humidity: {statistics.mean(self.humidities):.1f}%")
        print(f"Avg Pressure: {statistics.mean(self.pressures):.1f} hPa")
        print("-------------------------")

stats = WeatherStatistics()

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    stats.update(
        data['temperature'], 
        data['humidity'], 
        data['pressure']
    )
    return jsonify({"status": "received"}), 200

def register_with_subject():
    max_retries = 5
    for _ in range(max_retries):
        try:
            response = requests.post(
                f"{SUBJECT_URL}/register", 
                json={"url": "http://stats-display:5002"}
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
    app.run(host='0.0.0.0', port=5002)