from tkinter import * 
root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

class keyPresser():  
    def fred(self,event): 
        print('Down arrow key pressed')

    def __init__(self):       
        canvas.bind("<Down>", self.fred)
        canvas.focus()
        canvas.pack()
 
mm = keyPresser()
root.mainloop()

