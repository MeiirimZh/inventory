from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Authorization(object):
    def setupUi(self, Authorization):
        Authorization.setObjectName("Authorization")
        Authorization.setEnabled(True)
        Authorization.resize(500, 300)
        Authorization.setMinimumSize(QtCore.QSize(500, 300))
        Authorization.setMaximumSize(QtCore.QSize(500, 300))
        self.centralwidget = QtWidgets.QWidget(Authorization)
        self.centralwidget.setStyleSheet("background-color: rgb(20, 18, 41);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signInLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signInLabel.sizePolicy().hasHeightForWidth())
        self.signInLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.signInLabel.setFont(font)
        self.signInLabel.setStyleSheet("color:rgb(27, 223, 148);")
        self.signInLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.signInLabel.setObjectName("signInLabel")
        self.verticalLayout.addWidget(self.signInLabel)
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("color: rgb(228, 227, 231);")
        self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.verticalLayout.addWidget(self.usernameLabel)
        self.usernamePTE = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernamePTE.sizePolicy().hasHeightForWidth())
        self.usernamePTE.setSizePolicy(sizePolicy)
        self.usernamePTE.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.usernamePTE.setFont(font)
        self.usernamePTE.setAutoFillBackground(False)
        self.usernamePTE.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    color: rgb(228, 227, 231);\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"    color: rgb(228, 227, 231);\n"
"}")
        self.usernamePTE.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.usernamePTE.setObjectName("usernamePTE")
        self.verticalLayout.addWidget(self.usernamePTE)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet("color: rgb(228, 227, 231);")
        self.passwordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout.addWidget(self.passwordLabel)
        self.passwordLE = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLE.sizePolicy().hasHeightForWidth())
        self.passwordLE.setSizePolicy(sizePolicy)
        self.passwordLE.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordLE.setFont(font)
        self.passwordLE.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    color: rgb(228, 227, 231);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(27, 223, 148);\n"
"    border-radius: 10px;\n"
"    color: rgb(228, 227, 231);\n"
"}")
        self.passwordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLE.setObjectName("passwordLE")
        self.verticalLayout.addWidget(self.passwordLE)
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy)
        self.loginBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.loginBtn.setMaximumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet("QPushButton {\n"
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
        self.loginBtn.setCheckable(False)
        self.loginBtn.setAutoDefault(False)
        self.loginBtn.setDefault(False)
        self.loginBtn.setFlat(False)
        self.loginBtn.setObjectName("loginBtn")
        self.verticalLayout.addWidget(self.loginBtn)
        Authorization.setCentralWidget(self.centralwidget)

        self.retranslateUi(Authorization)
        QtCore.QMetaObject.connectSlotsByName(Authorization)

    def retranslateUi(self, Authorization):
        _translate = QtCore.QCoreApplication.translate
        Authorization.setWindowTitle(_translate("Authorization", "Inventory - Sign in"))
        self.signInLabel.setText(_translate("Authorization", "Sign in"))
        self.usernameLabel.setText(_translate("Authorization", "Username"))
        self.usernamePTE.setPlaceholderText(_translate("Authorization", "Enter the username"))
        self.passwordLabel.setText(_translate("Authorization", "Password"))
        self.passwordLE.setPlaceholderText(_translate("Authorization", "Enter the password"))
        self.loginBtn.setText(_translate("Authorization", "Login"))
