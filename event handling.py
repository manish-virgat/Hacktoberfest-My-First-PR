from tkinter import *
root = Tk()
root.title("Event Handling")
root.geometry("300x300")
def left(event):
    print("You have clicked left button")
def middle(event):
    print("You have clicked middle button")
def right(event):
     print("You have clicked right button")
frame = Frame(root, width = 350 , height = 450)
frame.bind ("<Button-1>",left)
frame.bind ("<Button-2>" ,middle)
frame.bind ("<Button-3>",right )
frame.pack()
root.mainloop()
