
from PyQt5 import QtCore, QtGui, QtWidgets


class TelaSacar(object):
    def setupUi(self, TelaSacar):
        TelaSacar.setObjectName("TelaSacar")
        TelaSacar.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(TelaSacar)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 90, 251, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 90, 81, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 150, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 150, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 120, 251, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 120, 67, 17))
        self.label_4.setObjectName("label_4")
        TelaSacar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaSacar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        TelaSacar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaSacar)
        self.statusbar.setObjectName("statusbar")
        TelaSacar.setStatusBar(self.statusbar)

        self.retranslateUi(TelaSacar)
        QtCore.QMetaObject.connectSlotsByName(TelaSacar)

    def retranslateUi(self, TelaSacar):
        _translate = QtCore.QCoreApplication.translate
        TelaSacar.setWindowTitle(_translate("TelaSacar", "MainWindow"))
        self.label.setText(_translate("TelaSacar", "sacar"))
        self.label_3.setText(_translate("TelaSacar", "Valor:    R$"))
        self.pushButton.setText(_translate("TelaSacar", "Confirmar"))
        self.pushButton_2.setText(_translate("TelaSacar", "Voltar"))
        self.label_4.setText(_translate("TelaSacar", "Senha:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaSacar = QtWidgets.QMainWindow()
    ui = TelaSacar()
    ui.setupUi(TelaSacar)
    TelaSacar.show()
    sys.exit(app.exec_())
