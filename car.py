from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery
from servicable import Serviceable
class Car(Serviceable, ABC):
    def __init__(self, engine:Engine, battery: Battery ) -> None:
        #Composite relationship
        self._engine : Engine = engine      #private
        self._battery : Battery = battery   #private

    def needs_service(self) -> bool:
        super().needs_service()

        #Both engine and battery need to be working fine 
        if self._engine.needs_service() or self._battery.needs_service(): 
            return True 
        else: 
            return False
