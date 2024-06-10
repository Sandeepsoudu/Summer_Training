from abstractvehile import AbstractVehicle

class Bike(AbstractVehicle):
    def display(self):
        print("Bike details:")
        print(f"Colour: {self.colour}")
        print(f"Number of tyres: {self.num_tyres}")
        print(f"Gears: {self.gears}")

class Car(AbstractVehicle):
    def display(self):
        print("Car details:")
        print(f"Colour: {self.colour}")
        print(f"Number of tyres: {self.num_tyres}")
        print(f"Gears: {self.gears}")

class Auto(AbstractVehicle):
    def display(self):
        print("Auto details:")
        print(f"Colour: {self.colour}")
        print(f"Number of tyres: {self.num_tyres}")
        print(f"Gears: {self.gears}")


