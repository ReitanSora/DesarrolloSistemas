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
            cursor.close()
            self.listaGenero.clear()
            for item in result:
                genero = Genero(
                    id=item[0], nombre=item[1], descripcion=item[2])
                self.listaGenero.append(genero)
            if result != None:
                return self.listaGenero
            else:
                return None
        except Exception as e:
            print(e)
            raise Exception(e)

    @classmethod
    def find_by_name(self, db, title) -> object:
        try:

            cursor = db.connection.cursor()
            sql = "select * from genero where nombre_genero = '{}'".format(
                title)
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            genero = Genero(
                id=result[0], nombre=result[1], descripcion=result[2])
            if result != None:
                return genero
            else:
                return None
        except Exception as e:
            print(e)
            raise Exception(e)
