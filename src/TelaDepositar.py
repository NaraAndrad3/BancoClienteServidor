


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaDepositar(object):
    """
        Classe que representa a tela de depósito e todas as suas configurações pré definidas
    """
    def setupUi(self, TelaDepositar):
        TelaDepositar.setObjectName("TelaDepositar")
        TelaDepositar.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(TelaDepositar)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 80, 111, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 80, 241, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 110, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 110, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        TelaDepositar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaDepositar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        TelaDepositar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaDepositar)
        self.statusbar.setObjectName("statusbar")
        TelaDepositar.setStatusBar(self.statusbar)

        self.retranslateUi(TelaDepositar)
        QtCore.QMetaObject.connectSlotsByName(TelaDepositar)

    def retranslateUi(self, TelaDepositar):
        _translate = QtCore.QCoreApplication.translate
        TelaDepositar.setWindowTitle(_translate("TelaDepositar", "MainWindow"))
        self.label.setText(_translate("TelaDepositar", "Depositar"))
        self.label_2.setText(_translate("TelaDepositar", "Valor:      R$"))
        self.pushButton.setText(_translate("TelaDepositar", "Confirmar"))
        self.pushButton_2.setText(_translate("TelaDepositar", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaDepositar = QtWidgets.QMainWindow()
    ui = TelaDepositar()
    ui.setupUi(TelaDepositar)
    TelaDepositar.show()
    sys.exit(app.exec_())
