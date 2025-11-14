'''Nombre, telefono, domicilio, validar letras en nombre y numeros en telefono, 
se agregan en la lista contando su sexo (F/M) y se agrega su clave'''
from tkinter import * 
from tkinter import messagebox
from validacionesp2 import Validar 
import numpy as np

'''VENTANA, TAMAÑO'''
class Principal():
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        ancho = 350
        alto = 250
        ventana_alto  = self.ven.winfo_screenwidth()
        ventana_ancho = self.ven.winfo_screenheight()
        x = (ventana_alto // 2) - (ancho //2)
        y = (ventana_ancho // 2) - (alto //2)
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")
        

    def quitar_placeholder1(self,event):
        if self.nombre.get() == self.placeholder1:
            self.nombre.delete(0,END)
            self.nombre.config(fg="black")
    def quitar_placeholder2(self,event):
        if self.telefono.get() == self.placeholder2:
            self.telefono.delete(0,END)
            self.telefono.config(fg="black")
    def quitar_placeholder3(self,event):
        if self.domicilio.get() == self.placeholder3:
            self.domicilio.delete(0,END)
            self.domicilio.config(fg="black")
     #Si el campo nombre contiene el placeholder, lo borra y pone texto negro
     #If the name field contains the placeholder, delete it and set black text

    def poner_placeholder1(self,event):
        if self.nombre.get() == "":
            self.nombre.insert(0, self.placeholder1)
            self.nombre.config(fg="gray")
    def poner_placeholder2(self,event):
        if self.telefono.get() == "":
            self.telefono.insert(0, self.placeholder2)
            self.telefono.config(fg="gray")
    def poner_placeholder3(self,event):
        if self.domicilio.get() == "":
            self.domicilio.insert(0, self.placeholder3)
            self.domicilio.config(fg="gray")
     #Si el campo nombre está vacío, poner placeholder y texto gris
     #If name field is empty, add placeholder and set it gray
    
    '''INTERFAZ DE LA VENTANA'''
    def inicio(self):
        #CAJA DE TEXTO NOMBRE
        self.placeholder1="Nombre"
        self.nombre = Entry(self.ven, fg="gray")
        self.nombre.insert(0, self.placeholder1)
        self.nombre.bind("<FocusIn>", self.quitar_placeholder1)
        self.nombre.bind("<FocusOut>", self.poner_placeholder1)
        #self.nombre.bind("<Return>", self.validarCaja)
        self.nombre.place(x=10, y=10, width=100)
        #CAJA DE TEXTO TELEFONO
        self.placeholder2="Telefono"
        self.telefono = Entry(self.ven, fg="gray")
        self.telefono.insert(0, self.placeholder2)
        self.telefono.bind("<FocusIn>", self.quitar_placeholder2)
        self.telefono.bind("<FocusOut>", self.poner_placeholder2)
        #self.telefono.bind("<Return>", self.validarCaja)
        self.telefono.place(x=120, y=10, width=100)
        #CAJA DE TEXTO DOMICILIO
        self.placeholder3="Domicilio"
        self.domicilio = Entry(self.ven, fg="gray")
        self.domicilio.insert(0, self.placeholder3)
        self.domicilio.bind("<FocusIn>", self.quitar_placeholder3)
        self.domicilio.bind("<FocusOut>", self.poner_placeholder3)
        self.domicilio.bind("<Return>", self.validarCaja)
        self.domicilio.place(x=230, y=10, width=100)

        Label(self.ven, text= "Sexo").place(x=10, y=30)
        self.modo = StringVar(value="F")
        Radiobutton(self.ven, text="F", variable=self.modo, value="F").place(x=10, y=50)
        Radiobutton(self.ven, text="M", variable=self.modo, value="M").place(x=10, y=70)
        self.lista= Listbox(self.ven, height=6, width=35, bg="white", font=("Helvetica",10))
        self.lista.place(x=10, y=100)
        Button(self.ven, text="Agregar", command=self.validarCaja, width=10).place(x=80, y=50,
                                                                               width=100, height=30)
    
        self.ven.mainloop()

    def agregar(self):
        pass

    def validarCaja(self, event=0):
        if(self.nombre.get == self.placeholder1 
           or self.telefono.get == self.placeholder2 
           or self.domicilio.get == self.placeholder3 or self.domicilio.get()==""):
            messagebox.showerror('Error','Faltan datos')
        #Validar si los campos están vacíos o siguen con el placeholder
        #Validate if fields are empty or still contain the placeholder
        else:
            nombre = self.nombre.get()
            telefono = self.telefono.get()
            domicilio = self.domicilio.get()
            #Obtener valores reales de los campos
            #Get actual field values
            
            if not self.val.ValidarLetra(nombre):
             messagebox.showerror('Error', 'El nombre solo debe contener letras')
             return
            #Validar que sean letras/Validate only letters
            if not self.val.ValidarNumeros(telefono):
              messagebox.showerror('Error', 'El teléfono solo debe contener números')
              return
            #Validar que el teléfono tenga solo números
            #Validate phone number contains only digits
            if self.modo.get() == "F":
                sexo = "Femenino"
            #Convertir valor del radiobutton a texto
            #Convert radiobutton value to readable text
            else:
                sexo = "Masculino"
            clave = nombre[0] + telefono[0] + domicilio[0:2]
            #Crear clave usando inicial/Create ID using initials
            persona = clave + "-" + nombre + "-" + telefono + "-" + domicilio + "-" + sexo
            #Armar cadena final/Build final record string
            self.lista.insert(self.lista.size()+1,persona)
            #Insertar en la lista/Insert into listbox
        
if __name__=='__main__':
    app= Principal()
    app.inicio()

    '''Validar nombre y telefono'''