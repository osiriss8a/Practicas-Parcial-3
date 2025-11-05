
from tkinter import * 
from tkinter import messagebox
from validacionesp2 import Validar 
import numpy as np

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
        else:
            nombre = self.nombre.get()
            telefono = self.telefono.get()
            domicilio = self.domicilio.get()
            
            if not self.val.ValidarLetra(nombre):
             messagebox.showerror('Error', 'El nombre solo debe contener letras')
             return
            if not self.val.ValidarNumeros(telefono):
              messagebox.showerror('Error', 'El teléfono solo debe contener números')
              return

            if self.modo.get() == "F":
                sexo = "Femenino"
            else:
                sexo = "Masculino"
            clave = nombre[0] + telefono[0] + domicilio[0:2]
            persona = clave + "-" + nombre + "-" + telefono + "-" + domicilio + "-" + sexo
            self.lista.insert(self.lista.size()+1,persona)
        
if __name__=='__main__':
    app= Principal()
    app.inicio()

    '''Validar nombre y telefono'''