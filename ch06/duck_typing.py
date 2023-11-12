class Vehicle:
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Bicycle:
    def drive(self):
        print("Riding a bicycle")

def drive_vehicle(vehicle):
    vehicle.drive()

my_car = Car()
my_bicycle = Bicycle()

drive_vehicle(my_car) # Driving a car
drive_vehicle(my_bicycle) # Riding a bicycle