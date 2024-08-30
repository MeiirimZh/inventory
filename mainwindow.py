from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(20, 18, 41);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.productsTab = QtWidgets.QWidget()
        self.productsTab.setObjectName("productsTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.productsTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.productFilterCB = QtWidgets.QComboBox(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productFilterCB.sizePolicy().hasHeightForWidth())
        self.productFilterCB.setSizePolicy(sizePolicy)
        self.productFilterCB.setMinimumSize(QtCore.QSize(100, 0))
        self.productFilterCB.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productFilterCB.setFont(font)
        self.productFilterCB.setStyleSheet("background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"border-radius: 5px;\n"
"text-align: center;")
        self.productFilterCB.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.productFilterCB.setFrame(False)
        self.productFilterCB.setObjectName("productFilterCB")
        self.productFilterCB.addItem("")
        self.productFilterCB.addItem("")
        self.productFilterCB.addItem("")
        self.productFilterCB.addItem("")
        self.productFilterCB.addItem("")
        self.productFilterCB.addItem("")
        self.horizontalLayout.addWidget(self.productFilterCB)
        self.productFilterPTE = QtWidgets.QPlainTextEdit(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productFilterPTE.sizePolicy().hasHeightForWidth())
        self.productFilterPTE.setSizePolicy(sizePolicy)
        self.productFilterPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productFilterPTE.setFont(font)
        self.productFilterPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.productFilterPTE.setObjectName("productFilterPTE")
        self.horizontalLayout.addWidget(self.productFilterPTE)
        self.productFilterBtn = QtWidgets.QPushButton(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productFilterBtn.sizePolicy().hasHeightForWidth())
        self.productFilterBtn.setSizePolicy(sizePolicy)
        self.productFilterBtn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productFilterBtn.setFont(font)
        self.productFilterBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.productFilterBtn.setFlat(False)
        self.productFilterBtn.setObjectName("productFilterBtn")
        self.horizontalLayout.addWidget(self.productFilterBtn)
        self.productFilterClearBtn = QtWidgets.QPushButton(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productFilterClearBtn.sizePolicy().hasHeightForWidth())
        self.productFilterClearBtn.setSizePolicy(sizePolicy)
        self.productFilterClearBtn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productFilterClearBtn.setFont(font)
        self.productFilterClearBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.productFilterClearBtn.setObjectName("productFilterClearBtn")
        self.horizontalLayout.addWidget(self.productFilterClearBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.productsTagsLabel = QtWidgets.QLabel(self.productsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productsTagsLabel.setFont(font)
        self.productsTagsLabel.setObjectName("productsTagsLabel")
        self.verticalLayout_2.addWidget(self.productsTagsLabel)
        self.productsTable = QtWidgets.QTableWidget(self.productsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productsTable.setFont(font)
        self.productsTable.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"}")
        self.productsTable.setObjectName("productsTable")
        self.productsTable.setColumnCount(6)
        self.productsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(5, item)
        self.verticalLayout_2.addWidget(self.productsTable)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.productNamePTE = QtWidgets.QPlainTextEdit(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productNamePTE.sizePolicy().hasHeightForWidth())
        self.productNamePTE.setSizePolicy(sizePolicy)
        self.productNamePTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productNamePTE.setFont(font)
        self.productNamePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.productNamePTE.setObjectName("productNamePTE")
        self.gridLayout.addWidget(self.productNamePTE, 0, 1, 1, 1)
        self.unitsInStockPTE = QtWidgets.QPlainTextEdit(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unitsInStockPTE.sizePolicy().hasHeightForWidth())
        self.unitsInStockPTE.setSizePolicy(sizePolicy)
        self.unitsInStockPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unitsInStockPTE.setFont(font)
        self.unitsInStockPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.unitsInStockPTE.setObjectName("unitsInStockPTE")
        self.gridLayout.addWidget(self.unitsInStockPTE, 3, 1, 1, 1)
        self.productNameLabel = QtWidgets.QLabel(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productNameLabel.sizePolicy().hasHeightForWidth())
        self.productNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productNameLabel.setFont(font)
        self.productNameLabel.setObjectName("productNameLabel")
        self.gridLayout.addWidget(self.productNameLabel, 0, 0, 1, 1)
        self.addProductBtn = QtWidgets.QPushButton(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addProductBtn.sizePolicy().hasHeightForWidth())
        self.addProductBtn.setSizePolicy(sizePolicy)
        self.addProductBtn.setMinimumSize(QtCore.QSize(80, 0))
        self.addProductBtn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addProductBtn.setFont(font)
        self.addProductBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.addProductBtn.setObjectName("addProductBtn")
        self.gridLayout.addWidget(self.addProductBtn, 0, 2, 1, 1)
        self.delProductBtn = QtWidgets.QPushButton(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delProductBtn.sizePolicy().hasHeightForWidth())
        self.delProductBtn.setSizePolicy(sizePolicy)
        self.delProductBtn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delProductBtn.setFont(font)
        self.delProductBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.delProductBtn.setObjectName("delProductBtn")
        self.gridLayout.addWidget(self.delProductBtn, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.unitPriceLabel = QtWidgets.QLabel(self.productsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unitPriceLabel.setFont(font)
        self.unitPriceLabel.setObjectName("unitPriceLabel")
        self.gridLayout.addWidget(self.unitPriceLabel, 2, 0, 1, 1)
        self.freightLabel = QtWidgets.QLabel(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freightLabel.sizePolicy().hasHeightForWidth())
        self.freightLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.freightLabel.setFont(font)
        self.freightLabel.setObjectName("freightLabel")
        self.gridLayout.addWidget(self.freightLabel, 1, 0, 1, 1)
        self.freightPTE = QtWidgets.QPlainTextEdit(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freightPTE.sizePolicy().hasHeightForWidth())
        self.freightPTE.setSizePolicy(sizePolicy)
        self.freightPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.freightPTE.setFont(font)
        self.freightPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.freightPTE.setObjectName("freightPTE")
        self.gridLayout.addWidget(self.freightPTE, 1, 1, 1, 1)
        self.unitPricePTE = QtWidgets.QPlainTextEdit(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unitPricePTE.sizePolicy().hasHeightForWidth())
        self.unitPricePTE.setSizePolicy(sizePolicy)
        self.unitPricePTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unitPricePTE.setFont(font)
        self.unitPricePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.unitPricePTE.setObjectName("unitPricePTE")
        self.gridLayout.addWidget(self.unitPricePTE, 2, 1, 1, 1)
        self.chgProductBtn = QtWidgets.QPushButton(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chgProductBtn.sizePolicy().hasHeightForWidth())
        self.chgProductBtn.setSizePolicy(sizePolicy)
        self.chgProductBtn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chgProductBtn.setFont(font)
        self.chgProductBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.chgProductBtn.setObjectName("chgProductBtn")
        self.gridLayout.addWidget(self.chgProductBtn, 2, 2, 1, 1)
        self.unitsInStockLabel = QtWidgets.QLabel(self.productsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unitsInStockLabel.setFont(font)
        self.unitsInStockLabel.setObjectName("unitsInStockLabel")
        self.gridLayout.addWidget(self.unitsInStockLabel, 3, 0, 1, 1)
        self.categoryLabel = QtWidgets.QLabel(self.productsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setObjectName("categoryLabel")
        self.gridLayout.addWidget(self.categoryLabel, 4, 0, 1, 1)
        self.productsCategoryPTE = QtWidgets.QPlainTextEdit(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productsCategoryPTE.sizePolicy().hasHeightForWidth())
        self.productsCategoryPTE.setSizePolicy(sizePolicy)
        self.productsCategoryPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productsCategoryPTE.setFont(font)
        self.productsCategoryPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.productsCategoryPTE.setObjectName("productsCategoryPTE")
        self.gridLayout.addWidget(self.productsCategoryPTE, 4, 1, 1, 1)
        self.supplierLabel = QtWidgets.QLabel(self.productsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.supplierLabel.setFont(font)
        self.supplierLabel.setObjectName("supplierLabel")
        self.gridLayout.addWidget(self.supplierLabel, 5, 0, 1, 1)
        self.productsSupplierPTE = QtWidgets.QPlainTextEdit(self.productsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productsSupplierPTE.sizePolicy().hasHeightForWidth())
        self.productsSupplierPTE.setSizePolicy(sizePolicy)
        self.productsSupplierPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productsSupplierPTE.setFont(font)
        self.productsSupplierPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.productsSupplierPTE.setObjectName("productsSupplierPTE")
        self.gridLayout.addWidget(self.productsSupplierPTE, 5, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Inkscape files/Inventory/ShoppingCart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.productsTab, icon, "")
        self.categoriesTab = QtWidgets.QWidget()
        self.categoriesTab.setObjectName("categoriesTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.categoriesTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.categoryFilterPTE = QtWidgets.QPlainTextEdit(self.categoriesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryFilterPTE.sizePolicy().hasHeightForWidth())
        self.categoryFilterPTE.setSizePolicy(sizePolicy)
        self.categoryFilterPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoryFilterPTE.setFont(font)
        self.categoryFilterPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.categoryFilterPTE.setObjectName("categoryFilterPTE")
        self.horizontalLayout_2.addWidget(self.categoryFilterPTE)
        self.categoryFilterBtn = QtWidgets.QPushButton(self.categoriesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryFilterBtn.sizePolicy().hasHeightForWidth())
        self.categoryFilterBtn.setSizePolicy(sizePolicy)
        self.categoryFilterBtn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoryFilterBtn.setFont(font)
        self.categoryFilterBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.categoryFilterBtn.setObjectName("categoryFilterBtn")
        self.horizontalLayout_2.addWidget(self.categoryFilterBtn)
        self.categoryFilterClearBtn = QtWidgets.QPushButton(self.categoriesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryFilterClearBtn.sizePolicy().hasHeightForWidth())
        self.categoryFilterClearBtn.setSizePolicy(sizePolicy)
        self.categoryFilterClearBtn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoryFilterClearBtn.setFont(font)
        self.categoryFilterClearBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.categoryFilterClearBtn.setObjectName("categoryFilterClearBtn")
        self.horizontalLayout_2.addWidget(self.categoryFilterClearBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.categoriesTagsLabel = QtWidgets.QLabel(self.categoriesTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoriesTagsLabel.setFont(font)
        self.categoriesTagsLabel.setObjectName("categoriesTagsLabel")
        self.verticalLayout_3.addWidget(self.categoriesTagsLabel)
        self.categoriesTable = QtWidgets.QTableWidget(self.categoriesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoriesTable.sizePolicy().hasHeightForWidth())
        self.categoriesTable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoriesTable.setFont(font)
        self.categoriesTable.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"}")
        self.categoriesTable.setObjectName("categoriesTable")
        self.categoriesTable.setColumnCount(2)
        self.categoriesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.categoriesTable)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.categoryNameLabel = QtWidgets.QLabel(self.categoriesTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoryNameLabel.setFont(font)
        self.categoryNameLabel.setObjectName("categoryNameLabel")
        self.gridLayout_2.addWidget(self.categoryNameLabel, 1, 0, 1, 1)
        self.addCategoryBtn = QtWidgets.QPushButton(self.categoriesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addCategoryBtn.sizePolicy().hasHeightForWidth())
        self.addCategoryBtn.setSizePolicy(sizePolicy)
        self.addCategoryBtn.setMinimumSize(QtCore.QSize(80, 0))
        self.addCategoryBtn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addCategoryBtn.setFont(font)
        self.addCategoryBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.addCategoryBtn.setObjectName("addCategoryBtn")
        self.gridLayout_2.addWidget(self.addCategoryBtn, 1, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.delCategoryBtn = QtWidgets.QPushButton(self.categoriesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delCategoryBtn.sizePolicy().hasHeightForWidth())
        self.delCategoryBtn.setSizePolicy(sizePolicy)
        self.delCategoryBtn.setMinimumSize(QtCore.QSize(80, 0))
        self.delCategoryBtn.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delCategoryBtn.setFont(font)
        self.delCategoryBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.delCategoryBtn.setObjectName("delCategoryBtn")
        self.verticalLayout_4.addWidget(self.delCategoryBtn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 2, 1, 1)
        self.categoryDescriptionPTE = QtWidgets.QPlainTextEdit(self.categoriesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryDescriptionPTE.sizePolicy().hasHeightForWidth())
        self.categoryDescriptionPTE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoryDescriptionPTE.setFont(font)
        self.categoryDescriptionPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.categoryDescriptionPTE.setObjectName("categoryDescriptionPTE")
        self.gridLayout_2.addWidget(self.categoryDescriptionPTE, 2, 1, 1, 1)
        self.categoryNamePTE = QtWidgets.QPlainTextEdit(self.categoriesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryNamePTE.sizePolicy().hasHeightForWidth())
        self.categoryNamePTE.setSizePolicy(sizePolicy)
        self.categoryNamePTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoryNamePTE.setFont(font)
        self.categoryNamePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.categoryNamePTE.setObjectName("categoryNamePTE")
        self.gridLayout_2.addWidget(self.categoryNamePTE, 1, 1, 1, 1)
        self.categoryDescriptionLabel = QtWidgets.QLabel(self.categoriesTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoryDescriptionLabel.setFont(font)
        self.categoryDescriptionLabel.setObjectName("categoryDescriptionLabel")
        self.gridLayout_2.addWidget(self.categoryDescriptionLabel, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Inkscape files/Inventory/TaskListsvg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.categoriesTab, icon1, "")
        self.supplierTab = QtWidgets.QWidget()
        self.supplierTab.setObjectName("supplierTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.supplierTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.companyFilterCB = QtWidgets.QComboBox(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companyFilterCB.sizePolicy().hasHeightForWidth())
        self.companyFilterCB.setSizePolicy(sizePolicy)
        self.companyFilterCB.setMinimumSize(QtCore.QSize(100, 0))
        self.companyFilterCB.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.companyFilterCB.setFont(font)
        self.companyFilterCB.setStyleSheet("background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"border-radius: 5px;\n"
"text-align: center;")
        self.companyFilterCB.setObjectName("companyFilterCB")
        self.companyFilterCB.addItem("")
        self.companyFilterCB.addItem("")
        self.companyFilterCB.addItem("")
        self.companyFilterCB.addItem("")
        self.companyFilterCB.addItem("")
        self.horizontalLayout_3.addWidget(self.companyFilterCB)
        self.companyFilterPTE = QtWidgets.QPlainTextEdit(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companyFilterPTE.sizePolicy().hasHeightForWidth())
        self.companyFilterPTE.setSizePolicy(sizePolicy)
        self.companyFilterPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.companyFilterPTE.setFont(font)
        self.companyFilterPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.companyFilterPTE.setObjectName("companyFilterPTE")
        self.horizontalLayout_3.addWidget(self.companyFilterPTE)
        self.companyFilterBtn = QtWidgets.QPushButton(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companyFilterBtn.sizePolicy().hasHeightForWidth())
        self.companyFilterBtn.setSizePolicy(sizePolicy)
        self.companyFilterBtn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.companyFilterBtn.setFont(font)
        self.companyFilterBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.companyFilterBtn.setObjectName("companyFilterBtn")
        self.horizontalLayout_3.addWidget(self.companyFilterBtn)
        self.companyFilterClearBtn = QtWidgets.QPushButton(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companyFilterClearBtn.sizePolicy().hasHeightForWidth())
        self.companyFilterClearBtn.setSizePolicy(sizePolicy)
        self.companyFilterClearBtn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.companyFilterClearBtn.setFont(font)
        self.companyFilterClearBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.companyFilterClearBtn.setObjectName("companyFilterClearBtn")
        self.horizontalLayout_3.addWidget(self.companyFilterClearBtn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.companiesTagsLabel = QtWidgets.QLabel(self.supplierTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.companiesTagsLabel.setFont(font)
        self.companiesTagsLabel.setObjectName("companiesTagsLabel")
        self.verticalLayout_5.addWidget(self.companiesTagsLabel)
        self.companiesTable = QtWidgets.QTableWidget(self.supplierTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.companiesTable.setFont(font)
        self.companiesTable.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"}")
        self.companiesTable.setObjectName("companiesTable")
        self.companiesTable.setColumnCount(5)
        self.companiesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.companiesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.companiesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.companiesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.companiesTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.companiesTable.setHorizontalHeaderItem(4, item)
        self.verticalLayout_5.addWidget(self.companiesTable)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.companyNameLabel = QtWidgets.QLabel(self.supplierTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.companyNameLabel.setFont(font)
        self.companyNameLabel.setObjectName("companyNameLabel")
        self.gridLayout_3.addWidget(self.companyNameLabel, 0, 0, 1, 1)
        self.companyNamePTE = QtWidgets.QPlainTextEdit(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companyNamePTE.sizePolicy().hasHeightForWidth())
        self.companyNamePTE.setSizePolicy(sizePolicy)
        self.companyNamePTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.companyNamePTE.setFont(font)
        self.companyNamePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.companyNamePTE.setObjectName("companyNamePTE")
        self.gridLayout_3.addWidget(self.companyNamePTE, 0, 1, 1, 1)
        self.addCompanyBtn = QtWidgets.QPushButton(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addCompanyBtn.sizePolicy().hasHeightForWidth())
        self.addCompanyBtn.setSizePolicy(sizePolicy)
        self.addCompanyBtn.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addCompanyBtn.setFont(font)
        self.addCompanyBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.addCompanyBtn.setObjectName("addCompanyBtn")
        self.gridLayout_3.addWidget(self.addCompanyBtn, 0, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 3, 1, 1)
        self.delCompanyBtn = QtWidgets.QPushButton(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delCompanyBtn.sizePolicy().hasHeightForWidth())
        self.delCompanyBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delCompanyBtn.setFont(font)
        self.delCompanyBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.delCompanyBtn.setObjectName("delCompanyBtn")
        self.gridLayout_3.addWidget(self.delCompanyBtn, 1, 2, 1, 1)
        self.cityPTE = QtWidgets.QPlainTextEdit(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cityPTE.sizePolicy().hasHeightForWidth())
        self.cityPTE.setSizePolicy(sizePolicy)
        self.cityPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cityPTE.setFont(font)
        self.cityPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.cityPTE.setObjectName("cityPTE")
        self.gridLayout_3.addWidget(self.cityPTE, 1, 1, 1, 1)
        self.chgCompanyBtn = QtWidgets.QPushButton(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chgCompanyBtn.sizePolicy().hasHeightForWidth())
        self.chgCompanyBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chgCompanyBtn.setFont(font)
        self.chgCompanyBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.chgCompanyBtn.setObjectName("chgCompanyBtn")
        self.gridLayout_3.addWidget(self.chgCompanyBtn, 2, 2, 1, 1)
        self.cityLabel = QtWidgets.QLabel(self.supplierTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cityLabel.setFont(font)
        self.cityLabel.setObjectName("cityLabel")
        self.gridLayout_3.addWidget(self.cityLabel, 1, 0, 1, 1)
        self.countryLabel = QtWidgets.QLabel(self.supplierTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.countryLabel.setFont(font)
        self.countryLabel.setObjectName("countryLabel")
        self.gridLayout_3.addWidget(self.countryLabel, 2, 0, 1, 1)
        self.countryPTE = QtWidgets.QPlainTextEdit(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countryPTE.sizePolicy().hasHeightForWidth())
        self.countryPTE.setSizePolicy(sizePolicy)
        self.countryPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.countryPTE.setFont(font)
        self.countryPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.countryPTE.setObjectName("countryPTE")
        self.gridLayout_3.addWidget(self.countryPTE, 2, 1, 1, 1)
        self.phoneLabel = QtWidgets.QLabel(self.supplierTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phoneLabel.setFont(font)
        self.phoneLabel.setObjectName("phoneLabel")
        self.gridLayout_3.addWidget(self.phoneLabel, 3, 0, 1, 1)
        self.homepageLabel = QtWidgets.QLabel(self.supplierTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.homepageLabel.setFont(font)
        self.homepageLabel.setObjectName("homepageLabel")
        self.gridLayout_3.addWidget(self.homepageLabel, 4, 0, 1, 1)
        self.phonePTE = QtWidgets.QPlainTextEdit(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phonePTE.sizePolicy().hasHeightForWidth())
        self.phonePTE.setSizePolicy(sizePolicy)
        self.phonePTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phonePTE.setFont(font)
        self.phonePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.phonePTE.setObjectName("phonePTE")
        self.gridLayout_3.addWidget(self.phonePTE, 3, 1, 1, 1)
        self.homepagePTE = QtWidgets.QPlainTextEdit(self.supplierTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homepagePTE.sizePolicy().hasHeightForWidth())
        self.homepagePTE.setSizePolicy(sizePolicy)
        self.homepagePTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.homepagePTE.setFont(font)
        self.homepagePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.homepagePTE.setObjectName("homepagePTE")
        self.gridLayout_3.addWidget(self.homepagePTE, 4, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Inkscape files/Inventory/Supplier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.supplierTab, icon2, "")
        self.receiptsTab = QtWidgets.QWidget()
        self.receiptsTab.setObjectName("receiptsTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.receiptsTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.receiptFilterPTE = QtWidgets.QPlainTextEdit(self.receiptsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiptFilterPTE.sizePolicy().hasHeightForWidth())
        self.receiptFilterPTE.setSizePolicy(sizePolicy)
        self.receiptFilterPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptFilterPTE.setFont(font)
        self.receiptFilterPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.receiptFilterPTE.setObjectName("receiptFilterPTE")
        self.horizontalLayout_4.addWidget(self.receiptFilterPTE)
        self.receiptFilterBtn = QtWidgets.QPushButton(self.receiptsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiptFilterBtn.sizePolicy().hasHeightForWidth())
        self.receiptFilterBtn.setSizePolicy(sizePolicy)
        self.receiptFilterBtn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptFilterBtn.setFont(font)
        self.receiptFilterBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.receiptFilterBtn.setObjectName("receiptFilterBtn")
        self.horizontalLayout_4.addWidget(self.receiptFilterBtn)
        self.receiptFilterClearBtn = QtWidgets.QPushButton(self.receiptsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiptFilterClearBtn.sizePolicy().hasHeightForWidth())
        self.receiptFilterClearBtn.setSizePolicy(sizePolicy)
        self.receiptFilterClearBtn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptFilterClearBtn.setFont(font)
        self.receiptFilterClearBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.receiptFilterClearBtn.setObjectName("receiptFilterClearBtn")
        self.horizontalLayout_4.addWidget(self.receiptFilterClearBtn)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.receiptsTagsLabel = QtWidgets.QLabel(self.receiptsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptsTagsLabel.setFont(font)
        self.receiptsTagsLabel.setObjectName("receiptsTagsLabel")
        self.verticalLayout_6.addWidget(self.receiptsTagsLabel)
        self.receiptsTable = QtWidgets.QTableWidget(self.receiptsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptsTable.setFont(font)
        self.receiptsTable.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"}")
        self.receiptsTable.setObjectName("receiptsTable")
        self.receiptsTable.setColumnCount(5)
        self.receiptsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.receiptsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.receiptsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.receiptsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.receiptsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.receiptsTable.setHorizontalHeaderItem(4, item)
        self.verticalLayout_6.addWidget(self.receiptsTable)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.receiptConfirmBtn = QtWidgets.QPushButton(self.receiptsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiptConfirmBtn.sizePolicy().hasHeightForWidth())
        self.receiptConfirmBtn.setSizePolicy(sizePolicy)
        self.receiptConfirmBtn.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptConfirmBtn.setFont(font)
        self.receiptConfirmBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.receiptConfirmBtn.setObjectName("receiptConfirmBtn")
        self.gridLayout_4.addWidget(self.receiptConfirmBtn, 0, 2, 1, 1)
        self.receiptOrderNumberLabel = QtWidgets.QLabel(self.receiptsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptOrderNumberLabel.setFont(font)
        self.receiptOrderNumberLabel.setObjectName("receiptOrderNumberLabel")
        self.gridLayout_4.addWidget(self.receiptOrderNumberLabel, 0, 0, 1, 1)
        self.receiptOrderNumberPTE = QtWidgets.QPlainTextEdit(self.receiptsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiptOrderNumberPTE.sizePolicy().hasHeightForWidth())
        self.receiptOrderNumberPTE.setSizePolicy(sizePolicy)
        self.receiptOrderNumberPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptOrderNumberPTE.setFont(font)
        self.receiptOrderNumberPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.receiptOrderNumberPTE.setObjectName("receiptOrderNumberPTE")
        self.gridLayout_4.addWidget(self.receiptOrderNumberPTE, 0, 1, 1, 1)
        self.receiptProductNameLabel = QtWidgets.QLabel(self.receiptsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptProductNameLabel.setFont(font)
        self.receiptProductNameLabel.setObjectName("receiptProductNameLabel")
        self.gridLayout_4.addWidget(self.receiptProductNameLabel, 2, 0, 1, 1)
        self.receiptProductNamePTE = QtWidgets.QPlainTextEdit(self.receiptsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiptProductNamePTE.sizePolicy().hasHeightForWidth())
        self.receiptProductNamePTE.setSizePolicy(sizePolicy)
        self.receiptProductNamePTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptProductNamePTE.setFont(font)
        self.receiptProductNamePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.receiptProductNamePTE.setObjectName("receiptProductNamePTE")
        self.gridLayout_4.addWidget(self.receiptProductNamePTE, 2, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 0, 3, 1, 1)
        self.receiptAmountPTE = QtWidgets.QPlainTextEdit(self.receiptsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiptAmountPTE.sizePolicy().hasHeightForWidth())
        self.receiptAmountPTE.setSizePolicy(sizePolicy)
        self.receiptAmountPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptAmountPTE.setFont(font)
        self.receiptAmountPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.receiptAmountPTE.setObjectName("receiptAmountPTE")
        self.gridLayout_4.addWidget(self.receiptAmountPTE, 3, 1, 1, 1)
        self.receiptOrderDateLabel = QtWidgets.QLabel(self.receiptsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptOrderDateLabel.setFont(font)
        self.receiptOrderDateLabel.setObjectName("receiptOrderDateLabel")
        self.gridLayout_4.addWidget(self.receiptOrderDateLabel, 1, 0, 1, 1)
        self.receiptCancelBtn = QtWidgets.QPushButton(self.receiptsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiptCancelBtn.sizePolicy().hasHeightForWidth())
        self.receiptCancelBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptCancelBtn.setFont(font)
        self.receiptCancelBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.receiptCancelBtn.setObjectName("receiptCancelBtn")
        self.gridLayout_4.addWidget(self.receiptCancelBtn, 1, 2, 1, 1)
        self.receiptOrderDatePTE = QtWidgets.QPlainTextEdit(self.receiptsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiptOrderDatePTE.sizePolicy().hasHeightForWidth())
        self.receiptOrderDatePTE.setSizePolicy(sizePolicy)
        self.receiptOrderDatePTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptOrderDatePTE.setFont(font)
        self.receiptOrderDatePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.receiptOrderDatePTE.setObjectName("receiptOrderDatePTE")
        self.gridLayout_4.addWidget(self.receiptOrderDatePTE, 1, 1, 1, 1)
        self.receiptAmountLabel = QtWidgets.QLabel(self.receiptsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptAmountLabel.setFont(font)
        self.receiptAmountLabel.setObjectName("receiptAmountLabel")
        self.gridLayout_4.addWidget(self.receiptAmountLabel, 3, 0, 1, 1)
        self.receiptSupplierLabel = QtWidgets.QLabel(self.receiptsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptSupplierLabel.setFont(font)
        self.receiptSupplierLabel.setObjectName("receiptSupplierLabel")
        self.gridLayout_4.addWidget(self.receiptSupplierLabel, 4, 0, 1, 1)
        self.receiptSupplierPTE = QtWidgets.QPlainTextEdit(self.receiptsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiptSupplierPTE.sizePolicy().hasHeightForWidth())
        self.receiptSupplierPTE.setSizePolicy(sizePolicy)
        self.receiptSupplierPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receiptSupplierPTE.setFont(font)
        self.receiptSupplierPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.receiptSupplierPTE.setObjectName("receiptSupplierPTE")
        self.gridLayout_4.addWidget(self.receiptSupplierPTE, 4, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Inkscape files/Inventory/Receipt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.receiptsTab, icon3, "")
        self.writeoffsTab = QtWidgets.QWidget()
        self.writeoffsTab.setObjectName("writeoffsTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.writeoffsTab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.writeoffFilterPTE = QtWidgets.QPlainTextEdit(self.writeoffsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeoffFilterPTE.sizePolicy().hasHeightForWidth())
        self.writeoffFilterPTE.setSizePolicy(sizePolicy)
        self.writeoffFilterPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffFilterPTE.setFont(font)
        self.writeoffFilterPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.writeoffFilterPTE.setObjectName("writeoffFilterPTE")
        self.horizontalLayout_5.addWidget(self.writeoffFilterPTE)
        self.writeoffFilterBtn = QtWidgets.QPushButton(self.writeoffsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeoffFilterBtn.sizePolicy().hasHeightForWidth())
        self.writeoffFilterBtn.setSizePolicy(sizePolicy)
        self.writeoffFilterBtn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffFilterBtn.setFont(font)
        self.writeoffFilterBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.writeoffFilterBtn.setObjectName("writeoffFilterBtn")
        self.horizontalLayout_5.addWidget(self.writeoffFilterBtn)
        self.writeoffFilterClearBtn = QtWidgets.QPushButton(self.writeoffsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeoffFilterClearBtn.sizePolicy().hasHeightForWidth())
        self.writeoffFilterClearBtn.setSizePolicy(sizePolicy)
        self.writeoffFilterClearBtn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffFilterClearBtn.setFont(font)
        self.writeoffFilterClearBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.writeoffFilterClearBtn.setObjectName("writeoffFilterClearBtn")
        self.horizontalLayout_5.addWidget(self.writeoffFilterClearBtn)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.writeoffsTagsLabel = QtWidgets.QLabel(self.writeoffsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffsTagsLabel.setFont(font)
        self.writeoffsTagsLabel.setObjectName("writeoffsTagsLabel")
        self.verticalLayout_7.addWidget(self.writeoffsTagsLabel)
        self.writeoffsTable = QtWidgets.QTableWidget(self.writeoffsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffsTable.setFont(font)
        self.writeoffsTable.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"}")
        self.writeoffsTable.setObjectName("writeoffsTable")
        self.writeoffsTable.setColumnCount(5)
        self.writeoffsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.writeoffsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.writeoffsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.writeoffsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.writeoffsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.writeoffsTable.setHorizontalHeaderItem(4, item)
        self.verticalLayout_7.addWidget(self.writeoffsTable)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem11, 0, 3, 1, 1)
        self.writeoffOrderNumberPTE = QtWidgets.QPlainTextEdit(self.writeoffsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeoffOrderNumberPTE.sizePolicy().hasHeightForWidth())
        self.writeoffOrderNumberPTE.setSizePolicy(sizePolicy)
        self.writeoffOrderNumberPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffOrderNumberPTE.setFont(font)
        self.writeoffOrderNumberPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.writeoffOrderNumberPTE.setObjectName("writeoffOrderNumberPTE")
        self.gridLayout_5.addWidget(self.writeoffOrderNumberPTE, 0, 1, 1, 1)
        self.writeoffOrderNumberLabel = QtWidgets.QLabel(self.writeoffsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffOrderNumberLabel.setFont(font)
        self.writeoffOrderNumberLabel.setObjectName("writeoffOrderNumberLabel")
        self.gridLayout_5.addWidget(self.writeoffOrderNumberLabel, 0, 0, 1, 1)
        self.writeoffProductNamePTE = QtWidgets.QPlainTextEdit(self.writeoffsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeoffProductNamePTE.sizePolicy().hasHeightForWidth())
        self.writeoffProductNamePTE.setSizePolicy(sizePolicy)
        self.writeoffProductNamePTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffProductNamePTE.setFont(font)
        self.writeoffProductNamePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.writeoffProductNamePTE.setObjectName("writeoffProductNamePTE")
        self.gridLayout_5.addWidget(self.writeoffProductNamePTE, 2, 1, 1, 1)
        self.writeoffConfirm = QtWidgets.QPushButton(self.writeoffsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeoffConfirm.sizePolicy().hasHeightForWidth())
        self.writeoffConfirm.setSizePolicy(sizePolicy)
        self.writeoffConfirm.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffConfirm.setFont(font)
        self.writeoffConfirm.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.writeoffConfirm.setObjectName("writeoffConfirm")
        self.gridLayout_5.addWidget(self.writeoffConfirm, 0, 2, 1, 1)
        self.writeoffProductNameLabel = QtWidgets.QLabel(self.writeoffsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffProductNameLabel.setFont(font)
        self.writeoffProductNameLabel.setObjectName("writeoffProductNameLabel")
        self.gridLayout_5.addWidget(self.writeoffProductNameLabel, 2, 0, 1, 1)
        self.writeoffCancel = QtWidgets.QPushButton(self.writeoffsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeoffCancel.sizePolicy().hasHeightForWidth())
        self.writeoffCancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffCancel.setFont(font)
        self.writeoffCancel.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.writeoffCancel.setObjectName("writeoffCancel")
        self.gridLayout_5.addWidget(self.writeoffCancel, 1, 2, 1, 1)
        self.writeoffAmountLabel = QtWidgets.QLabel(self.writeoffsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffAmountLabel.setFont(font)
        self.writeoffAmountLabel.setObjectName("writeoffAmountLabel")
        self.gridLayout_5.addWidget(self.writeoffAmountLabel, 3, 0, 1, 1)
        self.writeoffAmountPTE = QtWidgets.QPlainTextEdit(self.writeoffsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeoffAmountPTE.sizePolicy().hasHeightForWidth())
        self.writeoffAmountPTE.setSizePolicy(sizePolicy)
        self.writeoffAmountPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffAmountPTE.setFont(font)
        self.writeoffAmountPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.writeoffAmountPTE.setObjectName("writeoffAmountPTE")
        self.gridLayout_5.addWidget(self.writeoffAmountPTE, 3, 1, 1, 1)
        self.writeoffOrderDatePTE = QtWidgets.QPlainTextEdit(self.writeoffsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeoffOrderDatePTE.sizePolicy().hasHeightForWidth())
        self.writeoffOrderDatePTE.setSizePolicy(sizePolicy)
        self.writeoffOrderDatePTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffOrderDatePTE.setFont(font)
        self.writeoffOrderDatePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.writeoffOrderDatePTE.setObjectName("writeoffOrderDatePTE")
        self.gridLayout_5.addWidget(self.writeoffOrderDatePTE, 1, 1, 1, 1)
        self.writeoffOrderDateLabel = QtWidgets.QLabel(self.writeoffsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffOrderDateLabel.setFont(font)
        self.writeoffOrderDateLabel.setObjectName("writeoffOrderDateLabel")
        self.gridLayout_5.addWidget(self.writeoffOrderDateLabel, 1, 0, 1, 1)
        self.writeoffReasonLabel = QtWidgets.QLabel(self.writeoffsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffReasonLabel.setFont(font)
        self.writeoffReasonLabel.setObjectName("writeoffReasonLabel")
        self.gridLayout_5.addWidget(self.writeoffReasonLabel, 4, 0, 1, 1)
        self.writeoffReasonPTE = QtWidgets.QPlainTextEdit(self.writeoffsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeoffReasonPTE.sizePolicy().hasHeightForWidth())
        self.writeoffReasonPTE.setSizePolicy(sizePolicy)
        self.writeoffReasonPTE.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.writeoffReasonPTE.setFont(font)
        self.writeoffReasonPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.writeoffReasonPTE.setObjectName("writeoffReasonPTE")
        self.gridLayout_5.addWidget(self.writeoffReasonPTE, 4, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_5)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../Inkscape files/Inventory/Write-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.writeoffsTab, icon4, "")
        self.reportsTab = QtWidgets.QWidget()
        self.reportsTab.setObjectName("reportsTab")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.reportsTab)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.reportsTab2 = QtWidgets.QTabWidget(self.reportsTab)
        self.reportsTab2.setStyleSheet("color: white;")
        self.reportsTab2.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.reportsTab2.setIconSize(QtCore.QSize(20, 20))
        self.reportsTab2.setObjectName("reportsTab2")
        self.inventoryMovementTab = QtWidgets.QWidget()
        self.inventoryMovementTab.setObjectName("inventoryMovementTab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.inventoryMovementTab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.inventoryMovementTable = QtWidgets.QTableWidget(self.inventoryMovementTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inventoryMovementTable.setFont(font)
        self.inventoryMovementTable.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"}")
        self.inventoryMovementTable.setObjectName("inventoryMovementTable")
        self.inventoryMovementTable.setColumnCount(7)
        self.inventoryMovementTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryMovementTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryMovementTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryMovementTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryMovementTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryMovementTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryMovementTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryMovementTable.setHorizontalHeaderItem(6, item)
        self.verticalLayout_8.addWidget(self.inventoryMovementTable)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.IMTimePeriodLabel = QtWidgets.QLabel(self.inventoryMovementTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IMTimePeriodLabel.setFont(font)
        self.IMTimePeriodLabel.setObjectName("IMTimePeriodLabel")
        self.gridLayout_6.addWidget(self.IMTimePeriodLabel, 1, 0, 1, 1)
        self.IMTimePeriodPTE = QtWidgets.QPlainTextEdit(self.inventoryMovementTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IMTimePeriodPTE.sizePolicy().hasHeightForWidth())
        self.IMTimePeriodPTE.setSizePolicy(sizePolicy)
        self.IMTimePeriodPTE.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IMTimePeriodPTE.setFont(font)
        self.IMTimePeriodPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.IMTimePeriodPTE.setObjectName("IMTimePeriodPTE")
        self.gridLayout_6.addWidget(self.IMTimePeriodPTE, 1, 1, 1, 1)
        self.IMTimeUnitCB = QtWidgets.QComboBox(self.inventoryMovementTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IMTimeUnitCB.sizePolicy().hasHeightForWidth())
        self.IMTimeUnitCB.setSizePolicy(sizePolicy)
        self.IMTimeUnitCB.setMinimumSize(QtCore.QSize(100, 0))
        self.IMTimeUnitCB.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IMTimeUnitCB.setFont(font)
        self.IMTimeUnitCB.setStyleSheet("background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"border-radius: 5px;\n"
"text-align: center;")
        self.IMTimeUnitCB.setObjectName("IMTimeUnitCB")
        self.IMTimeUnitCB.addItem("")
        self.IMTimeUnitCB.addItem("")
        self.IMTimeUnitCB.addItem("")
        self.gridLayout_6.addWidget(self.IMTimeUnitCB, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem12, 0, 3, 1, 1)
        self.IMTimeUnitLabel = QtWidgets.QLabel(self.inventoryMovementTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IMTimeUnitLabel.setFont(font)
        self.IMTimeUnitLabel.setObjectName("IMTimeUnitLabel")
        self.gridLayout_6.addWidget(self.IMTimeUnitLabel, 0, 0, 1, 1)
        self.IMManagerLabel = QtWidgets.QLabel(self.inventoryMovementTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IMManagerLabel.setFont(font)
        self.IMManagerLabel.setObjectName("IMManagerLabel")
        self.gridLayout_6.addWidget(self.IMManagerLabel, 2, 0, 1, 1)
        self.IMViewBtn = QtWidgets.QPushButton(self.inventoryMovementTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IMViewBtn.sizePolicy().hasHeightForWidth())
        self.IMViewBtn.setSizePolicy(sizePolicy)
        self.IMViewBtn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IMViewBtn.setFont(font)
        self.IMViewBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.IMViewBtn.setObjectName("IMViewBtn")
        self.gridLayout_6.addWidget(self.IMViewBtn, 0, 2, 1, 1)
        self.IMSendBtn = QtWidgets.QPushButton(self.inventoryMovementTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IMSendBtn.sizePolicy().hasHeightForWidth())
        self.IMSendBtn.setSizePolicy(sizePolicy)
        self.IMSendBtn.setMinimumSize(QtCore.QSize(80, 30))
        self.IMSendBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IMSendBtn.setFont(font)
        self.IMSendBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.IMSendBtn.setObjectName("IMSendBtn")
        self.gridLayout_6.addWidget(self.IMSendBtn, 1, 2, 1, 1)
        self.IMManagerCB = QtWidgets.QComboBox(self.inventoryMovementTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IMManagerCB.setFont(font)
        self.IMManagerCB.setStyleSheet("background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"border-radius: 5px;\n"
"text-align: center;")
        self.IMManagerCB.setObjectName("IMManagerCB")
        self.gridLayout_6.addWidget(self.IMManagerCB, 2, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_6)
        self.reportsTab2.addTab(self.inventoryMovementTab, "")
        self.SLOBTab = QtWidgets.QWidget()
        self.SLOBTab.setObjectName("SLOBTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.SLOBTab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.SLOBTable = QtWidgets.QTableWidget(self.SLOBTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SLOBTable.setFont(font)
        self.SLOBTable.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"}")
        self.SLOBTable.setObjectName("SLOBTable")
        self.SLOBTable.setColumnCount(4)
        self.SLOBTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.SLOBTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SLOBTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.SLOBTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.SLOBTable.setHorizontalHeaderItem(3, item)
        self.verticalLayout_9.addWidget(self.SLOBTable)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.SLOBProductsLabel = QtWidgets.QLabel(self.SLOBTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SLOBProductsLabel.setFont(font)
        self.SLOBProductsLabel.setObjectName("SLOBProductsLabel")
        self.gridLayout_7.addWidget(self.SLOBProductsLabel, 0, 0, 1, 1)
        self.SLOBProductsPTE = QtWidgets.QPlainTextEdit(self.SLOBTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SLOBProductsPTE.sizePolicy().hasHeightForWidth())
        self.SLOBProductsPTE.setSizePolicy(sizePolicy)
        self.SLOBProductsPTE.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SLOBProductsPTE.setFont(font)
        self.SLOBProductsPTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"}")
        self.SLOBProductsPTE.setObjectName("SLOBProductsPTE")
        self.gridLayout_7.addWidget(self.SLOBProductsPTE, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem13, 0, 3, 1, 1)
        self.SLOBManagerLabel = QtWidgets.QLabel(self.SLOBTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SLOBManagerLabel.setFont(font)
        self.SLOBManagerLabel.setObjectName("SLOBManagerLabel")
        self.gridLayout_7.addWidget(self.SLOBManagerLabel, 1, 0, 1, 1)
        self.SLOBManagerCB = QtWidgets.QComboBox(self.SLOBTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SLOBManagerCB.sizePolicy().hasHeightForWidth())
        self.SLOBManagerCB.setSizePolicy(sizePolicy)
        self.SLOBManagerCB.setMinimumSize(QtCore.QSize(100, 0))
        self.SLOBManagerCB.setMaximumSize(QtCore.QSize(140, 30))
        self.SLOBManagerCB.setStyleSheet("background-color: rgb(27, 223, 148);\n"
"color: rgb(30, 28, 55);\n"
"border-radius: 5px;\n"
"text-align: center;")
        self.SLOBManagerCB.setObjectName("SLOBManagerCB")
        self.gridLayout_7.addWidget(self.SLOBManagerCB, 1, 1, 1, 1)
        self.SLOBSendBtn = QtWidgets.QPushButton(self.SLOBTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SLOBSendBtn.sizePolicy().hasHeightForWidth())
        self.SLOBSendBtn.setSizePolicy(sizePolicy)
        self.SLOBSendBtn.setMinimumSize(QtCore.QSize(80, 30))
        self.SLOBSendBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SLOBSendBtn.setFont(font)
        self.SLOBSendBtn.setStyleSheet("QPushButton {\n"
"color: rgb(30, 28, 55);\n"
"background-color: rgb(27, 223, 148);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 255, 169)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(19, 163, 108)\n"
"}")
        self.SLOBSendBtn.setObjectName("SLOBSendBtn")
        self.gridLayout_7.addWidget(self.SLOBSendBtn, 0, 2, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_7)
        self.reportsTab2.addTab(self.SLOBTab, "")
        self.horizontalLayout_6.addWidget(self.reportsTab2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../Inkscape files/Inventory/Diagramm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.reportsTab, icon5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.reportsTab2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.productsTable.setColumnWidth(0, 300)
        self.productsTable.setColumnWidth(1, 200)
        self.productsTable.setColumnWidth(2, 200)
        self.productsTable.setColumnWidth(3, 200)
        self.productsTable.setColumnWidth(4, 300)
        self.productsTable.setColumnWidth(5, 300)

        self.categoriesTable.setColumnWidth(0, 300)
        self.categoriesTable.setColumnWidth(1, 1000)

        self.companiesTable.setColumnWidth(0, 300)
        self.companiesTable.setColumnWidth(1, 300)
        self.companiesTable.setColumnWidth(2, 300)
        self.companiesTable.setColumnWidth(3, 200)
        self.companiesTable.setColumnWidth(4, 300)

        self.receiptsTable.setColumnWidth(0, 200)
        self.receiptsTable.setColumnWidth(1, 200)
        self.receiptsTable.setColumnWidth(2, 200)
        self.receiptsTable.setColumnWidth(3, 200)
        self.receiptsTable.setColumnWidth(4, 300)

        self.writeoffsTable.setColumnWidth(0, 200)
        self.writeoffsTable.setColumnWidth(1, 200)
        self.writeoffsTable.setColumnWidth(2, 200)
        self.writeoffsTable.setColumnWidth(3, 200)
        self.writeoffsTable.setColumnWidth(4, 1000)

        self.inventoryMovementTable.setColumnWidth(0, 300)
        self.inventoryMovementTable.setColumnWidth(1, 200)
        self.inventoryMovementTable.setColumnWidth(2, 200)
        self.inventoryMovementTable.setColumnWidth(3, 200)
        self.inventoryMovementTable.setColumnWidth(4, 210)
        self.inventoryMovementTable.setColumnWidth(5, 300)
        self.inventoryMovementTable.setColumnWidth(6, 350)

        self.SLOBTable.setColumnWidth(0, 300)
        self.SLOBTable.setColumnWidth(1, 200)
        self.SLOBTable.setColumnWidth(2, 200)
        self.SLOBTable.setColumnWidth(3, 200)

        self.IMManagerCB.setMinimumSize(250, 30)
        self.SLOBManagerCB.setMinimumSize(250, 30)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inventory"))
        self.label.setText(_translate("MainWindow", "Inventory"))
        self.productFilterCB.setItemText(0, _translate("MainWindow", "Product name"))
        self.productFilterCB.setItemText(1, _translate("MainWindow", "Freight"))
        self.productFilterCB.setItemText(2, _translate("MainWindow", "Unit price"))
        self.productFilterCB.setItemText(3, _translate("MainWindow", "Units in stock"))
        self.productFilterCB.setItemText(4, _translate("MainWindow", "Category name"))
        self.productFilterCB.setItemText(5, _translate("MainWindow", "Company name"))
        self.productFilterPTE.setPlaceholderText(_translate("MainWindow", "Enter the request"))
        self.productFilterBtn.setText(_translate("MainWindow", "OK"))
        self.productFilterClearBtn.setText(_translate("MainWindow", "CLEAR"))
        self.productsTagsLabel.setText(_translate("MainWindow", "Tags"))
        item = self.productsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product name"))
        item = self.productsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Freight"))
        item = self.productsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Unit price"))
        item = self.productsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Units in stock"))
        item = self.productsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Category"))
        item = self.productsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Supplier"))
        self.productNamePTE.setPlaceholderText(_translate("MainWindow", "Enter the product name"))
        self.unitsInStockPTE.setPlaceholderText(_translate("MainWindow", "Enter the units in stock"))
        self.productNameLabel.setText(_translate("MainWindow", "Product name"))
        self.addProductBtn.setText(_translate("MainWindow", "ADD"))
        self.delProductBtn.setText(_translate("MainWindow", "DELETE"))
        self.unitPriceLabel.setText(_translate("MainWindow", "Unit price"))
        self.freightLabel.setText(_translate("MainWindow", "Freight"))
        self.freightPTE.setPlaceholderText(_translate("MainWindow", "Enter the freight"))
        self.unitPricePTE.setPlaceholderText(_translate("MainWindow", "Enter the unit price"))
        self.chgProductBtn.setText(_translate("MainWindow", "CHANGE"))
        self.unitsInStockLabel.setText(_translate("MainWindow", "Units_in_stock"))
        self.categoryLabel.setText(_translate("MainWindow", "Category"))
        self.productsCategoryPTE.setPlaceholderText(_translate("MainWindow", "Enter the category"))
        self.supplierLabel.setText(_translate("MainWindow", "Supplier"))
        self.productsSupplierPTE.setPlaceholderText(_translate("MainWindow", "Enter the supplier"))
        self.categoryFilterPTE.setPlaceholderText(_translate("MainWindow", "Enter the category name"))
        self.categoryFilterBtn.setText(_translate("MainWindow", "OK"))
        self.categoryFilterClearBtn.setText(_translate("MainWindow", "CLEAR"))
        self.categoriesTagsLabel.setText(_translate("MainWindow", "Category name:"))
        item = self.categoriesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category name"))
        item = self.categoriesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        self.categoryNameLabel.setText(_translate("MainWindow", "Category name"))
        self.addCategoryBtn.setText(_translate("MainWindow", "ADD"))
        self.delCategoryBtn.setText(_translate("MainWindow", "DELETE"))
        self.categoryDescriptionPTE.setPlaceholderText(_translate("MainWindow", "Enter the description"))
        self.categoryNamePTE.setPlaceholderText(_translate("MainWindow", "Enter the category name"))
        self.categoryDescriptionLabel.setText(_translate("MainWindow", "Description"))
        self.companyFilterCB.setItemText(0, _translate("MainWindow", "Company name"))
        self.companyFilterCB.setItemText(1, _translate("MainWindow", "Company city"))
        self.companyFilterCB.setItemText(2, _translate("MainWindow", "Company country"))
        self.companyFilterCB.setItemText(3, _translate("MainWindow", "Company phone"))
        self.companyFilterCB.setItemText(4, _translate("MainWindow", "Company homepage"))
        self.companyFilterPTE.setPlaceholderText(_translate("MainWindow", "Enter the request"))
        self.companyFilterBtn.setText(_translate("MainWindow", "OK"))
        self.companyFilterClearBtn.setText(_translate("MainWindow", "CLEAR"))
        self.companiesTagsLabel.setText(_translate("MainWindow", "Tags"))
        item = self.companiesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Company name"))
        item = self.companiesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "City"))
        item = self.companiesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Country"))
        item = self.companiesTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.companiesTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Homepage"))
        self.companyNameLabel.setText(_translate("MainWindow", "Company name"))
        self.companyNamePTE.setPlaceholderText(_translate("MainWindow", "Enter the company name"))
        self.addCompanyBtn.setText(_translate("MainWindow", "ADD"))
        self.delCompanyBtn.setText(_translate("MainWindow", "DELETE"))
        self.cityPTE.setPlaceholderText(_translate("MainWindow", "Enter the city"))
        self.chgCompanyBtn.setText(_translate("MainWindow", "CHANGE"))
        self.cityLabel.setText(_translate("MainWindow", "City"))
        self.countryLabel.setText(_translate("MainWindow", "Country"))
        self.countryPTE.setPlaceholderText(_translate("MainWindow", "Enter the country"))
        self.phoneLabel.setText(_translate("MainWindow", "Phone"))
        self.homepageLabel.setText(_translate("MainWindow", "Homepage"))
        self.phonePTE.setPlaceholderText(_translate("MainWindow", "Enter the phone"))
        self.homepagePTE.setPlaceholderText(_translate("MainWindow", "Enter the homepage"))
        self.receiptFilterPTE.setPlaceholderText(_translate("MainWindow", "Enter the order number"))
        self.receiptFilterBtn.setText(_translate("MainWindow", "OK"))
        self.receiptFilterClearBtn.setText(_translate("MainWindow", "CLEAR"))
        self.receiptsTagsLabel.setText(_translate("MainWindow", "Order number:"))
        item = self.receiptsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order number"))
        item = self.receiptsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Order date"))
        item = self.receiptsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Product name"))
        item = self.receiptsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.receiptsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Supplier"))
        self.receiptConfirmBtn.setText(_translate("MainWindow", "CONFIRM"))
        self.receiptOrderNumberLabel.setText(_translate("MainWindow", "Order number"))
        self.receiptOrderNumberPTE.setPlaceholderText(_translate("MainWindow", "Enter the order number"))
        self.receiptProductNameLabel.setText(_translate("MainWindow", "Product name"))
        self.receiptProductNamePTE.setPlaceholderText(_translate("MainWindow", "Enter the product name"))
        self.receiptAmountPTE.setPlaceholderText(_translate("MainWindow", "Enter the amount"))
        self.receiptOrderDateLabel.setText(_translate("MainWindow", "Order date"))
        self.receiptCancelBtn.setText(_translate("MainWindow", "CANCEL"))
        self.receiptOrderDatePTE.setPlaceholderText(_translate("MainWindow", "Enter the order date"))
        self.receiptAmountLabel.setText(_translate("MainWindow", "Amount"))
        self.receiptSupplierLabel.setText(_translate("MainWindow", "Supplier"))
        self.receiptSupplierPTE.setPlaceholderText(_translate("MainWindow", "Enter the supplier"))
        self.writeoffFilterPTE.setPlaceholderText(_translate("MainWindow", "Enter the order number"))
        self.writeoffFilterBtn.setText(_translate("MainWindow", "OK"))
        self.writeoffFilterClearBtn.setText(_translate("MainWindow", "CLEAR"))
        self.writeoffsTagsLabel.setText(_translate("MainWindow", "Order number:"))
        item = self.writeoffsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order number"))
        item = self.writeoffsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Order date"))
        item = self.writeoffsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Product name"))
        item = self.writeoffsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.writeoffsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Reason"))
        self.writeoffOrderNumberPTE.setPlaceholderText(_translate("MainWindow", "Enter the order number"))
        self.writeoffOrderNumberLabel.setText(_translate("MainWindow", "Order number"))
        self.writeoffProductNamePTE.setPlaceholderText(_translate("MainWindow", "Enter the product name"))
        self.writeoffConfirm.setText(_translate("MainWindow", "CONFIRM"))
        self.writeoffProductNameLabel.setText(_translate("MainWindow", "Product name"))
        self.writeoffCancel.setText(_translate("MainWindow", "CANCEL"))
        self.writeoffAmountLabel.setText(_translate("MainWindow", "Amount"))
        self.writeoffAmountPTE.setPlaceholderText(_translate("MainWindow", "Enter the amount"))
        self.writeoffOrderDatePTE.setPlaceholderText(_translate("MainWindow", "Enter the order date"))
        self.writeoffOrderDateLabel.setText(_translate("MainWindow", "Order date"))
        self.writeoffReasonLabel.setText(_translate("MainWindow", "Reason"))
        self.writeoffReasonPTE.setPlaceholderText(_translate("MainWindow", "Enter the reason"))
        item = self.inventoryMovementTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product name"))
        item = self.inventoryMovementTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last receipt date"))
        item = self.inventoryMovementTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last write-off date"))
        item = self.inventoryMovementTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total receipt amount"))
        item = self.inventoryMovementTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total write-off amount"))
        item = self.inventoryMovementTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Receipt supplier"))
        item = self.inventoryMovementTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Write-off\'s most frequent reason"))
        self.IMTimePeriodLabel.setText(_translate("MainWindow", "Time period"))
        self.IMTimePeriodPTE.setPlaceholderText(_translate("MainWindow", "Enter"))
        self.IMTimeUnitCB.setItemText(0, _translate("MainWindow", "Days"))
        self.IMTimeUnitCB.setItemText(1, _translate("MainWindow", "Months"))
        self.IMTimeUnitCB.setItemText(2, _translate("MainWindow", "Years"))
        self.IMTimeUnitLabel.setText(_translate("MainWindow", "Tme unit"))
        self.IMManagerLabel.setText(_translate("MainWindow", "Manager"))
        self.IMViewBtn.setText(_translate("MainWindow", "VIEW"))
        self.IMSendBtn.setText(_translate("MainWindow", "SEND"))
        self.reportsTab2.setTabText(self.reportsTab2.indexOf(self.inventoryMovementTab), _translate("MainWindow", "Inventory Movement"))
        item = self.SLOBTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product name"))
        item = self.SLOBTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last movement date"))
        item = self.SLOBTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total amount"))
        item = self.SLOBTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total cost"))
        self.SLOBProductsLabel.setText(_translate("MainWindow", "Slow moving and obsolete products"))
        self.SLOBProductsPTE.setPlaceholderText(_translate("MainWindow", "Enter the products"))
        self.SLOBManagerLabel.setText(_translate("MainWindow", "Manager"))
        self.SLOBSendBtn.setText(_translate("MainWindow", "SEND"))
        self.reportsTab2.setTabText(self.reportsTab2.indexOf(self.SLOBTab), _translate("MainWindow", "SLOB"))
