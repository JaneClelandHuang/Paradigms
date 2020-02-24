# Python program showing 
# abstract base class work 
from abc import ABC, abstractmethod

class Polygon(ABC): 
    # abstract method 
    def noofsides(self): 
        pass

class Triangle(Polygon): 
    # overriding abstract method 
    #def noofsides(self): 
    #    print("I have 3 sides") 
    def extra(self):
        print("Dummy")

class Pentagon(Polygon): 
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides") 

class Hexagon(Polygon): 
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides") 

# Driver code 
triangle = Triangle() 
triangle.noofsides() 

pentagon = Pentagon() 
pentagon.noofsides() 

hexagon = Hexagon() 
hexagon.noofsides() 