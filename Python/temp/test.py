from tkinter import * 
from random import seed 
from random import randint 
from tkinter import messagebox
seed(1)
value = randint(0,500)
#value = 0 + (num *(1000 -0))
offset = value + 100
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

class MouseMover():

    def __init__(self):       
        self.width = 50     #used to be 400 
        self.height = 50    #used to be 400 
        
        self.rectangle = canvas.create_rectangle( 
            value, value,offset,offset, fill = "black")
        self.circle = canvas.create_oval(0,0,50,50)
        self.shape = None
        self.offset = (0,0) # Position of cursor with respect to the rectangle
        self.circlePosition = canvas.coords(self.circle)
        self.rectPosition = canvas.coords(self.rectangle) 
        self.previous = (self.circlePosition[0]+(self.circlePosition[2]/2),self.circlePosition[1]+(self.circlePosition[3]/2))
        print(self.previous)
        canvas.pack() 
        # Bind mouse events to methods
        canvas.bind("<Button-1>", self.select)# Note the new binding
        canvas.bind("<B1-Motion>", self.drag) # Another new binding
        canvas.bind("<Double-Button-1>", self.print_event) 
        canvas.bind("<ButtonRelease-1>", self.release) 
        canvas.bind("<Up>",self.onUpArrowKey)   
       # canvas.bind('<Down>',self.dragDown)
       # canvas.bind('<Left>',self.dragLeft)
       # canvas.bind('<Right>',self.dragRight)
       # canvas.focus()  
                                        
    def onUpArrowKey(self, event): 
        print('Up arrow key pressed')    def dragUp(self,event):
        print("getss into function")  # currently does not print
        widget = event.widget 
        xc = widget.canvasx(event.x) 
        yc = widget.canvasy(event.y)
        canvas.move(self.circle,0, 10)

        print("in here")

    def drag(self, event):
        #print("Do nothing")
        if (self.shape == self.circle):
            widget = event.widget
            xc = widget.canvasx(event.x) 
            yc = widget.canvasy(event.y)
			
            # Compute offset
            self.offset = (self.previous[0]-xc,self.previous[1]-yc)
            canvas.move(self.circle, xc-self.previous[0], yc-self.previous[1])
            self.previous = (xc, yc)
            print("NEW")
            print(xc)
            print(self.circlePosition[2])
            print(self.circlePosition[0])
            print(yc)
            print(self.circlePosition[3])
            print(self.circlePosition[1])
            print(self.offset[0])
            self.circlePosition[0] = xc-self.width/2#+self.offset[0] #self.rectPosition[0]+xc+self.offset[0]
            self.circlePosition[1] = yc-self.height/2#+self.offset[1] #self.rectPosition[1]+yc+self.offset[1]
            self.circlePosition[2] = self.circlePosition[0]+self.width
            self.circlePosition[3] = self.circlePosition[1]+self.height
                     
          #  tkroot = Tk()
          #  labelfont = ('courier', 20, 'bold')                
          #  widget = Label(tkroot, text='Testing arrow keys')
          #  widget.config(bg='gray', font=labelfont)            
           # widget.config(height=5, width=20)                  
          #  widget.pack(expand=YES, fill=BOTH)

            
            if(self.rectPosition[0] < self.circlePosition[0] < self.circlePosition[2] and self.rectPosition[0] < self.circlePosition[2] <self.rectPosition[2] and self.rectPosition[1] < self.circlePosition[1] < self.rectPosition[3] and self.rectPosition[1] < self.circlePosition[3] < self.rectPosition[3]):

                messagebox.showinfo("WINNER","Cogratulations!")


    def release(self,event):
        if (self.shape == self.circle):
            widget = event.widget
            xc = widget.canvasx(event.x) 
            yc = widget.canvasy(event.y)
            #self.rectPosition[0] = xc+self.offset[0] #self.rectPosition[0]+xc+self.offset[0]
            #self.rectPosition[1] = yc+self.offset[1] #self.rectPosition[1]+yc+self.offset[1]
            #self.rectPosition[2] = self.rectPosition[0]+self.width/2
            #self.rectPosition[3] = self.rectPosition[1]+self.height/2

    def setSelectedShape(self,xCoord,yCoord,circlePosition):
        print("HELLO")
        print(xCoord)
        print(circlePosition[2])
        print(circlePosition[0])
        print(yCoord)
        print(circlePosition[3])
        print(circlePosition[1])

        if (self.circlePosition[0] < xCoord < self.circlePosition[2] and circlePosition[1] < yCoord < circlePosition[3]):
            print("INSIDE SHAPE")
            self.shape = self.circle			
        else:
            self.shape = None
   # def winningGame(self,circlePosition,rectPosition):

    def select(self, event):
        widget = event.widget # Get handle to canvas 
        # Convert screen coordinates to canvas coordinates
        xc = widget.canvasx(event.x) 
        yc = widget.canvasy(event.y)
        self.setSelectedShape(xc,yc,self.circlePosition)
        print((xc, yc, self.circle))
	
    def print_event(self, event): 
        position = "(x={}, y={})".format(event.x, event.y) 
        print(event.type, "event", position) 

# Get an instance of the MouseMover object
mm = MouseMover()

root.mainloop()