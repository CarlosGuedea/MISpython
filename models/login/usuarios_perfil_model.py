from database.db_usuarios2 import get_db_connection

class Usuarios_Perfil:
    def __init__(self, usuario_id, email, perfil_nombre, modulo_nombre):
        self.usuario_id = usuario_id
        self.email = email
        self.perfil_nombre = perfil_nombre
        self.modulo_nombre = modulo_nombre

    @staticmethod
    def obtener_perfiles_por_usuario_id(usuario_id):
        """
        Obtiene todos los perfiles asociados a un usuario_id específico.
        """
        try:
            # Obtener la conexión a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            # Ejecutar la consulta SQL para obtener los perfiles
            cursor.execute("SELECT * FROM usuarios_perfil WHERE usuario_id = ?", (usuario_id,))
            perfiles = cursor.fetchall()

            # Crear objetos de la clase Usuarios_Perfil con los datos obtenidos
            perfiles_lista = [
                Usuarios_Perfil(
                    perfil[0],  # usuario_id
                    perfil[1],  # email
                    perfil[4],  # perfil_nombre
                    perfil[6]   # modulo_nombre
                )
                for perfil in perfiles
            ]

            return perfiles_lista

        except Exception as e:
            raise Exception(f"Error al obtener perfiles: {str(e)}")
        
        finally:
            cursor.close()
            conn.close()
