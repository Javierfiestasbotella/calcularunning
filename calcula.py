# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import tkinter as tk


def nkm2(km):
  s=3600/km/60
  s=round(s,1)
  return s


def nkm():
  try:
    s=3600/km.get()/60
    s=round(s,1)
    result.set(s)
    km.set(0)
  except ZeroDivisionError:
    messagebox.showinfo(message='No se puede dicivir por cero',title='Atencion!!')

def kmin():
  try:
    s=60/min.get()
    s=round(s,1)
    result.set(s)
    min.set(0)
  except ZeroDivisionError:
    messagebox.showinfo(message='No se puede dicivir por cero',title='Atencion!!')
  
def tabla():
  velocidades=[8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16,16.5,17,17.5,18,18.5,19,19.5,20,20.5]
  result=[]
  for i in velocidades:
    r=nkm2(i)
    result.append(round(r,1))
  for i,j in zip(velocidades,result):
    listado='{} km/h --------- {} min/km'.format(i,j)
  messagebox.showinfo(message='''    
8 km/h --------- 7.5 min/km
8.5 km/h --------- 7.1 min/km
9 km/h --------- 6.7 min/km
9.5 km/h --------- 6.3 min/km
10 km/h --------- 6.0 min/km
10.5 km/h --------- 5.7 min/km
11 km/h --------- 5.5 min/km
11.5 km/h --------- 5.2 min/km
12 km/h --------- 5.0 min/km
12.5 km/h --------- 4.8 min/km
13 km/h --------- 4.6 min/km
13.5 km/h --------- 4.4 min/km
14 km/h --------- 4.3 min/km
14.5 km/h --------- 4.1 min/km
15 km/h --------- 4.0 min/km
15.5 km/h --------- 3.9 min/km
16 km/h --------- 3.8 min/km
16.5 km/h --------- 3.6 min/km
17 km/h --------- 3.5 min/km
17.5 km/h --------- 3.4 min/km
18 km/h --------- 3.3 min/km
18.5 km/h --------- 3.2 min/km
19 km/h --------- 3.2 min/km
19.5 km/h --------- 3.1 min/km
20 km/h --------- 3.0 min/km
20.5 km/h --------- 2.9 min/km
20.5 km/h --------- 2.9 min/km
''',title='Tabla Referencias')  

def media():
  try:
    v=km.get()/min.get()
    v=round(v,1)
    result.set(v)
    km.set(0)
    min.set(0)
  except ZeroDivisionError:
    messagebox.showinfo(message='No se puede dicivir por cero',title='Atencion!!')

raiz=Tk()

result=IntVar()
velocity=IntVar()
min=IntVar()
km=IntVar()

nombre_usuario="Cuestionario"
raiz.geometry("280x450+0+0")
raiz.iconbitmap("running/rubik.ico")
raiz.title('Calculadora Silvia García')
        
fondo=PhotoImage(file="running/r.png",width=253,height=248)
lblFondo=Label(raiz,image=fondo).place(x=0, y=220)

etiqueta_id=Label(raiz,text="Km/h").place(x=30, y=20) 
espacio0=Entry(raiz,justify=RIGHT,textvariable=km).place(x=130, y=20,)
        
etiqueta_nombre=Label(raiz,text="min/Km u horas").place(x=30, y=50)
espacio1=Entry(raiz,justify=RIGHT,textvariable=min).place(x=130, y=50)
        
etiqueta_contraseña=Label(raiz,text="Velocidad").place(x=30, y=90)
espacio2=Entry(raiz,justify=RIGHT,textvariable=velocity).place(x=130, y=90)
        
etiqueta_apellidos=Label(raiz,text="Resultado").place(x=30, y=130)
espacio3=Entry(raiz,justify=RIGHT,textvariable=result).place(x=130, y=130)

boton7=Button(raiz,text="Km/h a min",command=nkm).place(x=20,y=160)
boton8=Button(raiz,text="min a km/h",command=kmin).place(x=150,y=160)
boton9=Button(raiz,text="velocidad media",command=media).place(x=75,y=195)
boton10=Button(raiz,text="Tabla",command=tabla).place(x=75,y=0)


if __name__ == '__main__': raiz.mainloop()
