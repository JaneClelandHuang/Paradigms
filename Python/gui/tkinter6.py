import tkinter as tk

app = tk.Tk()
app.geometry("200x100")
app.bind('<Return>', print("Hello"))

app.mainloop()