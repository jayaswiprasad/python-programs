from tkinter import *
import time

root = Tk()
root.title("Digital Clock")
root.geometry("250x100")

def display_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, display_time)

label = Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

display_time()
root.mainloop()
