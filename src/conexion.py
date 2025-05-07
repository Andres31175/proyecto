import psycopg2

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='3117590566',
        database='proyect',
        port='5432'
    )
    print("Conexión exitosa")
except Exception as ex:
    print("Error al conectar a la base de datos:")
    print(type(ex).__name__, ex)
