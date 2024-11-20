from PySide6.QtWidgets import QWidget, QPushButton, QSizePolicy


class CellOfTable(QPushButton):
    def __init__(self, value, parent=None):
        super().__init__(str(value), parent)
        self.value = value
        self.setText(str(value))

    def update_value(self, value):
        self.value = value
        self.setText(str(value))