import pyodbc

def get_db_connection():
    """
    Devuelve una nueva conexión a la base de datos.
    """
    conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=vuamm1.database.windows.net;DATABASE=admin_tramites;UID=carlos2025;PWD=1231#ASDF!a'
    conn = pyodbc.connect(conn_string)
    return conn