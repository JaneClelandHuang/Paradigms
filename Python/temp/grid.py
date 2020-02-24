from tkinter import * 
root = Tk()
canvas = Canvas(root, width=240, height=360)
canvas.pack()

#definition of the class starts here  
class Grid:  

    #defining constructor  
    def __init__(self, height=360, width=240):  
        self.height = height  
        self.width = width  
        canvas = Canvas(root, width, height)
        canvas.pack()
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
          
    #end of the class definition  
  
# Create an object of the class  
grid = Grid()