import tkinter as tk
root = tk.Tk()

class Grid:

    def __init__(self,width=240,height=420):
	    this.width = width
        this.height = height

        # Creates all vertical lines at intevals of 10
        for i in range(0,w+10,10):
            c.create_line([(i, 0), (i, h)], tag='grid_line')

        # Creates all horizontal lines at intevals of 10
        for i in range(0,h+10,10):
            c.create_line([(0, i), (w, i)], tag='grid_line')

        this.c = tk.Canvas(root, height=h, width=w, bg='white')
        this.c.pack(fill=tk.BOTH, expand=True)

        #c.bind('<Configure>', create_grid)

grid = Grid()
root.mainloop()
