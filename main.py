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

    def addSuppliers(self, parameters):
        # Parameters: company_name, company_city, company_country, company_phone, company_homepage
        query = """SELECT company_id FROM companies WHERE company_name = %s AND company_city = %s AND
                company_country = %s AND company_phone = %s AND company_homepage = %s"""
        self.cursor.execute(query, parameters)
        if self.cursor.fetchone() is None:
            query = """INSERT INTO companies (company_name, company_city, company_country, company_phone,
                    company_homepage) VALUES (%s, %s, %s, %s, %s)"""
            self.cursor.execute(query, parameters)
            query = "INSERT INTO suppliers (company_id) VALUES ((SELECT MAX(company_id) FROM companies))"
            self.cursor.execute(query)
        else:
            raise ValueError

    def deleteSuppliers(self, parameters):
        # Parameters: company_name, company_city, company_country, company_phone, company_homepage
        # Get the index of the delete record
        query = """SELECT company_id FROM companies WHERE company_name = %s AND company_city = %s AND
                company_country = %s AND company_phone = %s AND company_homepage = %s"""
        self.cursor.execute(query, parameters)
        res = self.cursor.fetchone()[0]
        # Delete supplier
        query = f"""DELETE FROM suppliers WHERE supplier_id = {res}"""
        self.cursor.execute(query)
        # Delete company
        query = """DELETE FROM companies WHERE company_name = %s AND company_city = %s AND
                company_country = %s AND company_phone = %s AND company_homepage = %s"""
        self.cursor.execute(query, parameters)

    def clearTable(self, table):
        query = f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE"
        self.cursor.execute(query)

    def updateProducts(self, product: tuple, action: str):
        """ Insert two records into 'product' when using edit: the first record is a new value,
        second is a changing record
        """
        if action == "add":
            query_select = """SELECT product_id FROM products WHERE product_name = %s AND
                     freight = %s AND unit_price = %s AND units_in_stock = %s AND
                     category_id = %s AND supplier_id = %s"""
            self.cursor.execute(query_select, product)
            if self.cursor.fetchone() is None:
                query = """INSERT INTO products (product_name, freight, unit_price, units_in_stock, category_id,
                        supplier_id) VALUES (%s, %s, %s, %s, %s, %s)"""
            else:
                raise ValueError
        elif action == "edit":
            query = """ALTER TABLE products
                    SET product_name = %s AND freight = %s AND unit_price = %s AND 
                    units_in_stock = %s AND category_id = %s AND supplier_id = %s
                    WHERE product_name = %s AND freight = %s AND unit_price = %s AND
                    units_in_stock = %s AND category_id = %s AND supplier_id = %s"""
        else:
            query = """DELETE FROM products WHERE product_id = (SELECT MAX(product_id) FROM products) AND
                    product_name = %s AND freight = %s AND
                    unit_price = %s AND units_in_stock = %s AND
                    category_id = %s AND supplier_id = %s"""

        self.cursor.execute(query, product)

    def manageCategories(self, category, action):
        if action == "add":
            query = "INSERT INTO categories (category_name, category_description) VALUES (%s, %s)"
        else:
            query = "DELETE FROM categories WHERE category_name = %s AND category_description = %s"
        self.cursor.execute(query, category)

    def showProducts(self, parameters=()):
        columns = ['product_name', 'freight', 'unit_price', 'units_in_stock', 'category_id', 'supplier_id']
        notEmptyColumns = [x for x in parameters if x != ""]
        if len(notEmptyColumns) > 0:
            query = ('SELECT product_name, freight, unit_price, units_in_stock,'
                     'category_name, company_name FROM products'
                     'JOIN categories USING (category_id)'
                     'JOIN suppliers USING (supplier_id)'
                     'JOIN companies USING (company_id)'
                     'WHERE {0} = %s').format(
                ' = %s AND '.join([columns[x] for x in range(6) if parameters[x] != ""]))
            self.cursor.execute(query, tuple(notEmptyColumns))
        else:
            query = ('SELECT product_name, freight, unit_price, units_in_stock,'
                     'category_name, company_name FROM products '
                     'JOIN categories USING (category_id)'
                     'JOIN suppliers USING (supplier_id)'
                     'JOIN companies USING (company_id)')
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def showSuppliers(self, parameters=()):
        columns = ['company_name', 'company_city', 'company_country', 'company_phone', 'company_homepage']
        notEmptyColumns = [x for x in parameters if x != ""]
        if len(notEmptyColumns) > 0:
            query = ('SELECT company_name, company_city, company_country, company_phone,'
                     'company_homepage FROM companies WHERE {0} = %s').format(
                ' = %s AND '.join([columns[x] for x in range(5) if parameters[x] != ""]))
            self.cursor.execute(query, tuple(notEmptyColumns))
        else:
            query = ('SELECT company_name, company_city, company_country,'
                     'company_phone, company_homepage FROM companies')
            self.cursor.execute(query)
        return self.cursor.fetchall()


# try:
db = Database(psycopg2.connect(host=host, user=user, password=password, database=db_name))
print(db.showProducts())
# except:
#     print("Error!")
# else:
#     print("Success!")
