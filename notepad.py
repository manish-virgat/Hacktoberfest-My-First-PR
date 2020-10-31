from tkinter import *
import tkinter.messagebox
import tkinter.scrolledtext as ScrolledText
root = Tk()
root.title("menus")
root.geometry("300x300")
def res():
    root.geometry("500x500")
def btn():
    root.geometry("300x300")
    print("back to normal form")
def custom_quit():
    answer = tkinter.messagebox.askokcancel("are you sure you want to quit?")
    if(answer):
        print("you have quit successfully")
        quit()
def cut():
    textarea.event_generate(("<<cut>>"))
def copy():
    textarea.event_generate(("<<copy>>"))
def paste():
    textarea.event_generate(("<<paste>>"))

textarea = ScrolledText.ScrolledText(root,width=100,height=100)
textarea.pack()
menu1 = Menu(root)
root.config(menu=menu1)
submenu= Menu(menu1)
menu1.add_cascade(label="file",menu=submenu)
submenu.add_command(label="filename")
submenu.add_command(label="new project")
submenu.add_command(label="save as")
submenu.add_command(label="save")
submenu.add_command(label="settings")
submenu.add_command(label="exit",command=custom_quit)
submenu2 = Menu(menu1)
menu1.add_cascade(label="edit",menu=submenu2)
submenu2.add_command(label="resizing window",command=res)
submenu2.add_command(label="back to normal",command=btn)
submenu2.add_command(label="cut",command=cut)
submenu2.add_command(label="copy",command=copy)
submenu2.add_command(label="paste",command=paste)
submenu3 = Menu(menu1)
menu1.add_cascade(label="view")
submenu4 = Menu(menu1)
menu1.add_cascade(label="navigate")
submenu5 = Menu(menu1)
menu1.add_cascade(label="code")
submenu6 = Menu(menu1)
menu1.add_cascade(label="help")
root.mainloop()



