from abc import ABC
from car import Car


class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date) #calls value from parent class
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self) -> bool:
        #if the value is more than 30000 returns true
        #return true if the current mileage < last mileage
        return self.current_mileage - self.last_service_mileage > 30000
