from datetime import date
from car import Car 
from capulet_engine import Capulet 
from sternman_engine import Sternman
from willoughby_engine import Willoughby
from nubbin_battery import Nubbin
from spindler_battery import Spindler


class CarFactory: 
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int ) -> Car:
        #constract car model
        engine = Capulet(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date , current_date)
        car = Car(engine, battery)
        return car

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = Willoughby(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def  create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = Sternman(warning_light_on)
        battery = Spindler(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = Willoughby(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date , current_date)
        car = Car(engine, battery)
        return car
    
    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = Capulet(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        car = Car(engine, battery)
        return car    
