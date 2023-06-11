from abc import ABC, abstractmethod

#Cars are accessed through the Serviceable interface
class Serviceable(ABC): 
    @abstractmethod
    def needs_service(self) -> bool: 
        pass