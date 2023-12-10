import tkinter as tk
from tkinter import ttk

def seleccionaElemento(event):
    seleccionado=arbol.focus()
    print(seleccionado)
    valores=arbol.item(seleccionado, 'values')
    print(valores)#obtengo en consola el valor que selecciono

def leerValor():
    print("Leido:")
    print(entrada.get("1.0", tk.END)) #obtengo/leo el valor de la entrada

def ponerValor():
    print("Vaciado")
    entrada.delete("1.0", tk.END) #borro todo lo que hay
    #print(entrada.insert(0,"new")) #pongo valor

raiz = tk.Tk()
raiz.title("Mi Agenda")
estilo=ttk.Style()

#Welcome
estilo.configure('bienvenida.TLabel', font=('Calibri', 15), padding=10)
etiqueta1=ttk.Label(raiz, text="Bienvenidx a tu agenda electrónica", style='bienvenida.TLabel')
etiqueta1.pack(padx=5, pady=5)

#tabla
arbol = ttk.Treeview(raiz,columns=('nombre','apellidos','email'), height=1)
arbol.heading("nombre",text="Nombre")
arbol.heading("apellidos",text="Apellidos")
arbol.heading("email",text="Correo electrónico")
arbol.insert('','0',values=("Mickey","Mouse","mickey.mouse@disney.com"))
#escuchador
arbol.pack(padx=10, pady=10)
arbol.bind('<<TreeviewSelect>>', seleccionaElemento)
# Oculta la primera columna
arbol['show'] = 'headings'
arbol.column("#0", width=0, stretch=tk.NO)  

#escribe
estilo.configure('escribe.TLabel', padding=10, foreground='#de2f9e', font=('Comic Sans', 10)) 
etiqueta1=ttk.Label(raiz, text="Escribe:", style='escribe.TLabel')
etiqueta1.pack(padx=5, pady=5)

#entrada de datos
entrada=tk.Text(raiz, height=10, width=40)
entrada.pack(padx=5, pady=10)

boton=ttk.Button(raiz, text="Leer Dato por consola", command=leerValor)
boton.pack(padx=10, pady=15)

boton2=ttk.Button(raiz, text="Volver a empezar", command=ponerValor)
boton2.pack(padx=10, pady=15)

raiz.mainloop()