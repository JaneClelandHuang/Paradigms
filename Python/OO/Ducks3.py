# Ducks basic
from abc import ABC, abstractmethod
from QuackBehavior import QuackBehavior
from FlyBehavior import FlyBehavior

class Duck(ABC): 
    def __init__(self,flyBehavior,quackBehavior):
        super().__init__()
        self.flyBehavior = flyBehavior
        self.quackBehavior = quackBehavior
    
    @abstractmethod
    def display(self):
        pass
        
    def quack(self):
        quackBehavior.quack()
    
    def fly(self):
        flyBehavior.fly()

class MallardDuck(Duck): 
    def display(self,flyBehavior,quackBehavior):
        print ("I'm a Mallard Duck")
    
class RedHeadDuck(Duck):
    def display(self,flyBehavior,quackBehavior):
        print ("I'm a RedHeadDuck")
        
class RubberDucky(Duck):
    def display(self,flyBehavior,quackBehavior):
        print ("I'm just a RubberDucky")

    def quack(self):
        print ("Peep Peep")

list = []
list.append(MallardDuck(FlyWithWings(),Quack()))
list.append(RedHeadDuck(FlyWithWings(),Quack()))
list.append(RubberDucky(FlyNoWay(),Peep()))

for duck in list:
    duck.display()
    duck.quack()
    duck.fly()