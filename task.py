import pandas as pd


class Pet:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age
    def display_info(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"
    def birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are {self.age} years old today."
    

my_Dog = Pet("rex", "alsatian", 6)

print(my_Dog.display_info())
print(my_Dog.birthday())  
print("Animal Name:", my_Dog.name)
print("Animal Age:", my_Dog.age)
print("Animal Species:", my_Dog.species)
   