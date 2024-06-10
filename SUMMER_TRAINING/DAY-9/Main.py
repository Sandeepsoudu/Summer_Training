from vehicle import Bike, Car, Auto
def main():
    xpulse = Bike("Black", 2, 5)
    xuv700 = Car("Black", 4, 6)
    trali_auto = Auto("Yellow", 3, 4)
    xpulse.display()
    print("\n")
    xuv700.display()
    print("\n")
    trali_auto.display()
if __name__ == "__main__":
    main()
