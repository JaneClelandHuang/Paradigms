import tkinter as tk

def create_grid(event=None):
    w = 180 # c.winfo_width() # Get current width of canvas
    h = 360 #c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 10
    #for i in range(0, w, 10):
    for i in range(0,180,10):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 10
    for i in range(0,360,10):
        c.create_line([(0, i), (w, i)], tag='grid_line')

root = tk.Tk()

c = tk.Canvas(root, height=200, width=100, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)

root.mainloop()
