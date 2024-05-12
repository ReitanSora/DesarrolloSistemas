from src.models.GeneroModel import Genero

class GeneroController():

    listaGenero = list()

    @classmethod
    def find_all(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "select * from genero"
            cursor.execute(sql)
            result = cursor.fetchall()
            self.listaGenero.clear()
            for item in result:
                genero = Genero(id=item[0], nombre=item[1], descripcion=item[2])
                self.listaGenero.append(genero)
            if result != None:
                return self.listaGenero
            else:
                return None
        except Exception as e:
            print(e)
            raise Exception(e)