'''Nombre, edad y correo y agregar validiendo letras y numeros,
se muestran en la tabla con su clave, al seleccionar un registro de la tabla
se pueda modificar'''

from tkinter import * 
from tkinter import messagebox
from validacionesp2 import Validar 
import numpy as np
from tkinter import ttk
import random 

'''VENTANA, TAMAÑO'''
class Principal():
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        ancho = 500
        alto = 300
        ventana_alto  = self.ven.winfo_screenwidth()
        ventana_ancho = self.ven.winfo_screenheight()
        x = (ventana_alto // 2) - (ancho //2)
        y = (ventana_ancho // 2) - (alto //2)
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")
        self.cont = 0
        self.bandera = False
        self.renglon =-1
        self.index = 0

    '''INTERFAZ DE VENTANA'''
    def inicio(self):
        
        Label(self.ven, text= "Nombre").place(x=10, y=10)
        self.nombre = Entry(self.ven, fg="blue")
        self.nombre.place(x=10, y=40, width=100)
       
        Label(self.ven, text= "Edad").place(x=130, y=10)
        self.edad = Entry(self.ven, fg="green")
        self.edad.place(x=125, y=40, width=100)
        
        Label(self.ven, text= "Correo").place(x=250, y=10)
        self.correo = Entry(self.ven, fg="purple")
        self.correo.place(x=240, y=40, width=100)

        Button(self.ven, text="Agregar", command=self.agregarElemento, width=10).place(x=380, y=50,
                                                                               width=100, height=30)
        Button(self.ven, text="Eliminar", command=self.Eliminar, width=10).place(x=380, y=90,
                                                                               width=100, height=30)
        Button(self.ven, text="Seleccionar", command=self.validarCaja, width=10).place(x=380, y=130,
                                                                               width=100, height=30)
        #DATAGRID
        columnas = ("Clave","Nombre","Correo","Edad")
        self.tabla = ttk.Treeview(self.ven, columns = columnas, show = "headings")
        self.tabla.place(x=10, y=100, width=350, height=190)

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=30)
        scrolly = ttk.Scrollbar(self.ven, orient="vertical", command= self.tabla.yview)
        scrollx = ttk.Scrollbar(self.ven, orient="horizontal",command= self.tabla.xview)
        scrolly.place(x=360, y=90,height=200)
        scrollx.place(x=10, y=280, width=350)
        
        self.ven.mainloop()

    def validarCaja(self):
        self.renglon = self.tabla.selection()
        #Obtener la fila seleccionada de la tabla
        #Get the selected row from the table
        if not self.renglon:
            messagebox.showerror("Error","Elije una fila")
        #Validar si no se seleccionó nada
        #Validate if nothing was selected
        else:
            valores= self.tabla.item(self.renglon, "values")
            print(valores)
            #Obtener valores de la fila seleccionada
            #Get values from selected row
            self.index = valores[0]
            self.index =self.index[:len(self.index)-2]
            print(self.index)
            #Extraer la clave sin los últimos dos caracteres
            #Extract the key without the last two characters
            self.nombre.insert(0,valores[1])
            self.edad.insert(0,valores[3])
            self.correo.insert(0,valores[2])
            #Cargar los datos en las cajas de texto
            #Load row data into entry boxes
            self.bandera = True
            #Activar modo edición
            #Activate edit mode

    def agregarElemento(self):
        if(len(self.nombre.get())==0 or len(self.edad.get())==0 or len(self.correo.get())==0):
            messagebox.showerror("Error","Faltan Datos")
        #Validar que no haya campos vacíos/Validate fields are not empty
        else:
            nombre = self.nombre.get()
            edad  =self.edad.get()
            correo = self.correo.get()
            if self.bandera == False:
            #Contador que aumenta cada registro/Global row counter
             self.cont += 1
             clave = str(self.cont)+str(random.randint(1,100))+self.nombre.get()[0:2].upper()
             #Generar clave: número + random + 2 letras del nombre
             #Generate key: number + random + first 2 letters of name
             self.tabla.insert("", "end", values=(clave,nombre,correo,edad))
             #Insertar fila nueva/Insert new row
             self.nombre.delete(0,END)
             self.edad.delete(0,END)
             self.correo.delete(0,END)
             #Limpiar campos/Clear fields
            else:
                clave = self.index+self.nombre.get()[0:2]
                #Generar la nueva clave con las iniciales del nombre
                #Generate edited key with new initials
                print("Modo de edicion activado")
                self.tabla.item(self.renglon,value = (clave, nombre, edad, correo))
                #Actualizar la fila seleccionada
                #Update selected row
                self.nombre.delete(0,END)
                self.edad.delete(0,END)
                self.correo.delete(0,END)
                #Limpiar entradas y restaurar modo agregar
                #Clear fields and restore add mode
                self.bandera = False
                self.renglon = -1
                messagebox.showinfo("Correcto","Datos Actualizados")

    def Eliminar(self):
        renglon = self.tabla.selection()
        #Obtener la fila seleccionada/Get selected row
        if not renglon:
            messagebox.showerror("Error","Elije una fila")
        else:
            self.tabla.delete(renglon)
            messagebox.showinfo("Correcto","Fila Eliminada")
            #Eliminar la fila/Delete row
if __name__=='__main__':
    app= Principal()
    app.inicio()