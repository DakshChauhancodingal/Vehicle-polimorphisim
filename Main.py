class Car:
    def fuel_type(self):
        print("This car uses generic fuel.")

    def max_speed(self):
        print("This car has a generic maximum speed.")

class BMW(Car):
    def fuel_type(self):
        print("BMW uses premium Diesel or Petrol.")

    def max_speed(self):
        print("BMW max speed is 240 km/h.")

# A generalized function to demonstrate polymorphism
def display_car_info(car_object):
    car_object.fuel_type()
    car_object.max_speed()

# Create instances of both classes
car = Car()
bmw = BMW()

print("--- Generic Car Details ---")
display_car_info(car)

print("\n--- BMW Details ---")
display_car_info(bmw)
