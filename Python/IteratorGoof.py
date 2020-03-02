class IteratorGoof():

    def __init__(self):
        self.animals = ["cat","dog","turkey","camel","giraffe"]
        self.position = 0

    def __iter__(self):
        return self

    def __nextQ__(self):
        if (self.position < len(self.animals)):
           animal = self.animals[self.position]
           self.position= self.position+1
        else:
           animal = None
        return animal
        
    def __next__(self):
        try:
           animal = self.animals[self.position]
           self.position= self.position+1
        except StopIteration:
           print("No more items")
           return None

ig = IteratorGoof()
print(next(ig))
print(next(ig))
print(next(ig))
print(next(ig))
print(next(ig))
print(next(ig))
