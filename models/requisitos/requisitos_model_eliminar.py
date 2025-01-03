from database.db_admin_tramites import get_db_connection

class Requisitos_Eliminar:
    def __init__(self, id):
        self.id = id

    @staticmethod
    def eliminar_requisito(id):
        """
        Elimina un requisito y su sección asociada de la base de datos (SQL Server).
        """
        try:
            # Obtener la conexión a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            # Consulta SQL para eliminar el requisito y su sección
            sql = """
            BEGIN TRANSACTION;
             DELETE FROM cat_secciones WHERE cat_id = ?;
            DELETE FROM cat_requisitos WHERE id = ?;
            COMMIT TRANSACTION;
            """
            # Ejecutar la consulta con los parámetros
            cursor.execute(sql, (id, id))

            # Confirmar los cambios
            conn.commit()

            # Verificar si se eliminaron registros
            if cursor.rowcount == 0:
                return False  # No se encontró el requisito con el UUID proporcionado
            return True  # Eliminación exitosa

        except Exception as e:
            if conn:
                conn.rollback()  # Revertir cambios en caso de error
            raise Exception(f"Error al eliminar requisito: {str(e)}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
