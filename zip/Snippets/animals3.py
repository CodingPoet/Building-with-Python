#!/usr/bin/env python3

#classes
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return self.name +" is "+ str(self.age)

class Dog(Animal):
    def perform_trick(self):
        print("I am performing a trick")
        
class Cat(Animal):
    def sleep(self):
        print("I am sleeping")
    
#main routine
cat = Cat("Fluffy", 3)
dog = Dog("Rex", 7)

print(cat)
print(dog)

cat.sleep()
dog.perform_trick()