from Tkinter import *

def Sumar():
    varres.set( "La Suma es : " + str( float(vartxt1.get()) + float(vartxt2.get())))

ventana = Frame(height=250,width=500)
ventana.pack(padx=5,pady=5)

vartxt1 = StringVar()
lblNum1=Label(text="Numero 1: ").place(x=30,y=40)
txt1 = Entry(ventana,textvariable=vartxt1).place(x=100,y=35)
vartxt2 = StringVar()
lblNum1=Label(text="Numero 2: ").place(x=30,y=80)
txt2 = Entry(ventana,textvariable=vartxt2).place(x=100,y=75)


varres=StringVar()
txtres=Label(textvariable=varres).place(x=28,y=145)


bsum = Button(ventana,command=Sumar,text="Calcular",padx=42,pady=5).place(x=300,y=50)

ventana.mainloop()
