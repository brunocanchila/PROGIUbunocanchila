import tkinter as tk
from tkinter import messagebox

def ingresar():
    usuario = usuario_entry.get()
    clave = clave_entry.get()
    if usuario == "bruno" and clave == "211004":
        messagebox.showinfo("inicio de sesion", "iniciaste sesion")
    else:
        messagebox.showerror("error", "usuario o contraseña incorrecta")     

ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("800x500")

frame_izquierdo = tk.Frame(ventana, width=200, height=200, bg="grey")
frame_izquierdo.pack(side="left", fill="both", expand=True)
frame_derecho = tk.Frame(ventana, width=200, height=200)
frame_derecho.pack(side="right", fill="both", expand=True)



titulo_label = tk.Label(frame_derecho, text="Inicio de Sesión", font=("Arial", 14))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

usuario_label = tk.Label(frame_derecho, text="Usuario:")
usuario_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

usuario_entry = tk.Entry(frame_derecho)
usuario_entry.grid(row=1, column=1, padx=10, pady=5)

clave_label = tk.Label(frame_derecho, text="Contraseña:")
clave_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

clave_entry = tk.Entry(frame_derecho, show="*") 
clave_entry.grid(row=2, column=1, padx=10, pady=5)

boton_ingresar = tk.Button(frame_derecho, text="Ingresar", command=ingresar)
boton_ingresar.grid(row=3, column=1, columnspan=3, pady=10)


ventana.mainloop()