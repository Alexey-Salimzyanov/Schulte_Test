import time
import functools
from PySide6.QtWidgets import QWidget, QPushButton, QMainWindow, QApplication, QVBoxLayout, QLabel, QMessageBox
from Result import result
from AuthController import AuthController
from AdminAccount import admin_account
from MyResultsWindow import ResultsWindow

class TestController:
    def __init__(self, table, test_window, main_window, results_window):
        self.table = table
        self.result = result
        self.test_window = test_window
        self.main_window = main_window
        self.expected_value = 1
        self.errors = 0
        self.__start_time = None
        self.__end_time = None
        self.__times = []
        self.current_test = 1
        self.total_tests = 5
        self.info_label = QLabel(test_window)
        self.info_label.setText(f"Find the number: {self.expected_value}")
        self.info_label.move(50, 20)
        self.info_label.show()
        self.connect_buttons()

    def connect_buttons(self):
        for button in self.table.buttons:
            button.clicked.connect(functools.partial(self.cell_clicked, button.value))
        self.set_start_time()

    def disconnect_buttons(self):
        for button in self.table.buttons:
            button.clicked.disconnect()

    def update_info_label(self):
        self.info_label.setText(f"Find the number: {self.expected_value}")

    def cell_clicked(self, value):
        if value == self.expected_value:
            print(f"Correct: {value}")
            self.expected_value += 1
            self.update_info_label()
            if self.expected_value > self.table.n * self.table.n:
                self.set_end_time()
                self.__times.append(self.__end_time - self.__start_time)
                self.display_results()
        else:
            print(f"Wrong: {value}. Expected: {self.expected_value}")
            self.errors += 1

    def set_start_time(self):
        self.__start_time = time.time()

    def set_end_time(self):
        self.__end_time = time.time()

    def display_results(self):
        total_time = self.__end_time - self.__start_time
        msg_box = QMessageBox()
        msg_box.setWindowTitle(f"Test {self.current_test} Results")
        msg_box.setText(f"Test {self.current_test} completed successfully!\n"
                        f"Time taken: {total_time:.2f} seconds\n"
                        f"Number of errors: {self.errors}")
        if self.current_test < self.total_tests:
            next_button = msg_box.addButton("Next Test", QMessageBox.AcceptRole)
        else:
            next_button = msg_box.addButton("Show All Results", QMessageBox.AcceptRole)
        exit_button = msg_box.addButton("Exit to Main Window", QMessageBox.RejectRole)
        msg_box.exec()

        if msg_box.clickedButton() == next_button:
            if self.current_test < self.total_tests:
                self.next_test()
            else:
                self.result.add_new_result_query(self.__times, self.errors)
                self.show_all_results()
        elif msg_box.clickedButton() == exit_button:
            self.close_test_window()
            self.main_window.show()

    def next_test(self):
        self.current_test += 1
        self.expected_value = 1
        self.update_info_label()
        self.disconnect_buttons()
        self.table.create_table()
        self.connect_buttons()

    def close_test_window(self):
        self.test_window.close()

    def show_all_results(self):
        self.test_window.close()
        self.auth_controller = AuthController(admin_account)
        self.results_window = ResultsWindow(self.main_window, self.auth_controller)  # Создаем экземпляр окна результатов
        self.results_window.show()
        pass

