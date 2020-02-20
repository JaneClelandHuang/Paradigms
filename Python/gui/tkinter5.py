from tkinter import * 
root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

class MouseMover():
	
    def __init__(self):       
        self.rectangle = canvas.create_rectangle( 
            5, 5, 25, 25, fill = "black")
        self.shape = None
        self.coords = canvas.coords(self.rectangle)
        self.previous = (self.coords[0]+(self.coords[2]/2),self.coords[1]+(self.coords[3]/2))
        canvas.pack() 
        # Bind mouse events to methods
        canvas.bind("<Button-1>", self.select)# Note the new binding
        canvas.bind("<B1-Motion>", self.drag) # Another new binding
        canvas.bind("<Double-Button-1>", self.print_event) 
        canvas.bind("<ButtonRelease-1>", self.print_event) 
 
    def drag(self, event):
        if (self.shape == self.rectangle):
            widget = event.widget
            xc = widget.canvasx(event.x) 
            yc = widget.canvasy(event.y)
            canvas.move(self.rectangle, xc-self.previous[0], yc-self.previous[1])
            self.previous = (xc, yc)
		
    def setSelectedShape(self,xCoord,yCoord,coords):
        if (xCoord < coords[2] and xCoord > coords[0])# and yCoord < coords[3] and yCoord > coords[1])
            self.shape = self.rectangle
        else:
            self.shape = None

    def select(self, event):
        widget = event.widget # Get handle to canvas 
        # Convert screen coordinates to canvas coordinates
        xc = widget.canvasx(event.x) 
        yc = widget.canvasy(event.y)
		setSelectedShape(xc,yc,self.rectangle)
        print((xc, yc, self.rectangle))
	
    def print_event(self, event): 
        position = "(x={}, y={})".format(event.x, event.y) 
        print(event.type, "event", position) 

# Get an instance of the MouseMover object
mm = MouseMover()

root.mainloop()

