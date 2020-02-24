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
        print("Finished Triangle print")

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

number = 0;
for shape in list:
    print("Start loop")
    print (number)
    number = number+1
    print (shape.noofsides())# Driver code 
    print ("After")
    

