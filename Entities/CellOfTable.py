from PySide6.QtWidgets import QPushButton


class CellOfTable(QPushButton):
    def __init__(self, value, parent=None):
        super().__init__(str(value), parent)
        self.__value = value
        self.setText(str(value))
        self._set_font_size(40)

    def update_value(self, value):
        self.__value = value
        self.setText(str(value))
        self._set_font_size(40)

    def _set_font_size(self, size):
        self.setStyleSheet(f"font-size: {size}px;")

    def get_value(self):
        return self.__value

