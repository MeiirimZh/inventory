import sys
import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
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

    def editSuppliers(self, parameters: tuple):
        query = """UPDATE companies SET company_name = %s, company_city = %s, company_country = %s, 
            company_phone = %s, company_homepage = %s
            WHERE company_name = %s AND company_city = %s AND company_country = %s AND 
            company_phone = %s AND company_homepage = %s"""
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
            query = """UPDATE products SET product_name = %s, freight = %s, unit_price = %s,  
                    units_in_stock = %s, category_id = %s, supplier_id = %s 
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

    def showCategories(self):
        query = 'SELECT category_name, category_description FROM categories'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def addReceipts(self, parameters):
        # Get the product_id
        query = "SELECT product_id FROM products WHERE product_name = %s"
        self.cursor.execute(query, (parameters[2],))
        product_id = self.cursor.fetchone()[0]
        # Get the supplier_id
        query = "SELECT supplier_id FROM products WHERE product_id = %s"
        self.cursor.execute(query, (product_id,))
        supplier_id = self.cursor.fetchone()[0]
        # Set the new parameters
        new_parameters = parameters[:2] + (product_id,) + (parameters[3],) + (supplier_id,)
        # Add the receipt
        query = """INSERT INTO receipts (order_number, order_date, product_id, amount, supplier_id)
                VALUES
                (%s, %s, %s, %s, %s)"""
        self.cursor.execute(query, new_parameters)

    def cancelReceipt(self, order_number):
        query = """DELETE FROM receipts 
                WHERE order_number = %s"""
        self.cursor.execute(query, (order_number,))

    def addWriteOffs(self, parameters):
        # Get the product_id
        query = "SELECT product_id FROM products WHERE product_name = %s"
        self.cursor.execute(query, (parameters[2],))
        product_id = self.cursor.fetchone()[0]
        # Set the new parameters
        new_parameters = parameters[:2] + (product_id,) + parameters[3:]
        # Add the write-off
        query = """INSERT INTO write_offs (order_number, order_date, product_id, amount, reason)
                VALUES
                (%s, %s, %s, %s, %s)"""
        self.cursor.execute(query, new_parameters)

    def cancelWriteOff(self, order_number):
        query = """DELETE FROM write_offs
                WHERE order_number = %s"""
        self.cursor.execute(query, (order_number,))

    def inventoryMovementReport(self, count, timeunit):
        """Return data description:
        1 - product name;
        2 - last receipt date;
        3 - last write-off date;
        4 - total receipt amount;
        5 - total write-off amount;
        6 - receipt supplier;
        7 - write-off's most frequent reason;
        """
        # Convert count to days
        actions = {'days': lambda x: count, 'months': lambda x: count*30, 'years': lambda x: count*365}
        action = actions.get(timeunit)
        count = action(count)
        # Get the receipts
        query = """SELECT product_name, MAX(order_date), SUM(amount), company_name
                FROM receipts
                JOIN products USING(product_id)
                JOIN suppliers ON receipts.supplier_id = suppliers.supplier_id
                JOIN companies USING(company_id)
                WHERE order_date >= (SELECT CURRENT_DATE - %s + 1)
                GROUP BY product_name, company_name"""
        self.cursor.execute(query, (count,))
        receipts = self.cursor.fetchall()
        # Get the most frequent reasons
        query = """SELECT product_id, reason, COUNT(*)
                FROM write_offs
                GROUP BY product_id, reason
                ORDER BY product_id, COUNT(*) DESC"""
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        most_frequent_reasons = []
        for i in range(len(res)-1):
            if res[i][0] == res[i+1][0]:
                most_frequent_reasons.append(res[i])
            else:
                pass
        if res[-1] != res[-2]:
            most_frequent_reasons.append(res[-1])
        # Get the write-offs
        query = """SELECT product_name, MAX(order_date), SUM(amount)
                FROM write_offs
                JOIN products USING(product_id)
                WHERE order_date >= (SELECT CURRENT_DATE - %s + 1)
                GROUP BY product_name"""
        self.cursor.execute(query, (count,))
        write_offs = self.cursor.fetchall()
        write_offs = tuple([list(write_offs[x])+[most_frequent_reasons[x][1]] for x in range(len(write_offs))])
        # Return the report result
        return [(receipts[x][0], receipts[x][1], write_offs[x][1],
                 receipts[x][2], write_offs[x][2], receipts[x][3], write_offs[x][3]) for x in range(len(receipts))]

    def SLOBInventoryReport(self):
        query = """SELECT product_name, MAX(order_date), SUM(amount), unit_price*units_in_stock
                FROM write_offs
                JOIN products USING(product_id)
                GROUP BY product_name, unit_price, units_in_stock
                ORDER BY MAX(order_date)"""
        self.cursor.execute(query)
        return self.cursor.fetchall()


app = QtWidgets.QApplication(sys.argv)
font = QtGui.QFont("Nunito")
app.setFont(font)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
