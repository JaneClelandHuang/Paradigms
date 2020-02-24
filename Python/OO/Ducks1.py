# Python program showing 
# abstract base class work 
from abc import ABC, abstractmethod

class Duck(ABC): 
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def quack(self):
        pass
    
    def fly(self):
        pass

class MallardDuck(Duck): 
    def quack(self):
        print("Quack Quack")
    def fly(self):
        print("I'm flying")
    
class RedHeadDuck(Duck):
    def quack(self):
        print("Quack Quack")
    def fly(self):
        print("I'm flying")
        
class RubberDucky(Duck):
    def quack(self):
        print("Peep Peep")
    def fly(self):
        print("I'm flying")

list = []
list.append(MallardDuck())
list.append(RedHeadDuck())
list.append(RubberDucky())

for duck in list:
    print (duck.quack())

