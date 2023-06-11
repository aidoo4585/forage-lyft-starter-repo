from abc import ABC, abstractmethod

#Engine interface for all subsequent engines to inherit 
class Engine(ABC):

    @abstractmethod 
    def needs_service(self) -> bool: 
        pass
