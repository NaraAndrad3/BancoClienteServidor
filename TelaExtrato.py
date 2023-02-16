


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaExtrato(object):
    def setupUi(self, TelaExtrato):
        TelaExtrato.setObjectName("TelaExtrato")
        TelaExtrato.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(TelaExtrato)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 50, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 100, 241, 171))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 280, 89, 25))
        self.pushButton.setObjectName("pushButton")
        TelaExtrato.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaExtrato)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        TelaExtrato.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaExtrato)
        self.statusbar.setObjectName("statusbar")
        TelaExtrato.setStatusBar(self.statusbar)

        self.retranslateUi(TelaExtrato)
        QtCore.QMetaObject.connectSlotsByName(TelaExtrato)

    def retranslateUi(self, TelaExtrato):
        _translate = QtCore.QCoreApplication.translate
        TelaExtrato.setWindowTitle(_translate("TelaExtrato", "MainWindow"))
        self.label.setText(_translate("TelaExtrato", "Extrato"))
        self.pushButton.setText(_translate("TelaExtrato", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaExtrato = QtWidgets.QMainWindow()
    ui = TelaExtrato()
    ui.setupUi(TelaExtrato)
    TelaExtrato.show()
    sys.exit(app.exec_())
