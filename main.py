import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.businessBox.toggled.connect(self.calculate)
        self.ui.economicBox.toggled.connect(self.calculate)
        self.ui.firstBox.toggled.connect(self.calculate)
        self.show()

    def calculate(self):
        price = 0
        if self.ui.businessBox.isChecked():
            price += 300
        if self.ui.economicBox.isChecked():
            price += 5
        if self.ui.firstBox.isChecked():
            price += 500

        self.ui.resultLabel.setText(f'Cena: {price}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())