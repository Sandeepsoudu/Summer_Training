from abc import ABC, abstractmethod

class AbstractVehicle(ABC):
    def __init__(self, colour, num_tyres, gears):
        self.colour = colour
        self.num_tyres = num_tyres
        self.gears = gears
    
    @abstractmethod
    def display(self):
        pass
