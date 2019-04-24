#coding=utf-8
import sys
import os

## Parte 3
## Temas:
# - QTextEdit
# - Añadir miembros a la clase
# - Añadir Menu
# - Añadir About
# - argv arguments
# - Layout

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QColorDialog
from PyQt5.QtGui import QFont
from Ui_Editor import Ui_MainWindow

class Editor(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, file=None):
        super().__init__(parent)
        self.setupUi(self)
        self.actionNew.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(lambda: self.openFile(None))
        self.actionSave.triggered.connect(self.saveFile)
        self.actionChangeColor.triggered.connect(self.changeColor)

        self.actionAbout.triggered.connect(self.about)
        self.actionAboutQt.triggered.connect(lambda: QMessageBox.aboutQt(self, "About Qt"))
        self.textEdit.textChanged.connect(lambda: self.setWindowModified(True))

        self.textEdit.cursorPositionChanged.connect(self.updateLineCol)
        self.textEdit.cursorPositionChanged.connect(self.updateFont)
        self.statusbar.showMessage("Ln 1, Col 1")
        self.fontComboBox.setEditable(False)
        self.toolBar_2.addWidget(self.fontComboBox)
        self.toolBar_2.addWidget(self.doubleSpinBox)

        self.titleTemplate = "[*] -- ENES Editor"
        self.fileName = file

        if file is not None and not os.path.exists(self.fileName):
            self.fileName = None

        if self.fileName is None:
            self.newFile()
        else:
            self.openFile(self.fileName)
            self._baseFile = os.path.basename(self.fileName)

    def updateFont(self):
        FontFam = self.textEdit.currentFont().family()
        indexOf = self.fontComboBox.findText(FontFam)
        self.fontComboBox.setCurrentIndex(indexOf)

    def about(self):
        MBox = QMessageBox(self)
        MBox.resize(240, 110)
        MBox.setWindowTitle("Acerca De")
        MBox.setText("ENES Editor<br>Un programa hecho para la FILSOL 2019<br>Carita Feliz 😀")
        MBox.show()

    def changeColor(self):
        ColorD = QColorDialog(self)
        ColorD.colorSelected.connect(self.textEdit.setTextColor)
        ColorD.open()

    def newFile(self):
        self.fileName = None
        self._baseFile = None
        self.setWindowTitle("Sin Título" + self.titleTemplate)
        self.textEdit.clear()

    def openFile(self, file):
        if file is None:
            # Nombre del Archivo
            tmpFile, ok = QFileDialog.getOpenFileName(self, "Abrir un Archivo", "./")
            if not ok:
                return
            self.fileName = tmpFile

        # Ponerlo en el título
        self._baseFile = os.path.basename(self.fileName)
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        # Abrir su contenido
        self.textEdit.clear()
        with open(self.fileName, 'r') as f:
            self.textEdit.setPlainText(f.read())

        self.setWindowModified(False)

    def saveFile(self):
        if not self.isWindowModified():
            return

        if self.fileName is None:
            tmpFile, ok = QFileDialog.getSaveFileName(self, "Guardar el archivo", "./")
            if not ok:
                return
            self.fileName = tmpFile
            self._baseFile = os.path.basename(self.fileName)
        self.setWindowTitle(self._baseFile + self.titleTemplate)

        with open(self.fileName, 'w') as f:
            f.write(self.textEdit.toPlainText())
        self.setWindowModified(False)

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
