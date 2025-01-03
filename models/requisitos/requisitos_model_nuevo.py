from database.db_admin_tramites import get_db_connection


class Requisitos_Nuevo:
    def __init__(self, uuid, id_area, valor, etiqueta, codigo, descripcion, id_tarifa, activo, estatus, usuario_creado, fecha_creado, fecha_eliminado, tipo, valor_seccion, descripcion_seccion, fila, activo_seccion, estatus_seccion, usuario_creado_seccion, fecha_creado_seccion, fecha_eliminado_seccion):
        self.uuid = uuid
        self.id_area = id_area
        self.valor = valor
        self.etiqueta = etiqueta
        self.codigo = codigo
        self.descripcion = descripcion
        self.id_tarifa = id_tarifa
        self.activo = activo
        self.estatus = estatus
        self.usuario_creado = usuario_creado
        self.fecha_creado = fecha_creado
        self.fecha_eliminado = fecha_eliminado
        self.tipo = tipo
        self.valor_seccion = valor_seccion
        self.descripcion_seccion = descripcion_seccion
        self.fila = fila
        self.activo_seccion = activo_seccion
        self.estatus_seccion = estatus_seccion
        self.usuario_creado_seccion = usuario_creado_seccion
        self.fecha_creado_seccion = fecha_creado_seccion
        self.fecha_eliminado_seccion = fecha_eliminado_seccion

    @staticmethod
    def nuevo_requisitos(uuid, id_area, valor, etiqueta, codigo, descripcion, id_tarifa, activo, estatus, usuario_creado, fecha_creado, fecha_eliminado, tipo, valor_seccion, descripcion_seccion, fila, activo_seccion, estatus_seccion, usuario_creado_seccion, fecha_creado_seccion, fecha_eliminado_seccion):
        """
        Inserta un nuevo requisito y sección en la base de datos (SQL Server) como una transacción.
        """
        try:
            # Obtener la conexión a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            # Consulta SQL para la transacción
            sql = """
            BEGIN TRANSACTION;
            INSERT INTO cat_requisitos (uuid, id_area, valor, etiqueta, codigo, descripcion, id_tarifa, activo, estatus, usuario_creado, fecha_creado, fecha_eliminado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            DECLARE @id_insertado INT = SCOPE_IDENTITY();
            INSERT INTO cat_secciones (cat_id, tipo, valor, descripcion, fila, activo, estatus, usuario_creado, fecha_creado, fecha_eliminado)
            VALUES (@id_insertado, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            COMMIT TRANSACTION;
            """
            # Ejecutar la consulta con los parámetros
            cursor.execute(sql, (
                uuid, id_area, valor, etiqueta, codigo, descripcion, id_tarifa, activo, estatus, usuario_creado, fecha_creado, fecha_eliminado,
                tipo, valor_seccion, descripcion_seccion, fila, activo_seccion, estatus_seccion, usuario_creado_seccion, fecha_creado_seccion, fecha_eliminado_seccion
            ))

            # Confirmar los cambios
            conn.commit()

            return True  # Inserción exitosa

        except Exception as e:
            if conn:
                conn.rollback()  # Revertir en caso de error
            raise Exception(f"Error al insertar requisito y sección: {str(e)}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
