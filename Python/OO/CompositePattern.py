from abc import ABC, abstractmethod

def Component(ABC):
    def performOperation(self): 
        pass

def Leaf(ABC,Component): # Strictly speaking, unnecessary
    def performOperation(self):
        pass


def Composite(ABC,Component):
    def __init__(self):
        self.children = list[]
        
    def performOperation(self):
        for child in self.children:
            child.performOperation()
         
    def add(self,childComponent):
        #if(childComponent
        print(type(childComponent))
        self.children.append(childComponent)
        
    def remove(self,childComponent):
        self.children.remove(childComponent)
    

