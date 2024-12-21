from abc import ABC, abstractmethod
import logging

class Logger:
    def log(self, message: str):
        pass

class LoggerImpl(Logger):
    def __init__(self, logger_name: str):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        logger.addHandler(ch)

        self.logger = logger

    @abstractmethod
    def log(self, message: str):
        self.logger.info(message)

car_logger: Logger = LoggerImpl('Car')
motorcycle_logger: Logger = LoggerImpl('Motorcycle')

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, make: str, model: str, market: str, logger: Logger):
        self.make = make
        self.model = model
        self.market = market
        self.logger: Logger = logger

    def start_engine(self):
        self.logger.log(f"{self.make} {self.model} ({self.market}): Двигун запущено")

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, market: str, logger: Logger):
        self.make = make
        self.model = model
        self.market = market
        self.logger: Logger = logger
        
    def start_engine(self):
        self.logger.log(f"{self.make} {self.model} ({self.market}): Мотор заведено")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        return

    @abstractmethod
    def create_motorcycle(self) -> Motorcycle:
        return

class USVehicleFactory(VehicleFactory):
    def create_car(self):
        return Car("Toyota", "Corolla", "US Spec", car_logger)
    
    def create_motorcycle(self):
        return Motorcycle("Harley-Davidson", "Sportster",  "US Spec", motorcycle_logger)
    
class EUVehicleFactory(VehicleFactory):
    def create_car(self):
        return Car("Toyota", "Corolla", "EU Spec", car_logger)
    
    def create_motorcycle(self):
        return Motorcycle("Harley-Davidson", "Sportster",  "EU Spec", motorcycle_logger)
    
usFactory = USVehicleFactory()

usFactory.create_car().start_engine()
usFactory.create_motorcycle().start_engine()

euFactory = EUVehicleFactory()

euFactory.create_car().start_engine()
euFactory.create_motorcycle().start_engine()
