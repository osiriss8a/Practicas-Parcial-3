
'''hacer un programa que lea nombre, apellido paterno y materno 
en 3 cajas sepoaradas,ademas leer dia, mes y año en 3 cajas de texto
separadas. 
al presionar un boton se agregara a un lisbox el rfc de la persona, ademas
tendra dos botones para eleminir elementos de listbox mediante pilas o colas'''
from tkinter import * 
from tkinter import messagebox
from validacionesp2 import Validar 

class Principal():
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        ancho = 420
        alto = 310
        ventana_alto  = self.ven.winfo_screenwidth()
        ventana_ancho = self.ven.winfo_screenheight()
        x = (ventana_alto // 2) - (ancho //2)
        y = (ventana_ancho // 2) - (alto //2)
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")
        self.datos = []

    def inicio(self):
         self.label = Label(text="Nombre")
         self.label.place(x=5, y=10)
         self.nombre = Entry(self.ven)
         self.nombre.place(x=60, y=10)

         self.label = Label(text="Apellido Paterno")
         self.label.place(x=5, y=35)
         self.Pat = Entry(self.ven)
         self.Pat.place(x=110, y=35)

         self.label = Label(text="Apellido Materno")
         self.label.place(x=5, y=65)
         self.Mat = Entry(self.ven)
         self.Mat.place(x=110, y=65)

         self.label = Label(text="Dia de Nacimiento")
         self.label.place(x=5, y=95)
         self.Dia = Entry(self.ven)
         self.Dia.place(x=110, y=95)

         self.label = Label(text="Mes de Nacimiento")
         self.label.place(x=5, y=125)
         self.Mes = Entry(self.ven)
         self.Mes.place(x=115, y=125)

         self.label = Label(text="Año de Nacimiento")
         self.label.place(x=5, y=155)
         self.An = Entry(self.ven)
         self.An.place(x=115, y=155)

         Button(self.ven, text="Agregar", command=self.agregar, width=10).place(x=120, y=210)
         Button(self.ven, text="Eliminar", command=self.eliminard, width=10).place(x=30, y=210)
         Button(self.ven, text="Ordenar", command=self.ordenar, width=10).place(x=210, y=210)

         self.lista= Listbox(self.ven, height=10, width=10, bg="white", font=("Helvetica",12))
         self.lista.place(x=270, y=10)

         self.modo = StringVar(value="Pilas")
         Radiobutton(self.ven, text="Pilas", variable=self.modo, value="Pilas").place(x=60, y=250)
         Radiobutton(self.ven, text="Colas", variable=self.modo, value="Colas").place(x=120, y=250)
         
         self.ven.mainloop()

    def agregar(self):
        nombre = self.nombre.get().strip().upper()
        pat = self.Pat.get().strip().upper()
        mat = self.Mat.get().strip().upper()
        dia = self.Dia.get().strip()
        mes = self.Mes.get().strip()
        anio = self.An.get().strip()
        if not (nombre and pat and mat and dia and mes and anio):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        if not (self.val.ValidarLetra(nombre) and self.val.ValidarLetra(pat) and self.val.ValidarLetra(mat)):
            messagebox.showerror("Error", "Los nombres y apellidos deben contener solo letras")
            return
        if not (self.val.ValidarNumeros(dia)and self.val.ValidarNumeros(mes) and self.val.ValidarNumeros(anio)):
            messagebox.showerror("Error","No son numeros")
            return
        rfc = (pat[:2] + mat[0] + nombre[0] + anio[2:] + mes + dia)

        if self.modo.get() == "Pilas":
            self.datos.append(rfc)
        else:
            self.datos.insert(0, rfc)

        self.actualizar_lista()
        messagebox.showinfo("RFC agregado", f"RFC generado: {rfc}")

        # Limpiar campos
        self.nombre.delete(0, END)
        self.Pat.delete(0, END)
        self.Mat.delete(0, END)
        self.Dia.delete(0, END)
        self.Mes.delete(0, END)
        self.An.delete(0, END)

    def actualizar_lista(self):
        self.lista.delete(0, END)
        for i in self.datos:
            self.lista.insert(END, i)    
           

    def eliminard(self):
         if not self.datos:
            messagebox.showwarning("Atención", "No hay elementos para eliminar.")
            return

         if self.modo.get() == "Pilas":
            self.datos.pop()  # Elimina el último
         else:
            self.datos.pop(0)  # Elimina el primero

         self.actualizar_lista()
    def ordenar(self):
        if self.lista.size() <= 0:
            messagebox.showerror("Error","La lista esta vacia")
            return
        if self.modo.get() == 'Pilas':
            #Ultimo que entra, primero que sale
            self.lista.delete(self.lista.size()-1)
        else:
            #Primero que entra, primero que sale
            self.lista.delete(0)
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')



if __name__=='__main__':
    app = Principal()
    app.inicio()