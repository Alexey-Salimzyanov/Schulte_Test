from Entities.CellOfTable import CellOfTable
import random
from PySide6.QtWidgets import QWidget


class SchulteTable(QWidget):
    def __init__(self, n, start_x, start_y, parent=None):
        super().__init__(parent)
        self.__n = n

        self.__start_x = start_x
        self.__start_y = start_y
        self.__button_size = 100
        self.__interval = 10

        self.__buttons = []

    def create_table(self):
        values = list(range(1, self.__n * self.__n + 1))
        random.shuffle(values)

        if not self.__buttons:
            for row in range(self.__n):
                for col in range(self.__n):
                    value = values.pop()
                    button = CellOfTable(value, self)
                    button.setFixedSize(self.__button_size, self.__button_size)
                    x = self.__start_x + col * (self.__button_size + self.__interval)
                    y = self.__start_y + row * (self.__button_size + self.__interval)
                    button.move(x, y)
                    self.__buttons.append(button)
        else:
            for button, value in zip(self.__buttons, values):
                button.update_value(value)

    def get_buttons(self):
        return self.__buttons

    def get_n(self):
        return self.__n

