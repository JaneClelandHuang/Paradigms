# Python program showing 
# abstract base class work 
from abc import ABC, abstractmethod

class Polygon(ABC): 
    # abstract method 
    def noofsides(self): 
        pass

class Triangle(Polygon): 
    def noofsides(self):
        print("I have three sides")

class Pentagon(Polygon): 
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides") 

class Hexagon(Polygon): 
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides") 

# Driver code 
list = []
list.append(Triangle())
print(len(list))
list.append(Pentagon())
list.append(Hexagon())

for shape in list:
    print ("Before")
    print (shape.noofsides())# Driver code 
    print ("After")
    

