#coding=utf-8
import sys

## Parte 2
## Temas:
# - Importar GUI desde QtDesigner
# - QLineEdit (Recibir input como texto)
# - Añadir Métodos (y conectarlos)
# - Mostrar un Diálogo Hijo

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Ui_MainWindow import Ui_MainWindow

class Sumador(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.sumButton.clicked.connect(self.add)

    def add(self):
        try:
            num1 = int(self.lineEdit_1.text())
            num2 = int(self.lineEdit_2.text())
        except ValueError:
            QMessageBox.critical(self, "ERROR", "Valor inválido para un número")
            self.lineEdit_1.setText("")
            self.lineEdit_2.setText("")
            return

        self.lineEdit_3.setText(str(num1+num2))


if __name__ == "__main__":
    APP = QApplication(sys.argv)

    GUI = Sumador()
    GUI.show()

    sys.exit(APP.exec_())
