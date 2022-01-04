import uuid
import time
from random import random, randint, choice
from abc import abstractmethod, ABC


class Animal(ABC):
    types = ('Predators', 'Herbivores')

    def __init__(self, power, speed):
        self.id = uuid.uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed
        self.is_out_of_a_power = False

    def eat(self, power):
        self.current_power += power
            if self.current_power + power >= self.max_power:
                self.current_power = self.max_power


    def lost_power(self, power):
        self.current_power -= power
        if self.current_power - power <= 0:
            self.is_out_of_a_power = True

    @abstractmethod
    def name(self):
        pass

    def animal_information(self):
        return self.name() + ' ' + str(self.id)




class Predator(Animal):
    def name(self):
        return self.types[1]


class Herbivorous(Animal):
    def name(self):
        return self.types[0]



class Forest:

    def __init__(self):
        self.animals = dict()

    def add_animal(self, animal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal):
        del self.animals[animal.id]

    def animals_count(self):
        return len(self.animals)


    @property
    def hunting_possible(self):
        if self.animals_count() <= 1:
            return False
        return True

    def get_animal(self, predator_id=None):
        if not isinstance(predator_id, type(None)):
            note_list = list(note for note in self.animals.keys()
                             if note != predator_id)
        else:
            note_list = list(self.animals.keys())
        animal_note = random.choice(note_list)
        return self.animals[animal_note]

    @staticmethod
    def print_animal_note():
        for animal in forest.animals.keys():
            print(forest.animals[animal].animal_info())

    def any_predator_left(self):
        for key in self.animals.keys():
            if isinstance(self.animals[key], Predator):
                return True
            return False

    def start_hunting(self):
        predator = Forest.get_animal(self)
        if isinstance(predator, Herbivorous):
            predator.eat(50)
        victim = Forest.get_animal(self, predator.id)
        if predator.speed > victim.speed and \
                predator.current_power > victim.current_power:
            predator.eat(50)
            victim.small_power = True
        else:
            predator.lose_power(30)
            victim.lose_power(30)
        if predator.small_power:
            self.remove_animal(predator)
        if victim.small_power:
            self.remove_animal(victim)




class AnimalGeneartor:
    def __iter__(self):
        return self

    def __next__(self):
        animal_type = random.choice(Animal.types)

        if animal_type == "Predator":
            new_animal = Predator(random.randint(25, 100),
                                  random.randint(25, 100))
        else:
            new_animal = Herbivorous(random.randint(25, 100),
                                     random.randint(25, 100))

        return new_animal


if __name__ == "__main__":
    nature = AnimalGeneartor()
    forest = Forest()
    for i in range(8):
        animal = next(nature)
        forest.add_animal(animal)
    print("Who leaves in the forest?")
    forest.print_animal_note()

    print("Let`s start hunting!")
    time.sleep(3)
    while forest.any_predator_left() and forest.hunting_possible:
        forest.start_hunting()

    print("Are there any survivors?")
    forest.print_animal_note()
