#coding=utf-8
import sys
import os

## Parte 3
## Temas:
# - QTextEdit
# - Añadir miembros a la clase
# - Añadir Menu
# - QResources
# - Añadir About
# - argv arguments
# - Layout

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from Ui_Editor import Ui_MainWindow

class Editor(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, file=None):
        super().__init__(parent)
        self.setupUi(self)
        self.actionNew.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(lambda: self.openFile(None))
        self.actionSave.triggered.connect(self.saveFile)

        self.actionAbout.triggered.connect(self.about)
        self.actionAboutQt.triggered.connect(lambda: QMessageBox.aboutQt(self, "About Qt"))
        self.textEdit.textChanged.connect(lambda: self.setWindowModified(True))

        self.textEdit.cursorPositionChanged.connect(self.updateLineCol)

        self.titleTemplate = "[*] -- ENES Editor"
        self.fileName = file


    def about(self):
        MBox = QMessageBox(self)
        MBox.resize(240, 110)
        MBox.setWindowTitle("Acerca De")
        MBox.setText("ENES Editor<br>Un programa hecho para la FILSOL 2019<br>Carita Feliz 😀")
        MBox.show()

    def newFile(self):
        pass

    def openFile(self, file):
        pass

    def saveFile(self):
        pass

    def updateLineCol(self):
        line = self.textEdit.textCursor().blockNumber() + 1
        col = self.textEdit.textCursor().columnNumber() + 1
        self.statusbar.showMessage("Ln {}, Col {}".format(line, col))



if __name__ == "__main__":
    APP = QApplication(sys.argv)

    openFile = None
    if len(sys.argv) > 1:
        openFile = sys.argv[1]

    GUI = Editor(file=openFile)
    GUI.show()

    sys.exit(APP.exec_())
