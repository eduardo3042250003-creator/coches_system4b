from models import coches_models
from view import coches_view



class CochesController:
    def insertarCochesController(self):
        coche1 = coches_models.CochesModel(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get(),)
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1
    def borrarCochesController(self):
        id = self.id.get()
        resp = self.confirmacion_eliminar("eliminar") 
        if resp == True:
            respuesta = coches_models.CochesModel.eliminar(id)
            self.respuesta_sql(respuesta)

    def actualizarCochesController(self):
        id = self.id.get()
        coche1 = coches_models.CochesModel(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get(),)
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1
    def buscarController(self,tipoAccion):
        #idBorrar
        id = self.id.get()
        coche1 = coches_models.CochesModel.buscar(id)
        coches_view.CochesView.encontro(self,coche1,tipoAccion,id)
        


    def mostrarCochescontroller(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in coches_models.CochesModel.consultar():
            self.tree.insert("", "end", values=row)
