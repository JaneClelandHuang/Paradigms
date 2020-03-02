class IteratorGoof():

    def __init__(self):
        self.animals = ["cat","dog","turkey","camel","giraffe"]
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self.position < len(self.animals)-1):
           animal = self.animals[self.position]
           self.position= self.position+1
        else:
            animal = None
        return animal
        
ig = IteratorGoof()
print(next(ig))
print(next(ig))
print(next(ig))
print(next(ig))
print(next(ig))
print(next(ig))
print("Continue anyway")
