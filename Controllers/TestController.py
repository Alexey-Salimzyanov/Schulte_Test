import time
import functools
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QLabel, QMessageBox
from Controllers.ResultDbController import result_db
from Controllers.AuthController import AuthController
from Entities.AdminAccount import admin_account
from Boundaries.ResultsWindow import ResultsWindow
from Entities.Result import Result

class TestController:
    def __init__(self, table, test_window, main_window):
        self.__table = table
        self.__result_db = result_db
        self.__test_window = test_window
        self.__main_window = main_window
        self.__expected_value = 1
        self.__errors = 0
        self.__start_time = None
        self.__end_time = None
        self.__times = []
        self.__current_test = 1
        self.__total_tests = 5
        self.__max_test_time = 60  # Максимальное время выполнения теста в секундах

        self.__info_label = QLabel(test_window)
        self.__info_label.setText(f"Найдите число: {self.__expected_value}")
        self.__info_label.setStyleSheet("font-size: 30px; font-weight: bold;")
        self.__info_label.setFixedWidth(300)
        self.__info_label.move(400, 20)
        self.__info_label.show()

        self.__connect_buttons()

        # Настройка таймера для проверки времени выполнения теста
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__check_test_time)
        self.__timer.start(1000)

    def __connect_buttons(self):
        for button in self.__table.buttons:
            button.clicked.connect(functools.partial(self.__cell_clicked, button.value))
        self.__set_start_time()

    def __disconnect_buttons(self):
        for button in self.__table.buttons:
            button.clicked.disconnect()

    def __update_info_label(self):
        self.__info_label.setText(f"Найдите число: {self.__expected_value}")

    def __cell_clicked(self, value):
        if value == self.__expected_value:
            self.__expected_value += 1
            if self.__expected_value <= self.__table.n * self.__table.n:
                self.__update_info_label()
            if self.__expected_value > self.__table.n * self.__table.n:
                self.__set_end_time()
                self.__times.append(self.__end_time - self.__start_time)
                self.__display_results()
        else:
            self.__errors += 1

    def __set_start_time(self):
        self.__start_time = time.time()

    def __set_end_time(self):
        self.__end_time = time.time()

    def __check_test_time(self):
        if time.time() - self.__start_time > self.__max_test_time:
            self.__timer.stop()
            self.__show_timeout_message()

    def __show_timeout_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Test Timeout")
        msg_box.setText("Превышено максимальное время выполнения теста")
        msg_box.addButton("Вернуться на главную", QMessageBox.AcceptRole)
        msg_box.exec()
        self.__close_test_window()
        self.__main_window.show()

    def __display_results(self):
        total_time = self.__end_time - self.__start_time
        self.__timer.stop()
        msg_box = QMessageBox()
        msg_box.setWindowTitle(f"Результаты {self.__current_test} теста")
        msg_box.setText(f"Тест {self.__current_test} успешно пройден!\n"
                        f"Затраченное время: {total_time:.2f} секунд\n"
                        f"Суммарное число ошибок: {self.__errors}")
        if self.__current_test < self.__total_tests:
            next_button = msg_box.addButton("Следующий тест", QMessageBox.AcceptRole)
        else:
            next_button = msg_box.addButton("Показать все результаты", QMessageBox.AcceptRole)
        exit_button = msg_box.addButton("Выйти на главную", QMessageBox.RejectRole)
        msg_box.exec()

        if msg_box.clickedButton() == next_button:
            if self.__current_test < self.__total_tests:
                self.__next_test()
            else:
                result = Result(times=self.__times, num_of_errors=self.__errors)
                self.__result_db.add_new_result(result)
                self.__show_all_results()
        elif msg_box.clickedButton() == exit_button:
            self.__close_test_window()
            self.__main_window.show()

    def __next_test(self):
        self.__current_test += 1
        self.__expected_value = 1
        self.__update_info_label()
        self.__disconnect_buttons()
        self.__table.create_table()
        self.__connect_buttons()
        self.__timer.start(1000)  # Перезапуск таймера для нового теста

    def __close_test_window(self):
        self.__test_window.close()

    def __show_all_results(self):
        self.__test_window.close()
        self.__auth_controller = AuthController(admin_account)
        self.__results_window = ResultsWindow(self.__main_window, self.__auth_controller)  # Создаем экземпляр окна результатов
        self.__results_window.show()
