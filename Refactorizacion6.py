class Vehicle:
    def calculate_travel_time(self, distance):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def calculate_travel_time(self, distance):
        speed = 60  # km/h
        time = distance / speed
        return f"Travel time by car: {time:.2f} hours"

class Bicycle(Vehicle):
    def calculate_travel_time(self, distance):
        speed = 15  # km/h
        time = distance / speed
        return f"Travel time by bicycle: {time:.2f} hours"

class Bus(Vehicle):
    def calculate_travel_time(self, distance):
        speed = 40  # km/h
        time = distance / speed
        return f"Travel time by bus: {time:.2f} hours"


vehicles = [
    Car(),
    Bicycle(),
    Bus()
]


distance = 100


for vehicle in vehicles:
    print(vehicle.calculate_travel_time(distance))