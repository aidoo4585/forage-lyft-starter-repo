from abc import ABC, abstractmethod
from battery import Battery

class Spindler(Battery, ABC): 
    def __init__(self, last_service_date:int , current_date:int) -> None:
        self._last_service_date : int = last_service_date   #private
        self._current_date: int = current_date              #private
    
    #battery service once every two years 
    def needs_service(self) -> bool: 
        super().needs_service()

        if self._last_service_date > 2: 
            return True 
        else: 
            return self._current_date - self._last_service_date > 2
        