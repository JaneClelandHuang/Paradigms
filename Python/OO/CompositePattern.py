from abc import ABC, abstractmethod

class Component(ABC):
    def performOperation(self): 
        pass

class Leaf(Component): # Strictly speaking, unnecessary
    def performOperation(self):
        pass


class Composite(Component):
    def __init__(self):
        self.children = []
        print("I'm called")
        super().__init__()
        
    def performOperation(self):
        for child in self.children:
            child.performOperation()
         
    def add(self,childComponent):
        self.children.append(childComponent)
        
    def remove(self,childComponent):
        self.children.remove(childComponent)
    

