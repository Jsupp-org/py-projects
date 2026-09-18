class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate
        
    def calculate_rental(self, days):
        return self.rental_rate * days

    def display_info(self):
        print(f"Brand: {self.brand}"
              f"\nModel: {self.model}"
              f"\nRental Rate: {self.rental_rate}")
               

 
class Car(Vehicle):
    def __init__(self, brand, model, rental_rate, number_of_seats):
        super().__init__(brand, model, rental_rate)
        self.number_of_seats = number_of_seats

    def get_vehicle_type(self):
        return "Car"

 
class Motorcycle(Vehicle):
    def __init__(self, brand, model, rental_rate, engine_cc):
        super().__init__(brand, model, rental_rate)
        self.engine_cc = engine_cc

    def get_vehicle_type(self):
        return "Motorcycle"


car1 = Car("Toyota", "Vios", 1500, 5)
car2 = Car("Honda", "Civic", 2000, 5)

motor1 = Motorcycle("Yamaha", "R15", 1000, 250)
motor2 = Motorcycle("BMW", "S1000", 5000, 1000)

vehicles = [car1, car2, motor1, motor2]

for vehicle in vehicles:
    vehicle.display_info()
    print(f"Type: {vehicle.get_vehicle_type()}")
    print(f"3-day Rental Cost: {vehicle.calculate_rental(3)}\n")