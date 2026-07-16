from tkinter import *

# ventana pincipal de la desktop app
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas Guanentá")

# tamaño de la ventana 
ventana_principal.geometry("500x500")

# color de la ventana 
ventana_principal.configure(bg="blue")

# deshabilitar boton de maximisar 
ventana_principal.resizable(0,0)

# agregamos un objeto tipo frame sobre la ventana
Frame_1 = Frame(ventana_principal)
Frame_1.config(bg="blue", width=480, height=240)
Frame_1.place(x=10, y=10)

# agregamos una images al frane
escudo = PhotoImage(file="escudoColegio.png")
lb_escudo= Label(Frame_1, image=escudo)
lb_escudo.place(x=10, y=20)

#  blucle principal
ventana_principal.mainloop()