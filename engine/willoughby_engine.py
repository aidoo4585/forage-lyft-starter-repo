from abc import ABC
from engine import Engine

class WilloughbyEngine(Engine, ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self._current_mileage = current_mileage             #private
        self._last_service_mileage = last_service_mileage   #private

    def needs_service(self) -> bool:
        super().needs_service() #call from parent engine class

        if self._current_mileage > 6000:
            return True
        else: 
            return self._current_mileage - self._last_service_mileage > 60000
