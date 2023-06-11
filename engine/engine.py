from abc import ABC, abstractmethod

#Engine interface for all subsequent engines to inherit 
#adding new engine part -> inherting from Engine interface
class Engine(ABC):

    @abstractmethod 
    def needs_service(self) -> bool: 
        pass
