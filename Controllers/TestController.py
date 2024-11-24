import time
from PySide6.QtCore import QTimer
from Controllers.ResultDbController import ResultDbController
from Entities.Result import Result

class TestController:
    def __init__(self, table, test_window, main_window):
        self.__table = table
        self.__test_window = test_window
        self.__main_window = main_window

        self.__start_time = None
        self.__end_time = None

        self.__expected_value = 1
        self.__errors = 0
        self.__times = []
        self.__current_test = 1
        self.__total_tests = 5
        self.__max_test_time = 60

        self.__test_window.connect_buttons(self)
        self._set_start_time()
        self.__timer = QTimer()
        self.__timer.timeout.connect(self._check_test_time)
        self.__timer.start(1000)

    def cell_clicked(self, value):
        if value == self.__expected_value:
            self.__expected_value += 1
            if self.__expected_value <= self.__table.get_n() * self.__table.get_n():
                self.__test_window.update_info_label(f"Найдите число: {self.__expected_value}")
            if self.__expected_value > self.__table.get_n() * self.__table.get_n():
                self._set_end_time()
                self.__times.append(self.__end_time - self.__start_time)
                self._handle_results()
        else:
            self.__errors += 1

    def _set_start_time(self):
        self.__start_time = time.time()

    def _set_end_time(self):
        self.__end_time = time.time()

    def _check_test_time(self):
        if time.time() - self.__start_time > self.__max_test_time:
            self.__timer.stop()
            self.__test_window.show_timeout_message()

    def _handle_results(self):
        total_time = self.__end_time - self.__start_time
        self.__timer.stop()
        clicked_button, next_button, exit_button = self.__test_window.show_intermediate_result(self.__current_test, total_time, self.__errors)

        if clicked_button == next_button:
            if self.__current_test < self.__total_tests:
                self._next_test()
            else:
                result = Result(id=None, times=self.__times, num_of_errors=self.__errors)
                ResultDbController.add_new_result(result)
                self.__test_window.show_final_results()
        elif clicked_button == exit_button:
            self.__test_window.close()
            self.__main_window.show()

    def _next_test(self):
        self.__current_test += 1
        self.__expected_value = 1
        self.__test_window.update_info_label(f"Найдите число: {self.__expected_value}")
        self.__test_window.disconnect_buttons()
        self.__table.create_table()
        self.__test_window.connect_buttons(self)
        self._set_start_time()
        self.__timer.start(1000)
