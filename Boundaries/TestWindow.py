from PySide6.QtWidgets import QMainWindow, QMessageBox, QLabel
from Boundaries.UiTestWindow import Ui_TestWindow
from Entities.SchulteTable import SchulteTable
from Controllers.TestController import TestController
from Controllers.AuthController import AuthController
from Entities.AdminAccount import admin_account
from Boundaries.ResultsWindow import ResultsWindow
import functools


class TestWindow(QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()
        self.__ui = Ui_TestWindow()
        self.__ui.setupUi(self)

        self.__main_window = main_window

        self.__info_label = QLabel(self)
        self.__info_label.setStyleSheet("font-size: 30px; font-weight: bold;")
        self.__info_label.setText("Найдите число: 1")
        self.__info_label.setFixedWidth(300)
        self.__info_label.move(400, 20)
        self.__info_label.show()

        self.__table = SchulteTable(2, 250, 85, self.__ui.centralwidget)
        self.__table.create_table()

        self.__controller = TestController(self.__table, self, self.__main_window)
        self.__ui.exitButton.clicked.connect(self._go_to_main_window)

    def _go_to_main_window(self):
        self.__main_window.show()
        self.close()

    def connect_buttons(self, controller):
        for button in self.__table.get_buttons():
            button.clicked.connect(functools.partial(controller.cell_clicked, button.get_value()))

    def disconnect_buttons(self):
        for button in self.__table.get_buttons():
            button.clicked.disconnect()

    def show_timeout_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Test Timeout")
        msg_box.setText("Превышено максимальное время выполнения теста")
        msg_box.addButton("Вернуться на главную", QMessageBox.AcceptRole)
        msg_box.exec()
        self.close()
        self.__main_window.show()

    def update_info_label(self, text):
        self.__info_label.setText(text)

    def show_final_results(self):
        self.close()
        self.__auth_controller = AuthController(admin_account)
        self.__results_window = ResultsWindow(self.__main_window, self.__auth_controller)
        self.__results_window.show()

    @staticmethod
    def show_intermediate_result(current_test, total_time, errors):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(f"Результаты {current_test} теста")
        msg_box.setText(f"Тест {current_test} успешно пройден!\n"
                        f"Затраченное время: {total_time:.2f} секунд\n"
                        f"Суммарное число ошибок: {errors}")
        if current_test < 5:
            next_button = msg_box.addButton("Следующий тест", QMessageBox.AcceptRole)
        else:
            next_button = msg_box.addButton("Показать все результаты", QMessageBox.AcceptRole)
        exit_button = msg_box.addButton("Выйти на главную", QMessageBox.RejectRole)
        msg_box.exec()

        return msg_box.clickedButton(), next_button, exit_button

