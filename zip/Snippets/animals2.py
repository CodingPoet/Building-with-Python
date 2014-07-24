#!/usr/bin/env python3


#classes
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return self.name +" is "+ str(self.age)
    
    def sleep(self):
        print("I am sleeping")


class Dog:
    #complete this class
    #needs an _init__, __str__, and perform_trick method
    
#main routine
cat = Cat("Fluffy", 3)
dog = Dog("Rex", 7)

print(cat)
print(dog)

cat.sleep()
dog.perform_trick()
