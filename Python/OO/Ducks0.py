# Ducks basic

class Duck(): 
    def __init__(self):
        super().__init__()
                  
    def quack(self):
        print("Quack Quack")
    
    def swim(self):
        print("I'm swimming")

class MallardDuck(Duck): 
    def duckName(self):
        print ("I'm a Mallard Duck")
    
class RedHeadDuck(Duck):
    def duckName(self):
        print ("I'm a RedHeadDuck")
        
class RubberDucky(Duck):
    def duckName(self):
        print ("I'm just a RubberDucky")

list = []
list.append(MallardDuck())
list.append(RedHeadDuck())
list.append(RubberDucky())

for duck in list:
    duck.duckName()
    duck.quack()
    duck.swim()
    
    
    
    
    

