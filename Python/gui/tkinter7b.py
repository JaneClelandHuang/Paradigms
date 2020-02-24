from tkinter import * 
root = Tk()


class keyPresser():  
    def handle_down_key(self,event):
        self.canvas.focus_set()                
        print('Down arrow key pressed')

    def __init__(self):   
        self.canvas = Canvas(root, width=400, height=400)
        self.rectangle = self.canvas.create_rectangle( 
            0, 0, 20, 20, fill = "black")
        self.canvas.bind("<Down>", self.handle_down_key)
        self.canvas.focus()
        self.canvas.pack()
        print("Hello")
 
mm = keyPresser()
root.mainloop()

