import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.businessButton.toggled.connect(self.calculate)
        self.ui.economyButton.toggled.connect(self.calculate)
        self.ui.firstButton.toggled.connect(self.calculate)
        self.show()

    def calculate(self):
        print("ioio")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())