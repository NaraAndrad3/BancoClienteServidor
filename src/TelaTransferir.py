


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaTransferir(object):
    def setupUi(self, TelaTransferir):
        TelaTransferir.setObjectName("TelaTransferir")
        TelaTransferir.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(TelaTransferir)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 100, 71, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 130, 67, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 130, 271, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 100, 271, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 160, 271, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 160, 67, 17))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 190, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 190, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        TelaTransferir.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaTransferir)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        TelaTransferir.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaTransferir)
        self.statusbar.setObjectName("statusbar")
        TelaTransferir.setStatusBar(self.statusbar)

        self.retranslateUi(TelaTransferir)
        QtCore.QMetaObject.connectSlotsByName(TelaTransferir)

    def retranslateUi(self, TelaTransferir):
        _translate = QtCore.QCoreApplication.translate
        TelaTransferir.setWindowTitle(_translate("TelaTransferir", "MainWindow"))
        self.label.setText(_translate("TelaTransferir", "Transferência"))
        self.label_3.setText(_translate("TelaTransferir", "Valor:   R$"))
        self.label_4.setText(_translate("TelaTransferir", "Destino:"))
        self.label_5.setText(_translate("TelaTransferir", "Senha:"))
        self.pushButton.setText(_translate("TelaTransferir", "Confirmar"))
        self.pushButton_2.setText(_translate("TelaTransferir", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaTransferir = QtWidgets.QMainWindow()
    ui = TelaTransferir()
    ui.setupUi(TelaTransferir)
    TelaTransferir.show()
    sys.exit(app.exec_())
