import sys
from PySide6 import QtGui, QtCore, QtWidgets

app = QtWidgets.QApplication(sys.argv)
fenetre = QtWidgets.QWidget()
fenetre.setWindowTitle("Mon Application")
h = w = 500
fenetre.resize(w, h)
fenetre.move(int(500-w/2), 500-h/2)

fenetre.show()
app.exec()
