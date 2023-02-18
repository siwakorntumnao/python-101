from tkinter import *
from tkinter import ttk
from tkinter import messagebox



GUI= Tk()
GUI.title('โปรเเกรมบันทึกข้อมูล')
GUI.geometry('500x400')


def Button1():
    messagebox.showinfo('ชื่อ','เพชร')
    
B1 = ttk.Button(GUI,text='=ชื่ออะไร',command=Button1)
B1.pack(ipadx=20, ipady=20)


def Button2():
    messagebox.showinfo('อายุ','17')
B1 = ttk.Button(GUI,text='=อายุเท่าไหร', command=Button2)
B1.pack(ipadx=20, ipady=20)


def Button3():
    messagebox.showinfo('อาหาร','fried rice')
B1 = ttk.Button(GUI,text='=ชอบกินไร',command=Button3)
B1.pack(ipadx=20, ipady=20)


def Button4():
    messagebox.showinfo('วิชา','social')
B1 = ttk.Button(GUI,text='=fav subject',command=Button4)
B1.pack(ipadx=20, ipady=20)


def Button5():
    messagebox.showinfo('ระดับ','6')
B1 = ttk.Button(GUI,text='=อยุ่ ม ไร',command=Button5)
B1.pack(ipadx=20, ipady=20)









GUI.mainloop()

