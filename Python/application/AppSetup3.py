import tkinter as tk

class Grid:
    def __init__(self, master):
        self.master = master
        self.master.title("Lines")
        self.height = 360 
        self.width = 240 
        self.rectangle_size = 10
        self.canvas = tk.Canvas(width=self.width, height=self.height)
        self.drawGrid()
        self.canvas.pack()
        self.placeMarker(3,4)
        
    def drawGrid(self):
        # Creates all vertical lines at intervals of rectangle_size
        for i in range(0, self.width, self.rectangle_size):
            self.canvas.create_line([(i, 0), (i, self.height)])

        # Creates all horizontal lines at intervals of 10
        for i in range(0, self.height, self.rectangle_size):
            self.canvas.create_line([(0, i), (self.width, i)])
            
    def placeMarker(self,x,y):
        x1 = x * self.rectangle_size
        y1 = y * self.rectangle_size
        self.canvas.create_rectangle(x1,y1, x1+self.rectangle_size, y1+self.rectangle_size, fill="blue")
        self.canvas.pack()
        
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
