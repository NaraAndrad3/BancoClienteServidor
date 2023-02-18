

from PyQt5 import QtCore, QtGui, QtWidgets


class TelaHistorico(object):
    """
        Classe que representa a tela de histórico e todas as suas configurações pré definidas
    """
    def setupUi(self, TelaHistorico):
        TelaHistorico.setObjectName("TelaHistorico")
        TelaHistorico.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(TelaHistorico)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 80, 301, 271))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 360, 89, 25))
        self.pushButton.setObjectName("pushButton")
        TelaHistorico.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaHistorico)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        TelaHistorico.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaHistorico)
        self.statusbar.setObjectName("statusbar")
        TelaHistorico.setStatusBar(self.statusbar)

        self.retranslateUi(TelaHistorico)
        QtCore.QMetaObject.connectSlotsByName(TelaHistorico)

    def retranslateUi(self, TelaHistorico):
        _translate = QtCore.QCoreApplication.translate
        TelaHistorico.setWindowTitle(_translate("TelaHistorico", "MainWindow"))
        self.label.setText(_translate("TelaHistorico", "Histórico"))
        self.pushButton.setText(_translate("TelaHistorico", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaHistorico = QtWidgets.QMainWindow()
    ui = TelaHistorico()
    ui.setupUi(TelaHistorico)
    TelaHistorico.show()
    sys.exit(app.exec_())
