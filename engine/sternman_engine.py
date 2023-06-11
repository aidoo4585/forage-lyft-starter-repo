from abc import ABC

from engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_is_on):
        self._warning_light_on = warning_light_is_on    #private 

    def needs_service(self):
        super().needs_service()
        
        if self._warning_light_is_on:
            return True
        else:
            return False
