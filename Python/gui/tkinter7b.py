# Demonstrates the arrow keys.
# Click on the widget first to get focus.
#widget.focus() doesn't work

from tkinter import * 
root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

class keyPresser():
     
    def showPosEvent(event):
        print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))
     
    def onUpArrowKey(event): 
        print('Up arrow key pressed')

    def onDownArrowKey(event): 
        canvas.move(self.rectangle,20,20)
        print('Down arrow key pressed')

    def onLeftArrowKey(event): 
        print('Left arrow key pressed')

    def print_event(self, event): 
        print(event.type) 

    def __init__(self):       
        self.width = 20
        self.height = 20
        self.rectangle = canvas.create_rectangle( 
            0, 0, 20, 20, fill = "black")
        # Bind keypress events to methods
        canvas.bind("<Up>", self.print_event)# Note the new binding
        canvas.bind("<Down>", self.print_event) # Another new binding
        canvas.pack() 
 
# Get an instance of the MouseMover object
mm = keyPresser()

root.mainloop()

