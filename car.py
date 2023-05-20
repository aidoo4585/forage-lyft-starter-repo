#abc is a module and ABC is a helper class that allows us to define abstract classes 
#abstractmethod is a decorator used to declare abstract methods within a class.
from abc import ABC, abstractmethod


#Car inherits ABC so it can be an abs class
class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass
