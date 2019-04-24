#coding=utf-8

# # Temas:

# - GUI que hereda de MainWindow
# - QLabel (Texto normal y html)
# - QPushbutton (conect slots)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class HelloWorld(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(500, 300)
        self.setWindowTitle("Esto es un titulo.")

        self.message = QLabel(self)
        self.message.setGeometry(50, 50, 400, 50)
        self.message.setAlignment(Qt.AlignCenter)
        self.message.setObjectName("message")
        textLabel = (""
                     "<div style='color:#f00;font-size:30px'>"
                     "HOLA MUNDO!!!"
                     "</div>")

        self.message.setText(textLabel)

        self.closeButton = QPushButton(self)
        self.closeButton.setGeometry(200, 120, 100, 50)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setText("Close")


if __name__ == "__main__":
    APP = QApplication(sys.argv)

    GUI = HelloWorld()
    GUI.show()

    sys.exit(APP.exec_())
