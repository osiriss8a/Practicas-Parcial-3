'''Valdar Numeros, solo ingresar 2 digitos, eliminar un dato que selecciones y 
ordenar los numeros en pilas o colas y eliminar en burbuja o seleccion, depense de su 
seleccion con el radiobutton'''

from tkinter import * 
from tkinter import messagebox
from Validacionesp1 import Validar 
import numpy as np

'''VENTANA'''
class Principal():
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        ancho = 320
        alto = 210
        ventana_alto  = self.ven.winfo_screenwidth()
        ventana_ancho = self.ven.winfo_screenheight()
        x = (ventana_alto // 2) - (ancho //2)
        y = (ventana_ancho // 2) - (alto //2)
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")
        self.lis = []
        #Lista para almacenar datos
        #List to store input numbers

    def validarCaja(self):
        valor = self.dato.get()
        #Obtiene el valor escrito en la caja de texto
        #Gets the entered value from the Entry widget
        if (self.val.ValidarNumeros(valor)):
        #Verifica si son números
        #Checks if input is numeric
            if (self.val.ValidarEntradas(valor)):
                #Verifica si solo tiene dos dígitos
                #Checks if input has only two digits
                self.lista.insert(self.lista.size()+1, valor)
                #Inserta el valor en la lista
                #Inserts value into the Listbox
                self.dato.delete(0,END)
                #Limpia la caja de texto
                #Clears the Entry box
            else: 
                messagebox.showerror("Error","Solo se permite dos digitos") 
                self.dato.delete(0,END) 
                #Error si no son dos dígitos
                #Error if value isn't two digits 
        else: 
            messagebox.showerror("Error","No son numeros")
            self.dato.delete(0,END)
            #Error si no es número
            #Error if input is not numeric

        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')
        #Actualiza etiqueta con cantidad de elementos
        #Updates label with number of elements

    def eliminarDato(self):
        if self.lista.size() <= 0:
            messagebox.showerror("Error","La lista esta vacia")
            return
        #Si la lista está vacía muestra error
        #Error if the list is empty
        if self.modo.get() == 'Pilas':
        #Si está en modo PILAS (LIFO)
        #If using STACK mode (LIFO)
            self.lista.delete(self.lista.size()-1)
            #Último entra, primero sale
            #Last in, first out
        else:
            # Modo COLAS (FIFO)
            # QUEUE mode (FIFO)
            self.lista.delete(0)
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')
        #Primero entra, primero sale
        #First in, first out
    
    def ordenar(self):
        self.lis = list(self.lista.get(0,END))
        #Obtiene todos los elementos del Listbox
        #Gets all items from Listbox
        if len(self.lis) <= 0:
            messagebox.showerror("Error","Lista vacia")
        #Si la lista está vacía da error
        #Error if list is empty
        metodo = self.modoorden.get()
        #Obtiene el método de ordenamiento seleccionado
        #Gets selected sorting method

        '''BURBUJA'''
        if metodo == "Burbuja":
            #Recorridos para ordenar/Sorting loops
            for i in range(0,len(self.lis)):
                for x in range(i,len(self.lis)-1):
                    #Compara elementos adyacentes
                    #Compares adjacent elements
                    if self.lis[x] > self.lis[x+1]:
                      aux = self.lis[x]
                      self.lis[x] = self.lis[x+1]
                      self.lis[x+1] = aux
            print(self.lis)
            self.lista.delete(0,END)
            for i in self.lis:
               self.lista.insert(self.lista.size()+1,i)
               #Limpia y vuelve a agregar en orden
               #Clears and re-inserts sorted list

            '''SELECCION'''
        else:
          p = 0
          #Posición del mayor
          #Position of largest element
          for i in range(0,len(self.lis)):
          #Posición del mayor
          #Position of largest element
            aux = int(self.lis[i])
            p = i
            for x in range(i,len(self.lis)):
                # print(self.lis[x])
                if aux < int(self.lis[x]):
                    aux = int(self.lis[x])
                    p = x 
            #Busca el número mayor
            #Searches for the largest number
            self.lis[p] = self.lis[i]
            self.lis[i] = str(aux)
            # Intercambia posiciones/ Swaps positions
          print(self.lis)
          self.lista.delete(0,END)
          for i in self.lis:
             self.lista.insert(self.lista.size()+1,i)
            #Actualiza la lista visual
            #Updates the visual list

    '''INTERFAZ'''
    def inicio(self):
        self.dato = Entry(self.ven)
        self.dato.place(x=50, y=10)

        self.modo = StringVar(value="Pilas")
        Radiobutton(self.ven, text="Pilas", variable=self.modo, value="Pilas").place(x=50, y=40)
        Radiobutton(self.ven, text="Colas", variable=self.modo, value="Colas").place(x=100, y=40)
        self.modoorden = StringVar(value="Burbuja")
        Radiobutton(self.ven, text="Burbuja", variable=self.modoorden, value="Burbuja").place(x=30, y=60)
        Radiobutton(self.ven, text="Seleccion", variable=self.modoorden, value="Seleccion").place(x=100, y=60)
        

        Button(self.ven, text="Validar", command=self.validarCaja, width=10).place(x=100, y=100)
        Button(self.ven, text="Eliminar", command=self.eliminarDato, width=10).place(x=100, y=130)
        Button(self.ven, text="Ordenar", command=self.ordenar, width=10).place(x=100, y=160)

        self.label = Label(text="Numero")
        self.label.place(x=5, y=80)
        self.lista= Listbox(self.ven, height=10, width=10, bg="white", font=("Helvetica",12))
        self.lista.place(x=190, y=10)

        self.ven.mainloop()

if __name__=='__main__':
    app = Principal()
    app.inicio()
    

    
    

    