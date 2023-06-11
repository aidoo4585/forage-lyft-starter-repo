#abc is a module and ABC is a helper class that allows us to define abstract classes 
#abstractmethod is a decorator used to declare abstract methods within a class.
from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery


#Car inherits ABC so it can be an abc class
class Car(ABC):
    @abstractmethod
    def __init__(self, engine:Engine, battery: Battery ) -> None:
        #Composite relationship
        self._engine : Engine = engine      #private
        self._battery : Battery = battery   #private

    @abstractmethod
    def needs_service(self) -> bool:
        pass
