import psycopg2
from config import host, user, password, db_name


class Database:
    '''Database
    '''
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

        self.connection.autocommit = True

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def manageSuppliers(self, parameters):
        # Parameters: company_name, company_city, company_country, company_phone, company_homepage
        query = """INSERT INTO companies (company_name, company_city, company_country, company_phone, company_homepage)
                VALUES
                (%s, %s, %s, %s, %s)"""
        self.cursor.execute(query, parameters)
        query = "INSERT INTO suppliers (company_id) VALUES ((SELECT MAX(company_id) FROM companies))"
        self.cursor.execute(query)

    def clearTable(self, table):
        query = f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE"
        self.cursor.execute(query)

try:
    db = Database(psycopg2.connect(host=host, user=user, password=password, database=db_name))
except:
    print("Error!")
else:
    print("Success!")
