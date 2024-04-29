import tkinter as tk

def registrar():
    LframeNombre = tk.Label(jframe, text= cnombre.get())
    LframeNombre.pack()
    LframeNombre = tk.Label(jframe, text= capellido.get())
    LframeNombre.pack()
    LframeNombre = tk.Label(jframe, text= cedad.get())
    LframeNombre.pack()
    
ventana = tk.Tk()
ventana.title("TECNAR APP")
ventana.geometry("800x600")
ventana.resizable(True, True)


lnombre = tk.Label(ventana,text = "NOMBRE:")
lnombre.place(x=5, y=10)
cnombre = tk.Entry(ventana, width=40)
cnombre.place(x=80, y=10)


lapellido = tk.Label(ventana,text = "APELLIDO:")
lapellido.place(x=5, y=40)
capellido = tk.Entry(ventana, width=40)
capellido.place(x=80, y=40)


ledad = tk.Label(ventana,text = "EDAD:")
ledad.place(x=5, y=70)
cedad = tk.Entry(ventana,width=40)
cedad.place(x=80, y=70)

bregistrar =tk.Button(ventana, text= "REGISTRAR", command=registrar)
bregistrar.place(x=100, y=100)

jframe = tk.Frame(ventana, width=300, height=150, relief="raised", bd=1)
jframe.place(x=20, y=130)

ventana.mainloop()


