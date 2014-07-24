#!/usr/bin/env python3


#classes
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return self.name +" is "+ str(self.age)

    def perform_trick(self):
        print("I am performing a trick")
        
    def sleep(self):
        print("I am sleeping")
    
#main routine
cat = Animal("Fluffy", 3)
dog = Animal("Rex", 7)

print(cat)
print(dog)

cat.sleep()
dog.perform_trick()
