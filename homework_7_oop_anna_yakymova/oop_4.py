from abc import ABC, abstractmethod

stages = {0: 'None', 1: 'Flowering', 2: 'Green', 3: 'Red'}

class GardenMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Garden(metaclass=GardenMeta):

    def __init__(self, vegetables, fruits, pests):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests

    def see_the_garden(self):
        print(f"There are {self.vegetables.number_of_fruits} {self.vegetables.all_fruits[0].veg_type if self.vegetables.number_of_fruits > 0 else ''} tomato vegetables, {self.fruits.number_of_fruits} {self.fruits.all_fruits[0].fruit_type if self.fruits.number_of_fruits > 0 else ''}apple fruits and {', '.join(pest.pest_type for pest in self.pests)} pests in the garden")

class Plant(ABC):
    def grow(self):
        self.state += 1 if self.state < 3 else 0
        self.grow_info()

    def is_ripe(self):
        return self.state == 3

    @abstractmethod
    def grow_info(self):
        pass

    def get_state(self):
        return self.state


class Vegetable(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def grow_info(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass


class Fruit(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def grow_info(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass


class Tomato(Vegetable):
    name = 'tomato'

    def __init__(self, tomato_index, veg_type):
        self.index = tomato_index
        self.veg_type = veg_type
        self.stage = 0

    def grow(self):
        if self.stage < 3:
            self.stage += 1

    def is_ripe(self):
        return self.stage == 3

    def grow_info(self):
        print(f"{self.veg_type} tomato - {self.index}: {stages[self.stage]}")

class TomatoBush:

    def __init__(self, number_of_fruits):
        self.number_of_fruits = number_of_fruits
        self.all_fruits = [Tomato(index, 'Rose') for index in range(number_of_fruits)]

    def grow_all(self):
        for tomato in self.all_fruits:
            tomato.grow()
            tomato.grow_info()

    def is_all_ripe(self):
        return all([tomato.is_ripe() for tomato in self.all_fruits])

    def give_harvest(self):
        self.all_fruits = []
        self.number_of_fruits = 0

class Apple(Fruit):
    name = 'apple'

    def __init__(self, apple_index, fruit_type):
        self.index = apple_index
        self.fruit_type = fruit_type
        self.stage = 0

    def grow(self):
        if self.stage < 3:
            self.stage += 1

    def is_ripe(self):
        return self.stage == 3

    def grow_info(self):
        print(f"{self.fruit_type} apple - {self.index}: {stages[self.stage]}")

class AppleTree:
    def __init__(self, number_of_fruits):
        self.number_of_fruits = number_of_fruits
        self.all_fruits = [Apple(index, 'Golden') for index in range(number_of_fruits)]

    def grow_all(self):
        for apple in self.all_fruits:
            apple.grow()
            apple.grow_info()

    def is_all_ripe(self):
        return all([apple.is_ripe() for apple in self.all_fruits])

    def give_harvest(self):
        self.all_fruits = []
        self.number_of_fruits = 0


class Gardener:
    trees_1 = {'Fruits': False, 'Veggies': False}
    def __init__(self, name, plants_list, pests_list):
        self.name = name
        self.plants_list = plants_list
        self.pests_list = pests_list

    def take_care(self):
        print(f'{self.name} is watering the plants...')
        for plant in self.plants_list:
            plant.grow_all()

    def harvest(self):
        plants_to_harvest = []

        plants_to_harvest += ([plant for plant in self.plants_list
                               if isinstance(plant, AppleTree)
                               and self.trees_1['Fruits']])

        plants_to_harvest += ([plant for plant in self.plants_list
                               if isinstance(plant, TomatoBush)
                               and self.trees_1['Veggies']])

        plants_to_be_eaten = [plant for plant in self.plants_list
                              if plant not in plants_to_harvest]
        for plant in plants_to_be_eaten:
            plant.eaten_by_pests()

        for plant in self.plants_list:
            if plant.is_all_ripe():
                print("Harvest is done")
                plant.give_harvest()
            else:
                print("Not ready to harvest")

    def poison_pests(self, pests_type):
        for i in range(len(self.pests_list)):
            for j in range(len(self.pests_list[i])):
                if self.pests_list[i][j].pest_type == pests_type:
                    self.pests_list[i][j].time_to_die()
                    self.pests_list[i][j] = ""
                    self.trees_1[pests_type] = True

        for i in self.trees_1.keys():
            if self.trees_1[i]:
                print(f"{i} pests  died!")


class Pests:
    def __init__(self, pests_type, pests_quantity, plants):
        self.pets_type = pests_type
        self.pests_quantity = pests_quantity
        self.plants = plants

    def eat_plants():
        for plant in plants:
            if plant.is_ripe_for_pests():
                plant.harvest()

            def time_to_die(self):
                del self



apple_tree = AppleTree(2)
tomato_bush = TomatoBush(1)
print(tomato_bush.all_tomatoes)
print(apple_tree.all_apples)

gardener = Gardener("Homer", [apple_tree, tomato_bush],
                    [apple_tree.all_pests, tomato_bush.all_pests])

for _ in range(3):
       gardener.take_care()

gardener.poison_pests("Fruits") # method which deletes pests of passed type
gardener.harvest()  # if pests haven't been poison, there will be no harvest
print(tomato_bush.all_tomatoes)
print(apple_tree.all_apples)
