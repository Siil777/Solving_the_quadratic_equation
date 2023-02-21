from tkinter import*
from tkinter import ttk  
from tkinter import ttk
import tkinter as tk
import math





def solve():
   a=float(E1.get())
   b=float(E2.get())
   c=float(E3.get())

   D = b**2 - 4 * a * c
   if D<0:
       
       
        result.config(text="Уравнение не имеет действительных корней")
        
   else:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        result.config(text=f"Корни уравнения:\n x1 = {x1}\n x2 = {x2}")

 
        
   
       

window=tk.Tk()#responds for formation 
window.title('The first window') 
window.geometry('600x300')# change size












lbl=tk.Label(window,text='Решение квадратного уровнения', font='Arial 20', bg="lightblue")
lbl1=tk.Label(window,text='x**2+')
lbl2=tk.Label(window,text='x+')
lbl3=tk.Label(window,text='=0')
result = tk.Label( text="Решение", bg="yellow", width=25, height=4, font=("Arial", 16))
#lbl.pack(pady=10)

#E1 = Entry(window, bd =5)
#E1.pack(side = RIGHT)

#ent.pack(side="left", padx="10")
#E1=Entry(window,fg='black', bg='paleturquoise' ,) #Text box
#E2=Entry(window,fg='black', bg='#32a852' ,) #Text box
#E3=Entry

E1 =tk.Entry(window,  width=10, bg="lightblue")
#E1.pack(side="left", padx=10)


E2 =tk.Entry(window,  width=10, bg="lightblue")
#E2.pack(side="right", padx=10)

E3=tk.Entry(window, width=10, bg="lightblue")

btn=Button(window, text='Решить',font='Arial 20', fg='black', bg='#32a852', command=solve)


E1.grid(row=1,column=0)
lbl1.grid(row=1, column=1)
E2.grid(row=1, column=2)
lbl2.grid(row=1,column=3)
E3.grid(row=1, column=4)
lbl3.grid(row=1, column=5)
lbl.grid(row=0,column=0, columnspan=10)
btn.grid(row=1, column=6, )
result.grid(row=4, column=0,columnspan=10)








window.mainloop() # start the window




















