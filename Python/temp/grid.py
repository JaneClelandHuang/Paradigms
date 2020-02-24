import tkinter as tk
root = tk.Tk()
 
class Grid:
    def __init__(self,width=240,height=360): #,width=240,height=420):
	    self.width = width
        self.height=height

grid = Grid()
root.mainloop()
