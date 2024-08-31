import sys
import psycopg2
from psycopg2 import sql
import datetime
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mainwindow import Ui_MainWindow
from authorizationwindow import Ui_Authorization
from config import host, user, password, db_name


class Database:
    """A class for interaction with postgresql database
    Attributes:
        productFilterDict   : dict - entered column and value for filtering products table
        copiedProduct       : list - selected product's parameters
        categoryFilterStr   : str - entered category name for filtering categories table
        companyFilterDict   : dict - entered column and value for filtering companies table
        copiedCompany       : list - selected company's parameters
        receiptFilterInt    : int - entered order number for filtering receipts table
        writeOffFilterInt   : int - entered order number for filtering write-offs table
        connection          : psycopg2.connection - connect to database
        cursor              : psycopg2.cursor - object to execute queries
    """

    def __init__(self, connection):
        self.productFilterDict = {}
        self.copiedProduct = []

        self.categoryFilterStr = ''

        self.companyFilterDict = {}
        self.copiedCompany = []

        self.receiptFilterInt = ''

        self.writeOffFilterInt = ''

        self.connection = connection
        self.cursor = connection.cursor()

        self.connection.autocommit = True

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def add_suppliers(self, parameters):
        # Parameters: company_name, company_city, company_country, company_phone, company_homepage
        query = """SELECT company_id FROM companies WHERE company_name = %s AND company_city = %s AND
                company_country = %s AND company_phone = %s AND company_homepage = %s"""
        self.cursor.execute(query, parameters)
        if self.cursor.fetchone() is None:
            query = """INSERT INTO companies (company_name, company_city, company_country, company_phone,
                    company_homepage) VALUES (%s, %s, %s, %s, %s);
                    INSERT INTO suppliers (company_id) VALUES ((SELECT MAX(company_id) FROM companies))"""
            self.cursor.execute(query, parameters)
        else:
            raise ValueError

    def delete_suppliers(self, parameters):
        # Parameters: company_name, company_city, company_country, company_phone, company_homepage
        # Get the index of the delete record
        query = """SELECT company_id FROM companies WHERE company_name = %s AND company_city = %s AND
                company_country = %s AND company_phone = %s AND company_homepage = %s"""
        self.cursor.execute(query, parameters)
        res = self.cursor.fetchone()[0]
        # Delete supplier and company
        query = f"""DELETE FROM suppliers WHERE supplier_id = %s;;
                DELETE FROM companies WHERE company_id = %s"""
        self.cursor.execute(query, (res, res))

    def edit_suppliers(self, parameters):
        query = """UPDATE companies SET company_name = %s, company_city = %s, company_country = %s, 
            company_phone = %s, company_homepage = %s
            WHERE company_name = %s AND company_city = %s AND company_country = %s AND 
            company_phone = %s AND company_homepage = %s"""
        self.cursor.execute(query, parameters)

    def clear_table(self, table):
        if table != 'suppliers':
            query = sql.SQL("TRUNCATE TABLE {} RESTART IDENTITY CASCADE").format(sql.Identifier(table))
        else:
            query = """TRUNCATE TABLE suppliers RESTART IDENTITY CASCADE;
                     TRUNCATE TABLE companies RESTART IDENTITY CASCADE"""
        self.cursor.execute(query)

    def update_products(self, product: tuple, action: str):
        """ Insert two records into 'product' when using edit: the first record is a new value,
        second is a changing record
        """
        if action == "add":
            query_select = """SELECT product_id FROM products
                    JOIN categories USING (category_id)
                    JOIN suppliers USING (supplier_id)
                    JOIN companies USING (company_id)
                    WHERE product_name = %s AND
                    freight = %s AND unit_price = %s AND units_in_stock = %s AND
                    category_name = %s AND company_name = %s"""
            self.cursor.execute(query_select, product)
            if self.cursor.fetchone() is None:
                # Get the category id
                query = "SELECT category_id FROM categories WHERE category_name = %s"
                self.cursor.execute(query, (product[4],))
                category_id = self.cursor.fetchone()[0]
                # Get the supplier id (company id)
                query = "SELECT company_id FROM companies WHERE company_name = %s"
                self.cursor.execute(query, (product[5],))
                company_id = self.cursor.fetchone()[0]
                # Update product parameters
                product = (product[0], product[1], product[2], product[3], category_id, company_id)

                query = """INSERT INTO products (product_name, freight, unit_price, units_in_stock, category_id,
                        supplier_id) VALUES (%s, %s, %s, %s, %s, %s)"""
            else:
                raise ValueError
        elif action == "edit":
            # Get the product id
            query = """SELECT product_id FROM products WHERE product_name = %s AND freight = %s AND unit_price = %s AND
                    units_in_stock = %s AND category_id = (SELECT category_id FROM categories
                    WHERE category_name = %s) AND supplier_id = (SELECT company_id FROM companies
                    WHERE company_name = %s)"""
            self.cursor.execute(query, product[:6])
            product_id = self.cursor.fetchone()[0]
            # Get the new category id
            query = "SELECT category_id FROM categories WHERE category_name = %s"
            self.cursor.execute(query, (product[10],))
            new_category_id = self.cursor.fetchone()[0]
            # Get the new company id
            query = "SELECT company_id FROM companies WHERE company_name = %s"
            self.cursor.execute(query, (product[11],))
            new_company_id = self.cursor.fetchone()[0]

            query = """UPDATE products SET product_name = %s, freight = %s, unit_price = %s,  
                    units_in_stock = %s, category_id = %s, supplier_id = %s
                    WHERE product_id = %s;"""
            product = (product[6], product[7], product[8], product[9], new_category_id, new_company_id, product_id)
        else:
            query = """DELETE FROM products 
                    WHERE product_id = (
                        SELECT product_id 
                        FROM products 
                        JOIN categories USING (category_id)
                        JOIN suppliers USING (supplier_id)
                        JOIN companies USING (company_id)
                        WHERE product_id = (SELECT MAX(product_id) FROM products) AND
                        product_name = %s AND freight = %s AND
                        unit_price = %s AND units_in_stock = %s AND
                        category_name = %s AND company_name = %s
                    )"""

        self.cursor.execute(query, product)

    def manage_categories(self, category, action):
        if action == "add":
            query = "INSERT INTO categories (category_name, category_description) VALUES (%s, %s)"
        else:
            query = "DELETE FROM categories WHERE category_name = %s AND category_description = %s"
        self.cursor.execute(query, category)

    def show_products(self, parameters):
        if len(parameters) == 0:
            query = """SELECT product_name, freight, unit_price, units_in_stock,
                    category_name, company_name FROM products 
                    JOIN categories USING (category_id)
                    JOIN suppliers USING (supplier_id)
                    JOIN companies USING (company_id)
                    ORDER BY product_id"""
        else:
            conditions = []
            for i in parameters:
                if parameters.get(i) != "":
                    string = "'" + parameters[i] + "'" if isinstance(parameters[i], str) else parameters[i]
                    conditions.append(f"{i} = {string}")
            query = """SELECT product_name, freight, unit_price, units_in_stock,
                                category_name, company_name FROM products 
                                JOIN categories USING (category_id)
                                JOIN suppliers USING (supplier_id)
                                JOIN companies USING (company_id) WHERE {0}
                                ORDER BY product_id""".format(' AND '.join(conditions))
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def show_suppliers(self, parameters):
        if len(parameters) == 0:
            query = """SELECT company_name, company_city, company_country, company_phone, company_homepage
                    FROM companies ORDER BY company_id"""
        else:
            conditions = []
            for i in parameters:
                if parameters.get(i) != "":
                    string = "'" + parameters[i] + "'"
                    conditions.append(f"{i} = {string}")
            query = """SELECT company_name, company_city, company_country, company_phone, company_homepage
                    FROM companies WHERE {0} ORDER BY company_id""".format(' AND '.join(conditions))
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def show_categories(self, name=""):
        if name:
            query = 'SELECT category_name, category_description FROM categories WHERE category_name = %s'
            self.cursor.execute(query, (name,))
        else:
            query = 'SELECT category_name, category_description FROM categories'
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def show_receipts(self, order_number):
        if not order_number:
            query = """SELECT order_number, order_date, product_name, amount, company_name
                    FROM receipts
                    JOIN products USING (product_id)
                    JOIN suppliers ON receipts.supplier_id = suppliers.supplier_id
                    JOIN companies USING (company_id)"""
            self.cursor.execute(query)
        else:
            query = """SELECT order_number, order_date, product_name, amount, company_name
                    FROM receipts
                    JOIN products USING (product_id)
                    JOIN suppliers ON receipts.supplier_id = suppliers.supplier_id
                    JOIN companies USING (company_id)
                    WHERE order_number = %s"""
            self.cursor.execute(query, (order_number,))
        return self.cursor.fetchall()

    def show_write_offs(self, order_number):
        if not order_number:
            query = """SELECT order_number, order_date, product_name, amount, reason
                    FROM write_offs
                    JOIN products USING (product_id)"""
            self.cursor.execute(query)
        else:
            query = """SELECT order_number, order_date, product_name, amount, reason
                    FROM write_offs
                    JOIN products USING (product_id)
                    WHERE order_number = %s"""
            self.cursor.execute(query, (order_number,))
        return self.cursor.fetchall()

    def show_managers(self):
        query = "SELECT manager_name, manager_surname, manager_middlename FROM managers"
        self.cursor.execute(query)
        return [f"{x[0]} {x[2]} {x[1]}" if x[2] else f"{x[0]} {x[1]}" for x in self.cursor.fetchall()]

    def get_users(self, username, user_password):
        query = "SELECT user_name, user_password FROM users WHERE user_name = %s AND user_password = %s"
        self.cursor.execute(query, (username, user_password))
        return True if len(self.cursor.fetchall()) != 0 else False

    def add_receipts(self, parameters):
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

    def cancel_receipt(self, order_number):
        query = """DELETE FROM receipts 
                WHERE order_number = %s"""
        self.cursor.execute(query, (order_number,))

    def add_write_offs(self, parameters):
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

    def cancel_write_off(self, order_number):
        query = """DELETE FROM write_offs
                WHERE order_number = %s"""
        self.cursor.execute(query, (order_number,))

    def inventory_movement_report(self, count, timeunit):
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
        actions = {'days': lambda x: x,
                   'months': lambda x: x * 30,
                   'years': lambda x: x * 365}
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
        for i in range(len(res) - 1):
            if res[i][0] == res[i + 1][0]:
                most_frequent_reasons.append(res[i])
            else:
                pass
        if len(most_frequent_reasons) > 0 and res[-1] != res[-2]:
            most_frequent_reasons.append(res[-1])
        query = """SELECT product_name, MAX(order_date), SUM(amount)
                FROM write_offs
                JOIN products USING(product_id)
                WHERE order_date >= (SELECT CURRENT_DATE - %s + 1)
                GROUP BY product_name"""
        self.cursor.execute(query, (count,))
        write_offs = self.cursor.fetchall()
        if len(res) > 1:
            write_offs = [list(write_offs[x]) + [most_frequent_reasons[x][1]] for x in range(len(write_offs))]
        else:
            write_offs = [list(write_offs[0]) + [res[0][1]]]
        # Generate the report
        res = []
        less = receipts if len(receipts) <= len(write_offs) else write_offs
        greater = receipts if len(receipts) > len(write_offs) else write_offs
        to_remove_from_less = []
        to_remove_from_greater = []
        # Add the full records
        for i in less:
            for j in greater:
                if i[0] == j[0]:
                    value = (i[0], i[1], j[1], i[2], j[2], i[3], j[3]) if less == receipts else \
                        (j[0], j[1], i[1], j[2], i[2], j[3], i[3])
                    res.append(value)
                    to_remove_from_less.append(i)
                    to_remove_from_greater.append(j)
        # Remove the matched items
        for i in to_remove_from_less:
            less.remove(i)
        for i in to_remove_from_greater:
            greater.remove(i)
        # Add the receipt only records
        for i in receipts:
            res.append((i[0], i[1], "-", i[2], 0, i[3], "-"))
        # Add the write-off only records
        for i in write_offs:
            res.append((i[0], "-", i[1], 0, i[2], "", i[3]))
        # Return the report
        return res

    def slob_inventory_report(self):
        query = """SELECT product_name, MAX(order_date), SUM(amount), unit_price*units_in_stock
                FROM write_offs
                JOIN products USING(product_id)
                GROUP BY product_name, unit_price, units_in_stock
                ORDER BY MAX(order_date)"""
        self.cursor.execute(query)
        return self.cursor.fetchall()


# Initialize Database object
db = Database(psycopg2.connect(host=host, user=user, password=password, database=db_name))

# Main window
app = QtWidgets.QApplication(sys.argv)
font = QtGui.QFont("Nunito")
app.setFont(font)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# Authorization window
Authorization = QtWidgets.QMainWindow()
uiAuthorize = Ui_Authorization()
uiAuthorize.setupUi(Authorization)
Authorization.show()


# Connection Database and GUI functions
def show_error(message):
    error = QMessageBox()
    error.setWindowTitle('Error!')
    error.setText(message)
    error.setIcon(QMessageBox.Critical)

    error.exec_()


def sign_in():
    username = uiAuthorize.usernamePTE.toPlainText()
    user_password = uiAuthorize.passwordLE.text()
    res = db.get_users(username, user_password)
    if res:
        MainWindow.show()
        Authorization.close()
    else:
        show_error("Invalid username and/or password!")


def output_products_gui():
    if ui.productFilterPTE.toPlainText():
        # Set the value
        value = float(ui.productFilterPTE.toPlainText()) if ui.productFilterPTE.toPlainText().isdigit() \
            else ui.productFilterPTE.toPlainText()
        # Add a tag to the dictionary
        db.productFilterDict[ui.productFilterCB.currentText().lower().replace(' ', '_')] = value
        # Add a tag text
        text = 'Tags | ' + str(db.productFilterDict).replace("'", "")[1:-1]
        ui.productsTagsLabel.setText(text)
        ui.productFilterPTE.setPlainText("")
    else:
        sqlquery = db.show_products(db.productFilterDict)
        populate_table(ui.productsTable, sqlquery, 6)


def output_categories_gui():
    if ui.categoryFilterPTE.toPlainText():
        db.categoryFilterStr = ui.categoryFilterPTE.toPlainText()
        # Add a tag text
        text = 'Category name: ' + ui.categoryFilterPTE.toPlainText()
        ui.categoriesTagsLabel.setText(text)
        ui.categoryFilterPTE.setPlainText("")
    else:
        sqlquery = db.show_categories(db.categoryFilterStr)
        populate_table(ui.categoriesTable, sqlquery, 2)


def output_companies_gui():
    if ui.companyFilterPTE.toPlainText():
        # Add a tag to the dictionary
        db.companyFilterDict[ui.companyFilterCB.currentText().lower().replace(' ', '_')] = \
            ui.companyFilterPTE.toPlainText()
        # Add a tag text
        text = 'Tags | ' + str(db.companyFilterDict).replace("'", "")[1:-1]
        ui.companiesTagsLabel.setText(text)
        ui.companyFilterPTE.setPlainText("")
    else:
        sqlquery = db.show_suppliers(db.companyFilterDict)
        populate_table(ui.companiesTable, sqlquery, 5)


def output_receipts_gui():
    if ui.receiptFilterPTE.toPlainText():
        try:
            db.receiptFilterInt = int(ui.receiptFilterPTE.toPlainText())
            # Add a tag text
            text = f'Order number: {ui.receiptFilterPTE.toPlainText()}'
            ui.receiptsTagsLabel.setText(text)
            ui.receiptFilterPTE.setPlainText("")
        except ValueError:
            show_error("The order number must not contain any symbols except for digits!")
    else:
        sqlquery = db.show_receipts(db.receiptFilterInt)
        populate_table(ui.receiptsTable, sqlquery, 5)


def output_write_offs_gui():
    if ui.writeoffFilterPTE.toPlainText():
        try:
            db.writeOffFilterInt = int(ui.writeoffFilterPTE.toPlainText())
            # Add a tag text
            text = f'Order number: {ui.writeoffFilterPTE.toPlainText()}'
            ui.writeoffsTagsLabel.setText(text)
            ui.writeoffFilterPTE.setPlainText("")
        except ValueError:
            ui.writeoffFilterPTE.setPlainText("")
            show_error("The order number must not contain any symbols except for digits!")
    else:
        sqlquery = db.show_write_offs(db.writeOffFilterInt)
        populate_table(ui.writeoffsTable, sqlquery, 5)


def output_inventory_movement_report_gui():
    try:
        parameters = get_inventory_movement_parameters_gui()
        sqlquery = db.inventory_movement_report(parameters[0], parameters[1])
        populate_table(ui.inventoryMovementTable, sqlquery, 7)
    except Exception as e:
        print(e)


def output_slob_report_gui():
    sqlquery = db.slob_inventory_report()
    populate_table(ui.SLOBTable, sqlquery, 4)


def clear_product_filter():
    db.productFilterDict = {}
    ui.productsTagsLabel.setText('Tags')
    output_products_gui()


def clear_category_filter():
    db.categoryFilterStr = ""
    ui.categoriesTagsLabel.setText('Category name:')
    output_categories_gui()


def clear_company_filter():
    db.companyFilterDict = {}
    ui.companiesTagsLabel.setText('Tags')
    output_companies_gui()


def clear_receipt_filter():
    db.receiptFilterInt = ""
    ui.receiptsTagsLabel.setText('Order number: ')
    output_receipts_gui()


def clear_write_off_filter():
    db.writeOffFilterInt = ""
    ui.writeoffsTagsLabel.setText('Order number: ')
    output_write_offs_gui()


def truncate_table_gui(table, funcs):
    db.clear_table(table)
    for func in funcs:
        func()


def get_product_parameters_gui():
    return (
        ui.productNamePTE.toPlainText(),
        float(ui.freightPTE.toPlainText()),
        float(ui.unitPricePTE.toPlainText()),
        float(ui.unitsInStockPTE.toPlainText()),
        ui.productsCategoryPTE.toPlainText(),
        ui.productsSupplierPTE.toPlainText()
    )


def get_category_parameters_gui():
    return (
        ui.categoryNamePTE.toPlainText(),
        ui.categoryDescriptionPTE.toPlainText()
    )


def get_company_parameters_gui():
    return (
        ui.companyNamePTE.toPlainText(),
        ui.cityPTE.toPlainText(),
        ui.countryPTE.toPlainText(),
        ui.phonePTE.toPlainText(),
        ui.homepagePTE.toPlainText()
    )


def get_receipt_parameters_gui():
    date = datetime.datetime.strptime(ui.receiptOrderDatePTE.toPlainText(), '%Y-%m-%d').date()
    return (
        int(ui.receiptOrderNumberPTE.toPlainText()),
        date,
        ui.receiptProductNamePTE.toPlainText(),
        int(ui.receiptAmountPTE.toPlainText()),
        ui.receiptSupplierPTE.toPlainText()
    )


def get_write_off_parameters_gui():
    date = datetime.datetime.strptime(ui.writeoffOrderDatePTE.toPlainText(), '%Y-%m-%d').date()
    return (
        int(ui.writeoffOrderNumberPTE.toPlainText()),
        date,
        ui.writeoffProductNamePTE.toPlainText(),
        int(ui.writeoffAmountPTE.toPlainText()),
        ui.writeoffReasonPTE.toPlainText()
    )


def get_inventory_movement_parameters_gui():
    return (
        int(ui.IMTimePeriodPTE.toPlainText()),
        ui.IMTimeUnitCB.currentText().lower()
    )


def copy_product_gui(row):
    items = [ui.productsTable.item(row, col).text() for col in range(ui.productsTable.columnCount())]
    text_fields = (ui.productNamePTE, ui.freightPTE, ui.unitPricePTE, ui.unitsInStockPTE,
                   ui.productsCategoryPTE, ui.productsSupplierPTE)
    db.copiedProduct = tuple(items)
    for i in range(len(text_fields)):
        text_fields[i].setPlainText(items[i])


def copy_category_gui(row):
    items = [ui.categoriesTable.item(row, col).text() for col in range(ui.categoriesTable.columnCount())]
    text_fields = (ui.categoryNamePTE, ui.categoryDescriptionPTE)
    for i in range(len(text_fields)):
        text_fields[i].setPlainText(items[i])


def copy_company_gui(row):
    items = [ui.companiesTable.item(row, col).text() for col in range(ui.companiesTable.columnCount())]
    text_fields = (ui.companyNamePTE, ui.cityPTE, ui.countryPTE, ui.phonePTE, ui.homepagePTE)
    db.copiedCompany = tuple(items)
    for i in range(len(text_fields)):
        text_fields[i].setPlainText(items[i])


def copy_receipt_gui(row):
    items = [ui.receiptsTable.item(row, col).text() for col in range(ui.receiptsTable.columnCount())]
    text_fields = (ui.receiptOrderNumberPTE, ui.receiptOrderDatePTE, ui.receiptProductNamePTE,
                   ui.receiptAmountPTE, ui.receiptSupplierPTE)
    for i in range(len(text_fields)):
        text_fields[i].setPlainText(items[i])


def copy_write_off_gui(row):
    items = [ui.writeoffsTable.item(row, col).text() for col in range(ui.writeoffsTable.columnCount())]
    text_fields = (ui.writeoffOrderNumberPTE, ui.writeoffOrderDatePTE, ui.writeoffProductNamePTE,
                   ui.writeoffAmountPTE, ui.writeoffReasonPTE)
    for i in range(len(text_fields)):
        text_fields[i].setPlainText(items[i])


def copy_slob_gui(row):
    items = [ui.SLOBTable.item(row, col).text() for col in range(ui.SLOBTable.columnCount())]
    if ui.SLOBProductsPTE.toPlainText():
        text = ui.SLOBProductsPTE.toPlainText() + ', ' + items[0]
    else:
        text = items[0]
    ui.SLOBProductsPTE.setPlainText(text)


def add_product_gui():
    try:
        product = get_product_parameters_gui()
        db.update_products(product, 'add')
        output_products_gui()
    except TypeError:
        show_error("It is not possible to add a product with a non-existent category and/or company!")


def add_category_gui():
    category = get_category_parameters_gui()
    db.manage_categories(category, 'add')
    output_categories_gui()


def add_company_gui():
    try:
        company = get_company_parameters_gui()
        db.add_suppliers(company)
        output_companies_gui()
    except ValueError:
        show_error("A company with the same parameters already exists!")


def confirm_receipt_gui():
    try:
        receipt = get_receipt_parameters_gui()
        db.add_receipts(receipt)
        output_receipts_gui()
    except ValueError as e:
        error_message = str(e)
        if 'time data' in error_message:
            show_error("Incorrect time data! Should be YYYY-MM-DD (Year-Month-Day)!")
        else:
            show_error("The order number and the amount must not contain any symbols except digits!")
    except TypeError:
        show_error("It is not possible to confirm a receipt with a non-existent product and/or supplier!")


def confirm_write_off_gui():
    try:
        write_off = get_write_off_parameters_gui()
        db.add_write_offs(write_off)
        output_write_offs_gui()
    except ValueError as e:
        error_message = str(e)
        if 'time data' in error_message:
            show_error("Incorrect time data! Should be YYYY-MM-DD (Year-Month-Day)!")
        else:
            show_error("The order number and the amount must not contain any symbols except digits!")
    except TypeError:
        show_error("It is not possible to confirm a write-off with a non-existent product and/or supplier!")


def del_product_gui():
    try:
        product = get_product_parameters_gui()
        db.update_products(product, 'delete')
        output_products_gui()
    except Exception as e:
        print(e)


def del_category_gui():
    try:
        category = get_category_parameters_gui()
        db.manage_categories(category, 'delete')
        output_categories_gui()
    except psycopg2.Error:
        show_error("You first need to change the category in the other tables before deleting the category!")


def del_company_gui():
    try:
        company = get_company_parameters_gui()
        db.delete_suppliers(company)
        output_companies_gui()
    except psycopg2.Error:
        show_error("You first need to change the company in the other tables before deleting the company!")
    except TypeError:
        show_error("No company meet these parameters!")


def cancel_receipt_gui():
    receipt = get_receipt_parameters_gui()
    db.cancel_receipt(receipt[0])
    output_receipts_gui()


def cancel_write_off_gui():
    write_off = get_write_off_parameters_gui()
    db.cancel_write_off(write_off[0])
    output_write_offs_gui()


def chg_product_gui():
    old_parameters = tuple(db.copiedProduct)
    new_parameters = get_product_parameters_gui()
    db.update_products((old_parameters+new_parameters), 'edit')
    output_products_gui()


def chg_company_gui():
    old_parameters = tuple(db.copiedCompany)
    new_parameters = get_company_parameters_gui()
    db.edit_suppliers(new_parameters+old_parameters)
    output_companies_gui()


def populate_table(table, data, column_count):
    table.setRowCount(len(data))
    for row_index, row_data in enumerate(data):
        for column_index in range(column_count):
            table.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(row_data[column_index])))


# Populate tables
output_products_gui()
output_categories_gui()
output_companies_gui()
output_receipts_gui()
output_write_offs_gui()
output_slob_report_gui()

# Add items to combo box
ui.IMManagerCB.addItems(db.show_managers())
ui.SLOBManagerCB.addItems(db.show_managers())

# Modulate main window
ui.productFilterBtn.clicked.connect(lambda: output_products_gui())
ui.productFilterClearBtn.clicked.connect(lambda: clear_product_filter())
ui.productsTruncateBtn.clicked.connect(lambda: truncate_table_gui('products', (output_products_gui, output_receipts_gui,
                                                                               output_write_offs_gui)))
ui.addProductBtn.clicked.connect(lambda: add_product_gui())
ui.delProductBtn.clicked.connect(lambda: del_product_gui())
ui.chgProductBtn.clicked.connect(lambda: chg_product_gui())
ui.productsTable.verticalHeader().sectionClicked.connect(copy_product_gui)

ui.categoryFilterBtn.clicked.connect(lambda: output_categories_gui())
ui.categoryFilterClearBtn.clicked.connect(lambda: clear_category_filter())
ui.categoriesTruncateBtn.clicked.connect(lambda: truncate_table_gui('categories', (output_categories_gui,
                                                                                   output_products_gui,
                                                                                   output_receipts_gui,
                                                                                   output_write_offs_gui)))
ui.addCategoryBtn.clicked.connect(lambda: add_category_gui())
ui.delCategoryBtn.clicked.connect(lambda: del_category_gui())
ui.categoriesTable.verticalHeader().sectionClicked.connect(copy_category_gui)

ui.companyFilterBtn.clicked.connect(lambda: output_companies_gui())
ui.companyFilterClearBtn.clicked.connect(lambda: clear_company_filter())
ui.companiesTruncateBtn.clicked.connect(lambda: truncate_table_gui('companies', (output_companies_gui,
                                                                                 output_products_gui)))
ui.addCompanyBtn.clicked.connect(lambda: add_company_gui())
ui.delCompanyBtn.clicked.connect(lambda: del_company_gui())
ui.chgCompanyBtn.clicked.connect(lambda: chg_company_gui())
ui.companiesTable.verticalHeader().sectionClicked.connect(copy_company_gui)

ui.receiptFilterBtn.clicked.connect(lambda: output_receipts_gui())
ui.receiptFilterClearBtn.clicked.connect(lambda: clear_receipt_filter())
ui.receiptsTruncateBtn.clicked.connect(lambda: truncate_table_gui('receipts', (output_receipts_gui,
                                                                               output_products_gui)))
ui.receiptConfirmBtn.clicked.connect(lambda: confirm_receipt_gui())
ui.receiptCancelBtn.clicked.connect(lambda: cancel_receipt_gui())
ui.receiptsTable.verticalHeader().sectionClicked.connect(copy_receipt_gui)

ui.writeoffFilterBtn.clicked.connect(lambda: output_write_offs_gui())
ui.writeoffFilterClearBtn.clicked.connect(lambda: clear_write_off_filter())
ui.writeOffsTruncateBtn.clicked.connect(lambda: truncate_table_gui('write_offs', (output_receipts_gui,
                                                                                  output_products_gui)))
ui.writeoffConfirm.clicked.connect(lambda: confirm_write_off_gui())
ui.writeoffCancel.clicked.connect(lambda: cancel_write_off_gui())
ui.writeoffsTable.verticalHeader().sectionClicked.connect(copy_write_off_gui)

ui.IMViewBtn.clicked.connect(lambda: output_inventory_movement_report_gui())

ui.SLOBTable.verticalHeader().sectionClicked.connect(copy_slob_gui)

# Modulate authorization window
uiAuthorize.loginBtn.clicked.connect(lambda: sign_in())

sys.exit(app.exec_())
