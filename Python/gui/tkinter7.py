from tkinter import *
     
def showPosEvent(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))
     
def onUpArrowKey(event): 
    print('Up arrow key pressed')

def onDownArrowKey(event): 
    print('Down arrow key pressed')
          
tkroot = Tk()
labelfont = ('courier', 20, 'bold')                
widget = Label(tkroot, text='Hello bind world')
widget.config(bg='red', font=labelfont)            
widget.config(height=5, width=20)                  
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Up>',onUpArrowKey)   
widget.bind('<Down>',onDownArrowKey)
widget.focus()                                     
tkroot.title('Click Me')
tkroot.mainloop()
