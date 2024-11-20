import random
import functools
from PySide6.QtWidgets import QWidget, QPushButton, QSizePolicy
from CellOfTable import CellOfTable

import random
import time
import functools
from PySide6.QtWidgets import QWidget, QPushButton, QMainWindow, QApplication, QVBoxLayout, QMessageBox





class SchulteTable(QWidget):
    def __init__(self, n, start_x, start_y, parent=None):
        super().__init__(parent)
        self.n = n
        self.start_x = start_x
        self.start_y = start_y
        self.button_size = 100
        self.interval = 10
        self.CurrentValue = None  # Атрибут для хранения текущего значения
        self.buttons = []  # Список для хранения кнопок

    def create_table(self):
        values = list(range(1, self.n * self.n + 1))
        random.shuffle(values)

        if not self.buttons:
            for row in range(self.n):
                for col in range(self.n):
                    value = values.pop()
                    button = CellOfTable(value, self)
                    button.setFixedSize(self.button_size, self.button_size)
                    x = self.start_x + col * (self.button_size + self.interval)
                    y = self.start_y + row * (self.button_size + self.interval)
                    button.move(x, y)
                    self.buttons.append(button)  # Добавляем кнопку в список
        else:
            for button, value in zip(self.buttons, values):
                button.update_value(value)



