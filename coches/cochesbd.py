from conexionBD import conexion, cursor 
class Cochesbd:
    def __init__(self,marca,color,modelo,velocidad,potencia ,asientos):
      self._marca = marca
      self._color = color
      self._modelo = modelo
      self._velocidad = velocidad
      self._potencia = potencia
      self._asientos = asientos
    def insertar(self):
        try:
            sql = "INSERT INTO coches VALUES (null, %s, %s, %s, %s, %s, %s)"
            valores = (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}")
            return False
    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from coches")
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def buscar(id):
        try:
            cursor.execute("select * from coches where id=%s", (id,))
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute( "select * from coches where id=%s",(id,))
            lista = cursor.fetchall()
            if len (lista) > 0:
                cursor.execute("delete from coches where id=%s",(id,))
                conexion.commit()
                return True
            else:
                return False
        except:
            return False
    def actualizar(self, id):
        try:
            cursor.execute( "select * from coches where id=%s",(id,))
            lista = cursor.fetchall()
            if len (lista) > 0:
                sql = "UPDATE coches SET marca = %s, color = %s, modelo = %s, velocidad = %s, potencia = %s, asientos = %s WHERE id = %s"
                valores = (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos, id)
                cursor.execute(sql, valores)
                conexion.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
    def acelerar(self):
        self._velocidad += 1
        print(f"la velocidad ahora es {self._velocidad}")
    def frenar(self):
        self._velocidad -= 1
        print(f"la velocidad ahora es {self._velocidad}")
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca=marca
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color=color
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def setModelo(self,modelo):
        self._modelo=modelo
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def setVelocidad(self,velocidad):
        self._velocidad=velocidad
    @property
    def potencia(self):
        return self._potencia
    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia
    @property
    def asientos(self):
        return self._asientos
    @asientos.setter
    def asientos(self,asientos):
        self._asientos = asientos
