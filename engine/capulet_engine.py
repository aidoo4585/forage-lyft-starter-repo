from abc import ABC
from engine import Engine


class CapuletEngine(Engine, ABC):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self._last_service_mileage: int = last_service_mileage   #private
        self._current_mileage: int = current_mileage             #private

    def needs_service(self) -> bool:  
        super().needs_service()

        if self._current_mileage > 3000: 
            return True
        else:
            return self._current_mileage - self._last_service_mileage > 3000
