import sys
from PyQt4 import QtCore, QtGui, uic
from populate import b1_pop

qtCreatorFile = "raw/gui.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == '__main__':
    b1_pop()
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()

sys.exit(app.exec_())

