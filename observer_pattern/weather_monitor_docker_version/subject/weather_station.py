# subject/weather_station.py
import time
import requests
from flask import Flask, request, jsonify
import threading
import os
from shared.observer import Subject

app = Flask(__name__)
weather_station = None

class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

    def notify_observers(self):
        payload = {
            'temperature': self._temperature,
            'humidity': self._humidity,
            'pressure': self._pressure
        }
        for observer_url in self._observers:
            try:
                requests.post(f"{observer_url}/update", json=payload)
            except Exception as e:
                print(f"Failed to notify {observer_url}: {e}")

def simulate_measurements():
    measurements = [
        (25.5, 60.0, 1013.0),
        (26.8, 55.0, 1012.5),
        (24.3, 65.0, 1014.2),
        (27.1, 50.0, 1011.8)
    ]
    for temp, humidity, pressure in measurements:
        print(f"Setting measurements: {temp}°C, {humidity}%, {pressure} hPa")
        weather_station.set_measurements(temp, humidity, pressure)
        time.sleep(2)

@app.route('/register', methods=['POST'])
def register_observer():
    observer_url = request.json.get('url')
    weather_station.register_observer(observer_url)
    return jsonify({"status": "Observer registered"}), 200

@app.route('/unregister', methods=['POST'])
def unregister_observer():
    observer_url = request.json.get('url')
    weather_station.remove_observer(observer_url)
    return jsonify({"status": "Observer unregistered"}), 200

@app.route('/observers', methods=['GET'])
def list_observers():
    return jsonify(weather_station.get_observers()), 200

if __name__ == "__main__":
    weather_station = WeatherStation()
    
    # Start measurement simulation in a separate thread
    sim_thread = threading.Thread(target=simulate_measurements)
    sim_thread.start()
    
    app.run(host='0.0.0.0', port=5000)