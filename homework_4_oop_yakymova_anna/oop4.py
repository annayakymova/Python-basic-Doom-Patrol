#1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    vehicle_type = 'regular vehicle'

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_max_speed_and_mileage(self):
        print(f'The vehicle has {self.max_speed} and {self.mileage}')

    car = Vehicle(10, 100)
    car.print_max_speed_and_mileage()


#2.Create a child class Bus that will inherit all the variables and methods of the Vehicle class and will have seating_capacity own method
    
 class Bus(Vehicle):

    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def get_max_speed(self):
       print(f'The bus has {self.max_speed}')

        bus = Bus(89,199, 78)
        bus.seating_capacity()

#3. Determine which class a given Bus object belongs to (Check type of an object)
print(type(bus))

#4. Create an instance of Bus named school_bus and determine if school_bus is also an instance of the Vehicle class
school_bus = Bus(18989, 1880, 61)
       print(isinstance(school_bus, Vehicle))

#5. Create a new class School with get_school_id and number_of_students instance attributes
      class School:

 def __init__(self, school_id, number_of_students):
    self.school_id = school_id
    self.number_of_students = number_of_students

def print_school_id_and_number_of_students(self):
        print(f'The school class has {self.school_id} and {self.number_of_students}')


#6*. Create a new class SchoolBus that will inherit all the methods from School and Bus and will have its own - bus_school_color
class SchoolBus(Bus, School):
    def __init__(self, max_speed, mileage, capacity, bus_color):
        super().__init__(max_speed, mileage, capacity)
        self.bus_color = bus_color
    def bus_school_color(self):
            print(f' The school bus has {self.bus_color}')

#7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,make a tuple of it and by using for call their action using the same method.
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
    print(f'bear {self.sound}')


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f'wolf {self.sound}')

bear = Bear("ohh i want to complete these tasks")
wolf = Wolf("i want that too")
predators = (bear, wolf)



for predators in (bear, wolf):
    predators.make_sound()

#8*. Create class City with name, population instance attributes, return a new instance only when population > 1500, otherwise return message: "Your city is too small". Hint: use magic methods / patterns
class City:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        new_instance = super(City, cls).__new__(cls)
        if population > 1500:
            return new_instance
        else:
            print("Your city is too small")




