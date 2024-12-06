from abc import ABC, abstractmethod
from typing import List

# Abstract base class for observers
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass

# Abstract base class for the subject (observable)
class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def register_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer {observer.__class__.__name__} registered successfully.")

    def remove_observer(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer {observer.__class__.__name__} removed successfully.")

    def notify_observers(self):
        for observer in self._observers:
            observer.update(
                temperature=self._temperature, 
                humidity=self._humidity, 
                pressure=self._pressure
            )

# Concrete implementation of the Subject (WeatherStation)
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()

# Concrete Observer implementations
class CurrentConditionsDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float):
        print("\n--- Current Conditions ---")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print("-------------------------")

class StatisticsDisplay(Observer):
    def __init__(self):
        self._temperatures: List[float] = []
        self._humidities: List[float] = []
        self._pressures: List[float] = []

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temperatures.append(temperature)
        self._humidities.append(humidity)
        self._pressures.append(pressure)

        print("\n--- Weather Statistics ---")
        print(f"Avg Temperature: {round(sum(self._temperatures)/len(self._temperatures), 1)}°C")
        print(f"Avg Humidity: {round(sum(self._humidities)/len(self._humidities), 1)}%")
        print(f"Avg Pressure: {round(sum(self._pressures)/len(self._pressures), 1)} hPa")
        print("-------------------------")

def main():
    # Create the weather station (subject)
    weather_station = WeatherStation()

    # Create observers
    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()

    # Register observers with the weather station
    weather_station.register_observer(current_display)
    weather_station.register_observer(stats_display)

    # Predefined weather measurements
    weather_measurements = [
        (25.5, 60.0, 1013.0),   # First measurement
        (26.8, 55.0, 1012.5),   # Second measurement
        (24.3, 65.0, 1014.2),   # Third measurement
        (27.1, 50.0, 1011.8),   # Fourth measurement
    ]

    # Update weather station with predefined measurements
    for temp, humidity, pressure in weather_measurements:
        print(f"\nSetting measurements: Temp {temp}°C, Humidity {humidity}%, Pressure {pressure} hPa")
        weather_station.set_measurements(temp, humidity, pressure)

    # Optional: Demonstrate removing an observer
    print("\nRemoving CurrentConditionsDisplay...")
    weather_station.remove_observer(current_display)
    
    # Add a final measurement after removing an observer
    print("\nAdding final measurement...")
    weather_station.set_measurements(23.7, 70.0, 1015.0)

if __name__ == "__main__":
    main()