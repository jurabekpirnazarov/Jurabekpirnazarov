from tkinter import *
root =Tk()
root.title('calculator')
en = Entry(root,width=30,borderwidth=5,justify=RIGHT)
en.grid(row=0,column=1,columnspan=4)

def ent_numb(aa):
    qiymat = en.get()+str(aa)
    en.delete(0, END)
    en.insert(0, qiymat)
#amallar
def plus():
    p_amal= en.get()
    global b_raqam
    global math
    math = "plus"
    b_raqam = int(p_amal)
    p2_amal = en.delete(0,END)

def minus():
    p_amal = en.get()
    global b_raqam
    global math
    math = "minus"
    b_raqam = int(p_amal)
    p2_amal = en.delete(0, END)
def kop():
    p_amal = en.get()
    global b_raqam
    global math
    math = "kop"
    b_raqam = int(p_amal)
    p2_amal = en.delete(0, END)
def bolish():
    p_amal = en.get()
    global b_raqam
    global math
    math = "bolish"
    b_raqam = int(p_amal)
    p2_amal = en.delete(0, END)
def teng():
    ikki_raqam = en.get()
    en.delete(0,END)
    if math == "bolish":
        en.insert(0,b_raqam / int(ikki_raqam))
    elif math == "kop":
        en.insert(0,b_raqam * int(ikki_raqam))
    elif math == "plus":
        en.insert(0,b_raqam + int(ikki_raqam))
    elif math == "minus":
        en.insert(0,b_raqam - int(ikki_raqam))


#knopkalar
b1 = Button(root,text='1',padx=15,pady=10, command=lambda:ent_numb(1))
b2 = Button(root,text='2',padx=15,pady=10, command=lambda:ent_numb(2))
b3 = Button(root,text='3',padx=15,pady=10, command=lambda:ent_numb(3))
b4 = Button(root,text='4',padx=15,pady=10, command=lambda:ent_numb(4))
b5 = Button(root,text='5',padx=15,pady=10, command=lambda:ent_numb(5))
b6 = Button(root,text='6',padx=15,pady=10, command=lambda:ent_numb(6))
b7 = Button(root,text='7',padx=15,pady=10, command=lambda:ent_numb(7))
b8 = Button(root,text='8',padx=15,pady=10, command=lambda:ent_numb(8))
b9 = Button(root,text='9',padx=15,pady=10, command=lambda:ent_numb(9))
b0 = Button(root,text='0',padx=15,pady=10, command=lambda:ent_numb(0))

b_plus = Button(root,text='+',padx=15,pady=10,command = plus)
b_minus = Button(root,text='-',padx=15,pady=10, command = minus )
b_kop = Button(root,text='*',padx=15,pady=10,command = kop)
b_bol = Button(root,text='/',padx=15,pady=10,command = bolish)
b_teng = Button(root,text='=',padx=13,pady=20,command=teng)



b1.grid(row=1,column=1)
b2.grid(row=1,column=2)
b3.grid(row=1,column=3)

b4.grid(row=2,column=1)
b5.grid(row=2,column=2)
b6.grid(row=2,column=3)

b7.grid(row=3,column=1)
b8.grid(row=3,column=2)
b9.grid(row=3,column=3)

b0.grid(row=4,column=2)
b_plus.grid(row=4,column=1)
b_minus.grid(row=4,column=3)
b_kop.grid(row=2,column=4)
b_bol.grid(row=1,column=4)
b_teng.grid(row=4,column=4,rowspan=4)


root.mainloop()