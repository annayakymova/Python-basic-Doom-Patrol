#1.
class Laptop:
    def __init__(self):
        battery_1 = Battery('There is 1 battery in the laptop')
        battery_2 = Battery('And there are 2 batteries in the laptpo')
        self.battery = (battery_1, battery_2)

class Battery:
    def __init__(self, autonomous_work):
        self.autonomous_work = autonomous_work

        laptop = Laptop()
        print(laptop.battery[0].autonomous_work)
        print(laptop.battery[1].autonomous_work)


#2
class Guitar:
    def __init__(self, strings):
        self.strings = strings

class GuitarString:
    def __init__(self):
        pass

strings = GuitarString()
guitar = Guitar(strings)

#3
class Calc:
    @staticmethod
    def add_nums(x, y, z):
        return x + y + z

    sum = Calc.add_nums(45, 67, 98)
    print(sum)

#4
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pasta contains ({self.ingredients})'

    @classmethod
    def carbonara(cls):
        return cls(['parmesan', 'eggs', 'bacon'])

    @classmethod
    def bolognaise(cls):
        return cls(['tomatoes', 'forcemeat'])


pasta_c = Pasta.carbonara()
pasta_b = Pasta.bolognaise()
print(pasta_c)
print(pasta_b)

#5
class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= self.max_visitors_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitors_num

#6
from dataclasses import dataclass


@dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


addressbook = AddressBookDataClass(key = 'one', name = 'Anna',
                              phone_number = 'one',
                              address ='Shevchenko Avenue',
                              email = 'annaya@email.com',
                              birthday = '29/01/04',
                              age = '17')
print(addressbook)

#7
from collections import namedtuple
AddressBookDataClass_1 = namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address',
                                                           'email', 'birthday', 'age'])
addressbook = AddressBookDataClass_1(key = 'one', name = 'Anna', phone_number = 'one',
                     address = 'Shevchenko Avenue', email = 'annaya@email.com',
                     birthday = '29/01/2004', age = '17')
print(addressbook)


#8
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key = {self.key}, name = {self.name}, phone_number = {self.phone_number},' \
               f' address = {self.address}, email = {self.email}, birthday = {self.birthday}, ' \
               f'age = {self.age})'

addressbook = AddressBook(key = 'one', name = 'Anna', phone_number = 'one',
                     address = 'Shevchenko Avenue', email = 'annaya@email.com',
                     birthday = '29/01/2004', age = '17')
print(addressbook)

#9
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def person_age(self):
        return self.age


person_j = Person('John', 36, 'USA')
print(person_j.age)

person_j.person_age = 89
print(person_j.person_age)

#10
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(0, 'Anna')
setattr(student, 'email', 'annaya@gmail.com')
print(getattr(student, 'email'))

#11
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        return self._temperature * 1.8 + 32


obj_temperature = Celsius(68)
print(obj_temperature.fahrenheit)