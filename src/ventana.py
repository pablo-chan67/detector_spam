import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "¡Boton presionado!")

ventana = tk.Tk()
ventana.title("Ventana simple")


label = tk.Label(ventana, text = "presiona el boton para ver un mensaje")
label.pack(pady=10)

boton = tk.Button(ventana, text = "Haz click aqui", command=mostrar_mensaje)
boton.pack()



ventana.mainloop()
