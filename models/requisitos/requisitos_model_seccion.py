from database.db_admin_tramites import get_db_connection


class Requisitos_Seccion:
    def __init__(self, id_requisito, descripcion_requisito, cat_id, valor, descripcion_seccion):
        self.id_requisito = id_requisito
        self.descripcion_requisito = descripcion_requisito
        self.cat_id = cat_id
        self.valor = valor
        self.descripcion_seccion = descripcion_seccion

    @staticmethod
    def obtener_secciones_detalle(id):
        """
        Obtiene todas las secciones de un unico requisito
        """
        try:
            # Obtener la conexión a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            # Ejecutar la consulta SQL para obtener un único resultado
            cursor.execute("SELECT cr.id AS id_requisito, cr.descripcion AS descripcion_requisito, cs.cat_id AS id_seccion, cs.valor as valor_seccion, cs.descripcion AS descripcion_seccion FROM cat_requisitos cr INNER JOIN cat_secciones cs ON cr.id = cs.cat_id WHERE cr.id = ?;", (id,))
            resultado = cursor.fetchone()  # Obtener un solo resultado

            if resultado:
                # Crear un objeto Requisitos_Detalle con los datos obtenidos
                return Requisitos_Seccion(
                    resultado[0],  # requisito_id
                    resultado[1],  # descripcion_requisito
                    resultado[2],  # seccion_cat_id
                    resultado[3],  #valor
                    resultado[4],  # descripcion_seccion
                )
                
            else:
                return None  # Si no hay resultados, retorna None

        except Exception as e:
            raise Exception(f"Error al obtener requisito: {str(e)}")

        finally:
            cursor.close()
            conn.close()