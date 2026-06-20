# Parent class
class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

# Child class
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

# Grandchild class
class SportsCar(Car):
    def turbo(self):
        print("Turbo mode activated")

    def race(self):
        print("Sports car is racing")

# Create object
my_car = SportsCar()

# Call methods
my_car.start()   # From Vehicle
my_car.drive()   # From Car
my_car.turbo()   # From SportsCar
my_car.race()    # From SportsCar
my_car.stop()    # From Vehicle