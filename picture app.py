from tkinter import *
from PIL import ImageTk,Image
root = Tk()

rasm = ImageTk.PhotoImage(Image.open("001.jpg"))
rasm2 = ImageTk.PhotoImage(Image.open("002.jpg"))
rasm3 = ImageTk.PhotoImage(Image.open("003.jpg"))
rasm4 = ImageTk.PhotoImage(Image.open("004.jpg"))
rasm5 = ImageTk.PhotoImage(Image.open("005.jpg"))

rasmlar = [rasm,rasm2,rasm3,rasm4,rasm5]

label = Label(image=rasm)
label.grid(row=0,column=0,columnspan=3)

def next(numb):
    global label
    global button_next
    global button_pre
    label.grid_forget()
    label = Label(image=rasmlar[numb+1])
    button_pre = Button(root, text="<<",command=lambda: pre(numb-1))
    button_pre.grid(row=1, column=0)
    button_next = Button(root, text=">>", command=lambda: next(numb+1))
    button_next.grid(row=1, column=2)
    label.grid(row=0, column=0, columnspan=3)
    if numb == 3:
        button_next = Button(root, text=">>", state = DISABLED)
        button_next.grid(row=1, column=2)


def pre(numb):
    global label
    global button_next
    global button_pre
    label.grid_forget()
    label.grid_forget()
    label = Label(image=rasmlar[numb - 1])
    button_pre = Button(root, text="<<", command=lambda: pre(numb - 1))
    button_pre.grid(row=1, column=0)
    button_next = Button(root, text=">>", command=lambda: next(numb + 1))
    button_next.grid(row=1, column=2)
    label.grid(row=0, column=0, columnspan=3)
    if numb == 1:
        button_pre = Button(root, text="<<", state = DISABLED)
        button_pre.grid(row=1, column=0)

button = Button(root,text="exit",command = root.quit)
button.grid(row=1,column=1)

button_next = Button(root,text=">>",command=lambda : next(2))
button_next.grid(row=1,column=2)

button_pre = Button(root,text="<<")
button_pre.grid(row=1,column=0)

root.mainloop()