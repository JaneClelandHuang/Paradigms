# FlyBehavior
from abc import ABC, abstractmethod

class QuackBehavior(ABC): 
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def quack(self):
        pass
        
class Quack(QuackBehavior): 
    def display(self):
        print ("Quack, Quack")
    
class Peep(QuackBehavior):
    def display(self):
        print ("Peep, Peep")
        
class Mute(QuackBehavior):
    def display(self):
        print ("...")