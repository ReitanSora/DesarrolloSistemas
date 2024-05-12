import base64

from src.models.PeliculaModel import Pelicula

class PeliculaController():

    @classmethod
    def find_all(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "select * from pelicula"
            cursor.execute(sql)
            result = cursor.fetchall()
            listaPelicula = list()
            for item in result:
                pelicula = Pelicula(id=item[0], nombre=item[1], fecha=item[2], sinopsis=item[3], enlace=item[4], imagen=self.convert_to_base64(item[5]))
                listaPelicula.append(pelicula)
            if result != None:
                return listaPelicula
            else:
                return None
        except Exception as e:
            print(e)
            raise Exception(e)
        
    @classmethod
    def convert_to_base64(self, imagen):
        if (type(imagen) == bytes):
            return base64.b64encode(imagen).decode("utf-8")
        else:
            return imagen
