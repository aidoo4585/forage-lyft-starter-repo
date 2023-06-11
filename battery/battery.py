from abc import ABC, abstractmethod

#modifying the behvaiour of a part for all cars 
#requires just modifying the interface
class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

