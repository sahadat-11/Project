import mysql.connector

class DB_Connector:
    status = False

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='mdfahim',
                database='blood'
            )
            self.cursor = self.connection.cursor(dictionary=True, buffered=True)
            self.status = True
        except Exception as e:
            self.status = False
            print(f"Database connection failed: {e}")
