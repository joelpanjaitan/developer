import MySQLdb

def get_data_connection():
    connectionData = None
    try:
        connectionData = MySQLdb.connect(
            host="localhost",
            user="root",
            password="password",
            db="api_db",
            port=3307,
        )
        print(f'connection is good')
    except MySQLdb.Error as e:
        print(f"Connection is error '${e}' occured")

    return connectionData

connection = get_data_connection()
