from tkinter import *
tkroot = Tk()

class myClass():
    def onDownArrowKey(): 
        print('Down arrow key pressed')

    def __init__(self):   
        print("Starting up the class")    
        labelfont = ('courier', 20, 'bold')                
        widget = Label(tkroot, text='Testing arrow keys')
        widget.config(bg='gray', font=labelfont)            
        widget.config(height=5, width=20)                  
        widget.pack(expand=YES, fill=BOTH)
        widget.bind('<Down>',self.onDownArrowKey)
        #widget.focus()  
                                
tkroot.title('Click Me')
myc = myClass()
tkroot.mainloop()

