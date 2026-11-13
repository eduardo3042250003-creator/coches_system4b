from coches import cochesbd
import tkinter as tk
from tkinter import Tk,Label,Entry,Button
from tkinter import messagebox
from tkinter import ttk
class App:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title ("Gestor de coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()
    def borrarPantalla (self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
        
    def main (self):
        self.borrarPantalla()
        Label(self.ventana,text ="::: MENU PRINCIPAL:::").pack(pady=20)
        Button(self.ventana,text='1.- Coches', command=self.menuAcciones).pack(pady=10)
        Button(self.ventana,text='2.- salir',command=self.ventana.quit).pack(pady=10)
    def menuAcciones(self,):
        self.borrarPantalla()
        tipo = "Coches"
        Label (self.ventana, text = f':::: menu de {tipo}:::: ').pack(pady = 10)
        Button(self.ventana, text = f"1.-agregar", command=self.InsertarCochesView).pack(pady=10)
        Button(self.ventana, text = f"2.-borrar", command=self.borrarCochesView).pack(pady=10)
        Button(self.ventana, text = f"3.- modificar", command=self.actualizarCochesView).pack(pady=10)
        Button(self.ventana, text = f"4.- mostrar", command=self.mostrarCochesView).pack(pady=10)
        Button(self.ventana, text = f"5.-salir", command=self.main).pack(pady=10)
    def InsertarCochesView(self):
        self.borrarPantalla()
        Label(self.ventana, text="ingresar datos del Coche").pack(pady=10)
        Label(self.ventana, text="Marca").pack(pady=10)
        self.marca = Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)
        Label(self.ventana, text="Color").pack(pady=10)
        self.color = Entry(self.ventana)
        self.color.pack(pady=5)
        Label(self.ventana, text="Modelo").pack(pady=10)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=5)
        Label(self.ventana, text="Velocidad").pack(pady=10)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=5)
        Label(self.ventana, text="Potencia").pack(pady=10)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=5)
        Label(self.ventana, text="asientos").pack(pady=10)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=5)
        Button(self.ventana, text='agregar', command=lambda: {self.insertarCochesController(), self.InsertarCochesView()}).pack(pady=5)
        Button(self.ventana, text='::Regresar::', command= self.menuAcciones).pack(pady=5)
    def borrarCochesView(self):
        self.borrarPantalla()
        Label(self.ventana, text="ingresar el id del coche que deseas borrar").pack(pady=10)
        self.idBorrar = Entry(self.ventana)
        self.idBorrar.focus()
        self.idBorrar.pack(pady = 5)
        self.btn_buscar = Button(self.ventana, text='buscar', command= lambda: self.buscarController("borrar"))
        self.btn_eliminar = Button(self.ventana, text='eliminar', command= lambda:{self.borrarCochesController(), self.borrarCochesView()})
        self.btn_eliminar.pack(pady=5)
        Button(self.ventana, text='::Regresar::', command= self.menuAcciones).pack(pady=5)
    def actualizarCochesView(self):
        self.borrarPantalla()
        Label(self.ventana, text="ingresar el id del coche que deseas actualizar").pack(pady=10)
        self.idActualizar = Entry(self.ventana)
        self.idActualizar.focus()
        self.idActualizar.pack(pady = 5)
        Label(self.ventana, text="Marca").pack(pady=10)
        self.marcaAct = Entry(self.ventana)
        self.marcaAct.pack(pady=5)
        Label(self.ventana, text="Color").pack(pady=10)
        self.colorAct = Entry(self.ventana)
        self.colorAct.pack(pady=5)
        Label(self.ventana, text="Modelo").pack(pady=10)
        self.modeloAct = Entry(self.ventana)
        self.modeloAct.pack(pady=5)
        Label(self.ventana, text="Velocidad").pack(pady=10)
        self.velocidadAct = Entry(self.ventana)
        self.velocidadAct.pack(pady=5)
        Label(self.ventana, text="Potencia").pack(pady=10)
        self.potenciaAct = Entry(self.ventana)
        self.potenciaAct.pack(pady=5)
        Label(self.ventana, text="asientos").pack(pady=10)
        self.asientosAct = Entry(self.ventana)
        self.asientosAct.pack(pady=5)
        Button(self.ventana, text='Actualizar', command= lambda: {self.actualizarCochesController(),self.actualizarCochesView()}).pack(pady=5)
        Button(self.ventana, text='::Regresar::', command= self.menuAcciones).pack(pady=5)
    def mostrarCochesView(self):
        self.borrarPantalla()
        Label(self.ventana, text="Lista de Coches").pack(pady=10)
        datos = self.mostrarCochescontroller()
        """
        Label(self.ventana, text=f"{datos}").pack(pady=5)
        Button(self.ventana,text="Volver",command=self.menuAcciones).pack(pady=10)
        """
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",borderwidth=2,relief="solid")
        style.configure("Treeview.Heading",relief="solid",borderwidth=1)
        columnas = ("id","marca","color","modelo","velocidad","potencia","asientos")
        tabla = ttk.Treeview(self.ventana,columns=columnas,show="headings")
        for col in columnas:
            tabla.heading(col, text=col)
            
            tabla.column(col, width=60, anchor="center")
        if datos:
            for coche in datos:
                tabla.insert("",tk.END, values=coche)
        tabla.pack(pady=10, fill="both", expand=True)
        Button(self.ventana, text="Volver", command=self.menuAcciones).pack(pady=10)
    def cambiarEstadoBoton(self, estado, tipoAccion):
        if estado:
            if tipoAccion == "borrar":
                self.btn_eliminar.config(state=tk.NORMAL)
            elif tipoAccion == "actualizar":
                self.btn_actualizar.config(state=tk.NORMAL)
        else:
            if tipoAccion == "borrar":
                self.btn_eliminar.config(state=tk.DISABLED)
            elif tipoAccion == "actualizar":
                self.btn_actualizar.config(state=tk.DISABLED)

    def confirmacion_eliminar(self, tipo):
        resp = messagebox.askyesno(title="Confirmación", message=f"¿Estás seguro de que deseas {tipo} este coche?") 
        if resp == "Yes":
            return True
        else:
            return False

##controllers        
    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title="::EXITO::",message="Accion como yo ...exitosa")
        else:
            messagebox.showerror(title='VERIFIQUE ', message="Esta accion no pudo realizarse con exito")
    def insertarCochesController(self):
        coche1 = cochesbd.Cochesbd(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get(),)
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1
    def borrarCochesController(self):
        id = self.idBorrar.get()
        resp = self.confirmacion_eliminar("eliminar") 
        if resp == True:
            respuesta = cochesbd.Cochesbd.eliminar(id)
        else:
            self.respuesta_sql(respuesta)
    def actualizarCochesController(self):
        id = self.idActualizar.get()
        coche1 = cochesbd.Cochesbd(self.marcaAct.get(),self.colorAct.get(),self.modeloAct.get(),self.velocidadAct.get(),self.potenciaAct.get(),self.asientosAct.get(),)
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1
    def buscarController(self,tipoAccion):
        id = self.idBorrar.get()
        coche1 = cochesbd.Cochesbd.buscar(id)
        if len(coche1) > 0:
            messagebox.showinfo(title="registro encontrado",message=f"El coche con id {id} existe en la base de datos puiedes {tipoAccion}lo")
            self.cambiarEstadoBoton(True, tipoAccion)
        else:
            messagebox.showerror(title="registro no encontrado",message=f"El coche con id {id} no existe en la base de datos")
            self.cambiarEstadoBoton(False, tipoAccion)


    def mostrarCochescontroller(self):
        obtenerCoches =  cochesbd.Cochesbd.consultar()
        return obtenerCoches
if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()