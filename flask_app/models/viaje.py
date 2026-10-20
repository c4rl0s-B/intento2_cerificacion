from flask_app.config.mysqlconnection import connectToMySQL

class Pelicula:
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
        query = """INSERT INTO viajes (destino, fecha_fin, fecha_iniccio, itinerario, created_at, updated_at) VALUES (%(destino)s,%(fecha_fin)s,%(fecha_inicio)s,%(itinerario)s,NOW(),NOW())"""