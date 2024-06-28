from app.database import get_db
from datetime import timedelta

class Reserva:
    
    #constructor
    def __init__(self, Id_reserva=None, nombre=None, email=None, nro_telefono=None, cant_comensales=None, fecha=None, hora=None, local=None, preferencias=None, confirmacion=None):
        self.Id_reserva = Id_reserva
        self.nombre = nombre
        self.email = email
        self.nro_telefono = nro_telefono
        self.cant_comensales = cant_comensales
        self.fecha = fecha
        self.hora = hora
        self.local = local
        self.preferencias = preferencias
        self.confirmacion = confirmacion
    
    def serialize(self):
        return {
            'Id_Reserva': self.Id_reserva,
            'Nombre': self.nombre,
            'email': self.email,
            'Nro_Telefono': self.nro_telefono,
            'Cant_Comensales': self.cant_comensales,
            'Fecha': self.fecha.isoformat() if self.fecha else None,
            'Hora': f"{self.hora.seconds // 3600:02}:{(self.hora.seconds // 60) % 60:02}" if isinstance(self.hora, timedelta) else self.hora,
            'Local': self.local,
            'Preferencias': self.preferencias,
            'Confirmacion': self.confirmacion,
        }
        
    @staticmethod
    def get_all():
        #Se muestra la lista de reservas
        db = get_db()
        cursor = db.cursor()
        query = """SELECT Id_reserva, nombre, email, nro_telefono, cant_comensales, fecha, hora, tbl_local.local, preferencias, confirmacion FROM tbl_reservas INNER JOIN tbl_local ON tbl_reservas.local_Id = tbl_local.Id_local"""
        cursor.execute(query)
        #Obtener Resultados
        rows = cursor.fetchall()
        reservas = [Reserva(Id_reserva=row[0], nombre=row[1], email=row[2], nro_telefono=row[3], cant_comensales=row[4], fecha=row[5], hora=row[6], local=row[7], preferencias=row[8], confirmacion=row[9]) for row in rows]
        #Cerramos el cursor
        cursor.close()
        #devuelve Resultados
        return reservas
    
    def save(self):
        #Guarda o actualiza las reservas.
        db = get_db()
        cursor = db.cursor()
        if self.Id_reserva:
            query = "UPDATE tbl_reservas SET nombre=%s, email=%s, nro_telefono=%s, cant_comensales=%s, fecha=%s, hora=%s, local_Id=%s, preferencias=%s, confirmacion=%s WHERE id_reserva = %s"
            cursor.execute(query, (self.nombre, self.email, self.nro_telefono, self.cant_comensales, self.fecha, self.hora, self.local, self.preferencias, self.confirmacion, self.Id_reserva))
        else:
            query = "INSERT INTO tbl_reservas (nombre, email, nro_telefono, cant_comensales, fecha, hora, local_Id, preferencias, confirmacion) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)"
            cursor.execute(query, (self.nombre, self.email, self.nro_telefono, self.cant_comensales, self.fecha, self.hora, self.local, self.preferencias, self.confirmacion))
        #Obtener el ultimo Id generado
        self.Id_reserva = cursor.lastrowid
        db.commit() #Confirmación de las sentencias
        cursor.close()
        
    @staticmethod
    def get_by_id(Id_reserva):
        #Metodo para seleccionar una reserva
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM tbl_reservas WHERE Id_reserva = %s"
        cursor.execute(query, (Id_reserva,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Reserva(Id_reserva=row[0], nombre=row[1], email=row[2], nro_telefono=row[3], cant_comensales=row[4], fecha=row[5], hora=row[6], local=row[7], preferencias=row[8], confirmacion=row[9])
        return None
        
    @staticmethod
    def confirm(Id_reserva):
        #Metodo para confirmar las reservas
        db = get_db()
        cursor = db.cursor()
        query = "UPDATE tbl_reservas SET confirmacion = 1 WHERE Id_reserva = %s"
        cursor.execute(query, (Id_reserva,))
        db.commit()
        cursor.close()
        
    def delete(self):
        #Metodo para eliminar una reserva
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM tbl_reservas WHERE Id_reserva = %s"
        cursor.execute(query, (self.Id_reserva,))
        db.commit()
        cursor.close()
        