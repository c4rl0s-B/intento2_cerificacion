from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Viaje:
    def __init__(self,data):
        self.id = data.get('id')
        self.destino = data.get('destino')
        self.fecha_fin = data.get('fecha_fin')
        self.fecha_inicio = data.get('fecha_inicio')
        self.itinerario = data.get('itinerario')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    @classmethod
    def save(cls,data):
        query = """INSERT INTO viajes (destino, fecha_fin, fecha_inicio, itinerario, created_at, updated_at) VALUES (%(destino)s,%(fecha_fin)s,%(fecha_inicio)s,%(itinerario)s,NOW(),NOW())"""
        return connectToMySQL('viajero-frecuente').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM viajes"
        viajes_en_db = connectToMySQL('viajero-frecuente').query_db(query)
        viajes = []
        for viaje in viajes_en_db:
            viajes.append(cls(viaje))
        return viajes

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM viajes WHERE id=%(id)s"
        viaje_en_db = connectToMySQL('viajero-frecuente').query_db(query,data)
        if not viaje_en_db:
            return None
        return cls(viaje_en_db[0])

    @classmethod
    def update(cls,data):
        query = """UPDATE viajes SET destino=%(destino)s, fecha_fin=%(fecha_fin)s, fecha_inicio=%(fecha_inicio)s, itinerario=%(itinerario)s, updated_at=NOW() WHERE id=%(id)s"""
        return connectToMySQL('viajero-frecuente').query_db(query,data)

    # @classmethod
    # def delete(cls,data):
    #     query = "DELETE FROM viajes WHERE id=%(id)s"
    #     return connectToMySQL('viajero-frecuente').query_db(query,data)

    @classmethod
    def eliminar(cls, data):
        query = """
            DELETE FROM usuarios
            WHERE id = %(id)s;
        """
        return connectToMySQL('viajero-frecuente').query_db(query,data)

    
    @staticmethod
    def validar_viaje(formulario):
        es_valido = True
        if len(formulario['destino']) < 2:
            flash("El destino debe tener al menos 2 caracteres", 'viaje')
            es_valido = False
        if len(formulario['itinerario']) < 10:
            flash("El itinerario debe tener al menos 10 caracteres", 'viaje')
            es_valido = False
        if not formulario.get('fecha_inicio'):
            flash("La fecha de inicio es obligatoria", 'viaje')
            es_valido = False
        if not formulario.get('fecha_fin'):
            flash("La fecha de fin es obligatoria", 'viaje')
            es_valido = False
        elif formulario.get('fecha_inicio') and formulario.get('fecha_fin'):
            if formulario['fecha_fin'] < formulario['fecha_inicio']:
                flash("La fecha de fin no puede ser anterior a la fecha de inicio", 'viaje')
                es_valido = False
        elif formulario.get('fecha_inicio')and formulario.get('fecha_fin'):
            if formulario['fecha_inicio']>= 'NOW()':
                flash("La fecha de inicio no puede ser anterior a la fecha actual", 'viaje')
                es_valido = False   
        return es_valido

    @staticmethod
    def validar_edicion(formulario):
        es_valido = True
        if len(formulario['destino']) < 2:
            flash("El destino debe tener al menos 2 caracteres", 'viaje')
            es_valido = False
        if len(formulario['itinerario']) < 10:
            flash("El itinerario debe tener al menos 10 caracteres", 'viaje')
            es_valido = False
        if not formulario.get('fecha_inicio'):
            flash("La fecha de inicio es obligatoria", 'viaje')
            es_valido = False
        if not formulario.get('fecha_fin'):
            flash("La fecha de fin es obligatoria", 'viaje')
            es_valido = False
        elif formulario.get('fecha_inicio') and formulario.get('fecha_fin'):
            if formulario['fecha_fin'] < formulario['fecha_inicio']:
                flash("La fecha de fin no puede ser anterior a la fecha de inicio", 'viaje')
                es_valido = False
        return es_valido

    # @staticmethod
    # def validar_eliminacion(formulario):
    #     es_valido = True
    #     if not formulario.get('id'):
    #         flash("El ID del viaje es obligatorio", 'viaje')
    #         es_valido = False
    #     return es_valido