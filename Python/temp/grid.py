import tkinter as tk
root = tk.Tk()
 
class GeekforGeeks: 
	geek = "" 

	# default constructor 
	def __init__(self): 
		self.geek = "GeekforGeeks"
        self.width = 240
        self.height = 360
		
	# a method for printing data members 
	def print_Geek(self): 
		print(self.geek) 


# creating object of the class 
obj = GeekforGeeks() 

# calling the instance method using the object obj 
obj.print_Geek() 

