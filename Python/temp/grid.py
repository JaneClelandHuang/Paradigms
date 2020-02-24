from tkinter import * 
root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

#definition of the class starts here  
class Grid:  

    #defining constructor  
    def __init__(self, height=360, width=240):  
        self.height = height  
        self.width = width  
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
          
    #end of the class definition  
  
# Create an object of the class  
person1 = Person(5,6)  
#Create another object of the same class  
person2 = Person(9,10)  
#call member methods of the objects  
person1.showAge()  
person2.showName() 