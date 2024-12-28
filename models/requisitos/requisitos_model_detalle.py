from database.db_admin_tramites import get_db_connection


class Requisitos_Detalle:
    def __init__(self, id, estatus, codigo, valor, etiqueta):
        self.id = id
        self.estatus = estatus
        self.codigo = codigo
        self.valor = valor
        self.etiqueta = etiqueta

    @staticmethod
    def obtener_requisitos_detalle(id):
        """
        Obtiene los detalles de un único requisito
        """
        try:
            # Obtener la conexión a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            # Ejecutar la consulta SQL para obtener un único resultado
            cursor.execute("SELECT id, estatus, codigo, valor, etiqueta FROM cat_requisitos WHERE id = ?", (id,))
            resultado = cursor.fetchone()  # Obtener un solo resultado

            if resultado:
                # Crear un objeto Requisitos_Detalle con los datos obtenidos
                return Requisitos_Detalle(
                    resultado[0],  # id
                    resultado[1],  # estatus
                    resultado[2],  # codigo
                    resultado[3],  # valor
                    resultado[4],  # etiqueta
                )
            else:
                return None  # Si no hay resultados, retorna None

        except Exception as e:
            raise Exception(f"Error al obtener requisito: {str(e)}")

        finally:
            cursor.close()
            conn.close()