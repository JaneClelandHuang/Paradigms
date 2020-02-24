from tkinter import * 
root = Tk()

#definition of the class starts here  
class Grid():  

    #defining constructor  
    def __init__(self, root): 
        self.height = 360 
        self.width = 240 
        canvas = Canvas(root, self.width, self.height)
        canvas.pack()	

        self.root = root
        self.canvas = canvas
		
        # Creates all vertical lines at intevals of 100
        for i in range(0, self.width+10, 10):
            canvas.create_line([(i, 0), (i, self.height)], tag='grid_line')

        # Creates all horizontal lines at intevals of 100
        for i in range(0, self.height+10, 10):
            canvas.create_line([(0, i), (self.width, i)], tag='grid_line')
  

 
    #end of the class definition  
  
# Create an object of the class  
grid = Grid(root)
root.mainloop()