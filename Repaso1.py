

from tkinter import * 
from tkinter import messagebox
from validacionesp2 import Validar 
from tkinter import ttk

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
        self.lis = []
    def ordenar(self):
        seleccion = self.tabla.selection()
        if self.modo.get() == "Pilas":
        # Elimina la última fila (pila)
          item = self.tabla.get_children()[-1]
          self.tabla.delete(item)
        else:
        # Elimina la primera fila (cola)
          item = self.tabla.get_children()[0]
          self.tabla.delete(item)
    
    def eliminar(self):
        renglon = self.tabla.selection()
        if not renglon:
            messagebox.showerror("Error","Elije una fila")
        else:
            self.tabla.delete(renglon)
            messagebox.showinfo("Correcto","Fila Eliminada")
       

    def validar(self):
        if (len(self.nombre.get())==0 or len(self.edad.get())==0 or len(self.matricula.get())==0):
            messagebox.showerror("Error","Faltan Datos")
        else:
            nom = self.nombre.get()
            ed = self.edad.get()
            mat = self.matricula.get()
            
            if not self.val.ValidarLetra(nom):
             messagebox.showerror('Error', 'El nombre solo debe contener letras')
             return
            if not self.val.ValidarNumeros(ed):
              messagebox.showerror('Error', 'La edad solo debe contener numeros')
              return
            if not self.val.ValidarNumeros(mat):
              messagebox.showerror('Error', 'La matricula solo debe contener numeros')
              return
            messagebox.showinfo("Correcto","Registro exitoso")
            self.tabla.insert("", "end", values=(nom,ed,mat))
            self.nombre.delete(0,END)
            self.edad.delete(0,END)
            self.matricula.delete(0,END)

    def inicio(self):
        self.label = Label(text="Nombre Estudiante")
        self.label.place(x=10, y=10)

        self.nombre = Entry(self.ven)
        self.nombre.place(x=120, y=10)

        self.label = Label(text="Edad")
        self.label.place(x=10, y=35)

        self.edad = Entry(self.ven)
        self.edad.place(x=120, y=35)

        self.label = Label(text="Matricula")
        self.label.place(x=10, y=65)

        self.matricula = Entry(self.ven)
        self.matricula.place(x=120, y=65)

        Button(self.ven, text="Validar", command=self.validar, width=10).place(x=250, y=10)
        Button(self.ven, text="Eliminar", command=self.eliminar, width=10).place(x=250, y=40)
        Button(self.ven, text="Ordenar", command=self.ordenar, width=10).place(x=340, y=10)

        columnas = ("Nombre","Edad","Matricula")
        self.tabla = ttk.Treeview(self.ven, columns = columnas, show = "headings")
        self.tabla.place(x=10, y=100, width=350, height=190)

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=30)
        scrolly = ttk.Scrollbar(self.ven, orient="vertical", command= self.tabla.yview)
        scrollx = ttk.Scrollbar(self.ven, orient="horizontal",command= self.tabla.xview)
        scrolly.place(x=360, y=90,height=200)
        scrollx.place(x=10, y=280, width=350)
        
        self.modo = StringVar(value="Pilas")
        Radiobutton(self.ven, text="Pilas", variable=self.modo, value="Pilas").place(x=250, y=70)
        Radiobutton(self.ven, text="Colas", variable=self.modo, value="Colas").place(x=300, y=70)
         
        self.ven.mainloop()
   

if __name__=='__main__':
    app = Principal()
    app.inicio()