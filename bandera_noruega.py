from tkinter import *

# ventana pincipal de la desktop app
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Bandera de Noruega")

# tamaño de la ventana 
ventana_principal.geometry("1000x650")

# color de la ventana (fondo blanco)
ventana_principal.configure(bg="#F4FFFD")

# deshabilitar boton de maximisar 
ventana_principal.resizable(0,0)

# ---- medidas de la cruz ----
# banda vertical total (blanco+azul+blanco): x = 320 a 420
# banda horizontal total (blanco+azul+blanco): y = 280 a 380
# el azul queda centrado dentro de esas bandas, dejando 20px de blanco a cada lado

# ---- 4 formas rojas (frames) ----
Frame_rojo_1 = Frame(ventana_principal)
Frame_rojo_1.config(bg="#920D0D", width=320, height=280)
Frame_rojo_1.place(x=0, y=0)

Frame_rojo_2 = Frame(ventana_principal)
Frame_rojo_2.config(bg="#920D0D", width=580, height=280)
Frame_rojo_2.place(x=420, y=0)

Frame_rojo_3 = Frame(ventana_principal)
Frame_rojo_3.config(bg="#920D0D", width=320, height=320)
Frame_rojo_3.place(x=0, y=380)

Frame_rojo_4 = Frame(ventana_principal)
Frame_rojo_4.config(bg="#920D0D", width=580, height=320)
Frame_rojo_4.place(x=420, y=380)

Frame_azul_1 = Frame(ventana_principal)
Frame_azul_1.config(bg="#0044FF", width=60, height=700)
Frame_azul_1.place(x=340, y=0)

Frame_azul_1 = Frame(ventana_principal)
Frame_azul_1.config(bg="#0044FF", width=1000, height=60)
Frame_azul_1.place(x=0, y=300)

#  blucle principal
ventana_principal.mainloop()
