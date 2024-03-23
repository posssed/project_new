import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class App(QMainWindow):
    def init(self):
        super().init()
        uic.loadUi('project.ui', self)
        self.dolar.clicked.connect(self.dollars)

    def dollars(self):
        pass


if App == 'main':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

App.show()
app.exec_()
