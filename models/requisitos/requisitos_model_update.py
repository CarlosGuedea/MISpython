from database.db_admin_tramites import get_db_connection


class Requisitos_Update:
    def __init__(self, id, codigo, valor, descripcion):
        self.id = id
        self.codigo = codigo
        self.valor = valor
        self.descripcion = descripcion

    @staticmethod
    def update_requisitos(id, codigo, valor, descripcion):
        """
        Actualiza los detalles de un único requisito en la base de datos.
        """
        try:
            # Obtener la conexión a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            # Consulta SQL para actualizar el requisito
            sql = """
            UPDATE cat_requisitos
            SET codigo = ?, valor = ?, descripcion = ?
            WHERE id = ?
            """
            # Ejecutar la consulta con los parámetros
            cursor.execute(sql, (codigo, valor, descripcion, id))

            # Confirmar los cambios
            conn.commit()

            # Comprobar si se actualizó alguna fila
            if cursor.rowcount == 0:
                return False  # No se encontró el requisito con el ID proporcionado
            return True  # Actualización exitosa

        except Exception as e:
            conn.rollback()  # Revertir en caso de error
            raise Exception(f"Error al actualizar requisito: {str(e)}")

        finally:
            cursor.close()
            conn.close()
