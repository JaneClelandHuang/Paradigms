# Demonstrates the arrow keys.
# Click on the widget first to get focus.
#widget.focus() doesn't work

from tkinter import *
tkroot = Tk()

def onUpArrowKey(event): 
    widget = event.widget 
    print('Up arrow key pressed')

class myClass:
    def showPosEvent(event):
        print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))
     
    #def onUpArrowKey(): 
    #    widget = event.widget 
    #   print('Up arrow key pressed')

    def onDownArrowKey(): 
        print('Down arrow key pressed')

    def onLeftArrowKey(event): 
        print('Left arrow key pressed')
         
    def __init__(self):    
        labelfont = ('courier', 20, 'bold')                
        widget = Label(tkroot, text='Testing arrow keys')
        widget.config(bg='gray', font=labelfont)            
        widget.config(height=5, width=20)                  
        widget.pack(expand=YES, fill=BOTH)

        widget.bind('<Up>',onUpArrowKey)   
        widget.bind('<Down>',self.onDownArrowKey)
        widget.bind('<Left>',self.onLeftArrowKey)
        widget.focus()  
                                
tkroot.title('Click Me')
tkroot.mainloop()
myc = myClass()
