import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from nice_calculator import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run_1)
        self.pushButton_2.clicked.connect(self.run_2)
        self.pushButton_3.clicked.connect(self.run_3)
        self.pushButton_4.clicked.connect(self.run_4)
        self.pushButton_5.clicked.connect(self.run_5)
        self.pushButton_6.clicked.connect(self.run_6)
        self.pushButton_7.clicked.connect(self.run_7)
        self.pushButton_8.clicked.connect(self.run_8)
        self.pushButton_9.clicked.connect(self.run_9)

    def run_1(self):
        self.lcdNumber.display(int(self.lineEdit.text()) + int(self.lineEdit_2.text()))

    def run_2(self):
        self.lcdNumber_2.display(int(self.lineEdit.text()) - int(self.lineEdit_2.text()))

    def run_3(self):
        self.lcdNumber_3.display(int(self.lineEdit.text()) * int(self.lineEdit_2.text()))

    def run_4(self):
        try:
            self.lcdNumber_4.display(int(self.lineEdit.text()) / int(self.lineEdit_2.text()))
        except ZeroDivisionError:
            self.lcdNumber_4.display('Error')

    def run_5(self):
        self.lcdNumber_5.display(int(self.lineEdit.text()) ** int(self.lineEdit_2.text()))

    def run_6(self):
        self.lcdNumber_6.display(math.sqrt(int(self.lineEdit.text())))

    def run_7(self):
        self.lcdNumber_7.display(math.sqrt(int(self.lineEdit_2.text())))

    def run_8(self):
        self.lcdNumber_8.display(math.factorial(int(self.lineEdit.text())))

    def run_9(self):
        self.lcdNumber_9.display(math.factorial(int(self.lineEdit_2.text())))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())