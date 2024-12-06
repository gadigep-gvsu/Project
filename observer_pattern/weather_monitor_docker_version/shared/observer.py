# shared/observer.py
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def register_observer(self, observer_url: str):
        if observer_url not in self._observers:
            self._observers.append(observer_url)
            print(f"Observer {observer_url} registered successfully.")

    def remove_observer(self, observer_url: str):
        if observer_url in self._observers:
            self._observers.remove(observer_url)
            print(f"Observer {observer_url} removed successfully.")

    def get_observers(self):
        return self._observers