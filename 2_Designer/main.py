#coding=utf-8
import sys

# # Temas:

# - Importar GUI desde QtDesigner
# - QLineEdit (Recibir input como texto)
# - Añadir Métodos (y conectarlos)
# - Mostrar un Diálogo Hijo

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class Sumador(QMainWindow):
    pass


if __name__ == "__main__":
    APP = QApplication(sys.argv)

    GUI = Sumador()
    GUI.show()

    sys.exit(APP.exec_())
