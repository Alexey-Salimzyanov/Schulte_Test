from PySide6.QtWidgets import QWidget, QPushButton, QSizePolicy


class CellOfTable(QPushButton):
    def __init__(self, value, parent=None):
        super().__init__(str(value), parent)
        self.value = value
        self.setText(str(value))
        self.setFontSize(40)

    def update_value(self, value):
        self.value = value
        self.setText(str(value))
        self.setFontSize(40)

    def setFontSize(self, size):
        self.setStyleSheet(f"font-size: {size}px;")

