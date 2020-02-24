from tkinter import * 
root = Tk()
canvas = Canvas(root, width=240, height=360)
canvas.pack()

#definition of the class starts here  
class Grid():  

    #defining constructor  
    def __init__(self, height=360, width=240):  
        self.height = height  
        self.width = width  
        # Creates all vertical lines at intevals of 100
        for i in range(0, self.width+10, 10):
            canvas.create_line([(i, 0), (i, self.height)], tag='grid_line')

        # Creates all horizontal lines at intevals of 100
        for i in range(0, self.height+10, 10):
            canvas.create_line([(0, i), (self.width, i)], tag='grid_line')
        c = root.Canvas(root, height=1000, width=1000, bg='white')
        c.pack(fill=tk.BOTH, expand=True)

 
    #end of the class definition  
  
# Create an object of the class  
grid = Grid()