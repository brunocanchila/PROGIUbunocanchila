import tkinter as tk
from tkinter import messagebox

def registrar():
    nombre = cnombre.get()
    apellido = capellido.get()
    edad = cedad.get()
    direccion = cdireccion.get()
    telefono = ctelefono.get()
    sexo = Csexo.get()
    ciudad = listbox_ciudad.get(listbox_ciudad.curselection())

    datos = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nSexo: {sexo}\nCiudad: {ciudad}"
    messagebox.showinfo("Datos registrados", datos)

ventana = tk.Tk()
ventana.title("Splavia Unitecnar")

lnombre = tk.Label(ventana, text="Nombre:")
lnombre.grid(row=0, column=0)
cnombre = tk.Entry(ventana)
cnombre.grid(row=0, column=1)

lpellido = tk.Label(ventana, text="Apellido:")
lpellido.grid(row=1, column=0)
capellido = tk.Entry(ventana)
capellido.grid(row=1, column=1)

ledad = tk.Label(ventana, text="Edad:")
ledad.grid(row=2, column=0)
cedad = tk.Entry(ventana)
cedad.grid(row=2, column=1)

ldireccion = tk.Label(ventana, text="Dirección:")
ldireccion.grid(row=3, column=0)
cdireccion = tk.Entry(ventana)
cdireccion.grid(row=3, column=1)

ltelefono = tk.Label(ventana, text="Teléfono:")
ltelefono.grid(row=4, column=0)
ctelefono = tk.Entry(ventana)
ctelefono.grid(row=4, column=1)

lsexo = tk.Label(ventana, text="Sexo:")
lsexo.grid(row=5, column=0)
Csexo = tk.StringVar()
rmasculino = tk.Radiobutton(ventana, text="Masculino", variable=Csexo, value="Masculino")
rmasculino.grid(row=5, column=1)
rfemenino = tk.Radiobutton(ventana, text="Femenino", variable=Csexo, value="Femenino")
rfemenino.grid(row=5, column=2)

lciudad = tk.Label(ventana, text="Ciudad:")
lciudad.grid(row=6, column=0)
listbox_ciudad = tk.Listbox(ventana)
listbox_ciudad.grid(row=6, column=1)
ciudades = ["Cartagena", "Barranquilla", "Bogota"] 
for ciudad in ciudades:
    listbox_ciudad.insert(tk.END, ciudad)

boton_registrar = tk.Button(ventana, text="Registrar", command=registrar)
boton_registrar.grid(row=7, column=1)

ventana.mainloop()