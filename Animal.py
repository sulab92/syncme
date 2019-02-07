'''
Created on Feb 7, 2019

@author: sthapa
'''
class TestAnimal:
    def __init__(self, dog , age):
        self.dog = dog
        self.age = age

    def bark(self):
        print("barking!!," + self.dog)


d1 = TestAnimal("Pug", 10)

d1.bark()