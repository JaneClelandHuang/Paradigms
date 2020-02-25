import tkinter as tk

class Grid:
    def __init__(self, master):
        self.master = master
        self.master.title("Lines")
        #self.canvas = tk.Canvas(self.master)
        self.height = 360 
        self.width = 240 
        self.canvas = tk.Canvas(self.master)
        self.drawGrid()
        self.canvas.pack()
    def drawGrid(self):
        # Creates all vertical lines at intervals of 100
        for i in range(0, self.width+10, 10):
            self.canvas.create_line([(i, 0), (i, self.height)], tag='grid_line')

        # Creates all horizontal lines at intervals of 100
        for i in range(0, self.height+10, 10):
            canvas.create_line([(0, i), (self.width, i)], tag='grid_line')
        #self.canvas.create_line(15, 25, 200, 25)
        #self.canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        #self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        
class Window1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow)

class Window2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): #run mainloop 
    root = tk.Tk()
    app = Grid(root)
    root.mainloop()

if __name__ == '__main__':
    main()
