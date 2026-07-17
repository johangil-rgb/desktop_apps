from tkinter import *
from tkinter import messagebox

# ventana pincipal de la desktop app
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas Guanentá")

# tamaño de la ventana 
ventana_principal.geometry("500x500")

# color de la ventana 
ventana_principal.configure(bg="black")

# deshabilitar boton de maximisar 
ventana_principal.resizable(0,0)

#-------------------------
#frame entrada de datos
#-------------------------

Frame_entrada = Frame(ventana_principal)
Frame_entrada.config(bg="green", width=480, height=240)
Frame_entrada.place(x=10, y=10)

# agregamos una images al frane
escudo = PhotoImage(file="escudoColegio.png")
lb_escudo= Label(Frame_entrada, image=escudo)
lb_escudo.place(x=10, y=20)

#---------------------
#frame operaciones
#---------------------
Frame_operaciones = Frame(ventana_principal)
Frame_operaciones.config(bg="green", width=480, height=120)
Frame_operaciones.place(x=10,y=260)

#---------------------
#frame resultados
#---------------------
Frame_operaciones = Frame(ventana_principal)
Frame_operaciones.config(bg="green", width=480, height=100)
Frame_operaciones.place(x=10,y=390)

#  blucle principal
ventana_principal.mainloop()