import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QAction, QTextEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__() # C-tor of deafult Class
        self.initUI() # UI - C-tor of this Class
        self.save_status = 0


    def initUI(self):
        # Window block
        self.resize(800,600)
        self.center()
        self.setWindowTitle('DyakinEditor') 
        self.setWindowIcon(QIcon('icon.png'))

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # Manu Block
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        self.statusBar().showMessage('Ready')

        

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    text = ex.textEdit.toPlainText()
    sys.exit(app.exec_())