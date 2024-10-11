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
        price = 0
        if self.ui.businessButton.isChecked():
            price = 300
        elif self.ui.economyButton.isChecked():
            price = 5
        elif self.ui.firstButton.isChecked():
            price = 500

        self.ui.resultLabel.setText(f'Price: {price}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())