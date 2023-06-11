from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery
class Car(ABC):
    @abstractmethod
    def __init__(self, engine:Engine, battery: Battery ) -> None:
        #Composite relationship
        self._engine : Engine = engine      #private
        self._battery : Battery = battery   #private

    @abstractmethod
    def needs_service(self) -> bool:
        pass
