from PySide6.QtWidgets import QMainWindow
from Boundaries.UiTestWindow import Ui_TestWindow
from Entities.SchulteTable import SchulteTable
from Controllers.TestController import TestController


class TestWindow(QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()
        self.ui = Ui_TestWindow()
        self.ui.setupUi(self)

        self.main_window = main_window

        self.table = SchulteTable(5, 250, 85, self.ui.centralwidget)
        self.table.create_table()

        self.controller = TestController(self.table, self, self.main_window)
        self.ui.exitButton.clicked.connect(self.go_to_main_window)

    def go_to_main_window(self):
        self.main_window.show()
        self.close()
