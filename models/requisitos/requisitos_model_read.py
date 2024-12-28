from database.db_admin_tramites import get_db_connection


class Requisitos_Read:
    def __init__(self, id, estatus, codigo, valor, etiqueta):
        self.id = id
        self.estatus = estatus
        self.codigo = codigo
        self.valor = valor
        self.etiqueta = etiqueta

    @staticmethod
    def obtener_requisitos():
        """
        Obtiene todos los requisitos
        """
        try:
            # Obtener la conexión a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            # Ejecutar la consulta SQL para obtener los perfiles
            cursor.execute("SELECT id, estatus, codigo, valor, etiqueta FROM cat_requisitos where estatus = 'True'")
            Requisitos = cursor.fetchall()

            # Crear objetos de la clase Usuarios_Perfil con los datos obtenidos
            requisitos_lista = []
            for Requisito in Requisitos:
                requisito_obj = Requisitos_Read(
                    Requisito[0],  # id
                    Requisito[1],  # estatus
                    Requisito[2],  # codigo
                    Requisito[3],  # valor
                    Requisito[4]   # etiqueta
                )
                requisitos_lista.append(requisito_obj)
                


            return requisitos_lista

        except Exception as e:
            raise Exception(f"Error al obtener requisitos: {str(e)}")
        
        finally:
            cursor.close()
            conn.close()


