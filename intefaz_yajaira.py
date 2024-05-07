from tkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox

ventana = Tk()

ventana.title = "LOGIN"
ventana.geometry("800x500")
ventana.configure(background="light blue")
ventana.resizable(FALSE, FALSE)


frame1 = Frame(ventana,bg="white")
frame2 = Frame(ventana,bg="purple")

imagen = Image.open("D:\descargas D\logo tecnar.png")
imagen = imagen.resize((300,300))
imagen = ImageTk.PhotoImage(imagen)
label = Label(image=imagen,background="yellow")
label.place(x=60,y=100)

frame1.place(x=0,y=0,width=400,height=800)
frame2.place(x=400,y=0,width=400,height=800)

titulo = Label(ventana, text="Inicio Sesion", bg= "purple",font= "helvetica 14")
titulo.place(x=500, y=80, width=200)


usuario = Label(ventana, text= "usuario: ", bg="purple",font= "helvetica 14")
usuario.place(x=410, y= 140, width=200)
medidas1= Entry(ventana, bg="white",bd= 3)
medidas1.place(x= 600, y=140,width=120)

contraseña = Label(ventana, text= "contraseña: ", bg="purple",font= "helvetica 14")
contraseña.place(x= 420, y=200, width=200)
medidas2= Entry(ventana, width=30, bd=3)
medidas2.place(x=600, y=200, width= 120)

def iniciar():
    messagebox.showinfo("","SESION INICIADA")

boton_sesion = Button(ventana,background= "purple",text="INGRESAR",font= "helvetica 12",command=iniciar)
boton_sesion.place(x=550,y=300,width= 100)


ventana.mainloop()