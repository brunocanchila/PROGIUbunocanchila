import tkinter as tk

ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Splavia Unitecnar", bg="RoyalBlue4", fg="pink", font=("Times New Roman", 22), width=25, height=5, anchor="n")
etiqueta.pack()

ventana.geometry("400x200")
usuario = tk.Entry(ventana, text="usuario", width="10", fg="RoyalBlue4", font=("Bahnchrift Light", 15))
usuario = tk.Label(ventana, text="usuario", width="10", bg="RoyalBlue", fg="pink",   font=("Bahnchrift Light", 15))
usuario.place(x=210, y=90)
usuario.place(x=50, y=90)

ventana.geometry("400x200")
contraseña1 = tk.Label(ventana, text="contraseña", width="10", bg="RoyalBlue", fg="pink",   font=("Bahnchrift Light", 15))
contraseña1.place(x=210, y=90)
contraseña = tk.Entry(ventana, text="contraseña", width="10", fg="gray", font=("Bahnchrift Light", 15))

boton1 = tk.Button(ventana, text="Acceder", command="cambiar_texto", bg="white", relief="raised", fg="black", width=50, height=5, font=("Times New Roman", 15))
boton1.pack()

ventana.mainloop()