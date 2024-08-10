import psycopg2
from config import host, user, password, db_name


class Database:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()


try:
    db = Database(psycopg2.connect(host=host, user=user, password=password, database=db_name))
except:
    print("Error!")
else:
    print("Success!")
