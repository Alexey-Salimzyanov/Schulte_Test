# main.py
import sys
import random
import time
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton,QWidget,QTableWidget,QWidget,QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from MainWindow import Ui_MainWindow
from AuthWindow import Ui_AuthWindow
from ResultsWindow import Ui_ResultsWindow
from TestWindow import Ui_TestWindow
from Result import result
from Estimation import Estimation
from AdminAccount import AdminAccount
from AuthController import AuthController
from ResultsController import ResultsController
from SchulteTable import SchulteTable
from TestController import TestController
from MyResultsWindow import ResultsWindow


class TestWindow(QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()
        self.ui = Ui_TestWindow()
        self.ui.setupUi(self)
        self.main_window = main_window
        # Создаем таблицу из кнопок размером 5x5 начиная с точки (50, 50)
        self.table = SchulteTable(2, 250, 50, self.ui.centralwidget)
        self.table.create_table()







        self.controller = TestController(self.table, self, self.main_window, self)
        # Настраиваем обработчик нажатия на кнопку выхода
        self.ui.exitButton.clicked.connect(self.go_to_main_window)

    def go_to_main_window(self):
        self.main_window.show()
        self.close()





class AuthWindow(QMainWindow):
    def __init__(self, main_window, admin_account):
        super().__init__()
        self.ui = Ui_AuthWindow()
        self.ui.setupUi(self)

        # Сохраняем ссылку на главное окно и аккаунт администратора
        self.main_window = main_window
        self.auth_controller = AuthController(admin_account)

        # Подключаем кнопки
        self.ui.toMainButton.clicked.connect(self.go_to_main)
        self.ui.enterButton.clicked.connect(self.check_authentication)

    def go_to_main(self):
        self.close()  # Закрываем окно авторизации
        self.main_window.show()  # Показываем главное окно

    def open_results_window(self):
        self.close()  # Закрываем окно авторизации
        self.results_window = ResultsWindow(self.main_window, self.auth_controller)  # Создаем экземпляр окна результатов
        self.results_window.show()  # Показываем окно результатов

    def check_authentication(self):
        password = self.ui.passwordEdit.text()
        if self.auth_controller.authenticate(password):
            QtWidgets.QMessageBox.information(self, "Успех", "Авторизация успешна")
            self.open_results_window()  # Переход на окно результатов при успешной авторизации
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Неверный пароль")

class MainWindow(QMainWindow):
    def __init__(self, admin_account):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.admin_account = admin_account

        # Подключаем событие нажатия на кнопку
        self.ui.authButton.clicked.connect(self.open_auth_window)
        self.ui.startTestButton.clicked.connect(self.open_test_window)

    def open_auth_window(self):
        self.hide()  # Скрываем главное окно
        self.auth_window = AuthWindow(self, self.admin_account)  # Передаем ссылку на главное окно и аккаунт администратора
        self.auth_window.show()  # Показываем окно авторизации

    def open_test_window(self):
        self.hide()  # Скрываем главное окно
        self.test_window = TestWindow(self)
        self.test_window.show()

app = QApplication(sys.argv)

# Создание аккаунта администратора
admin_account = AdminAccount("12345")

# Создание главного окна, передавая в него аккаунт администратора
window = MainWindow(admin_account)
window.show()

sys.exit(app.exec())


#---------------------проверка авторизации----------------------------
# # Создание аккаунта администратора
# admin = AdminAccount("12345")
#
# # Создание контроллера авторизации
# auth_controller = AuthController(admin)
#
# # Попытка авторизации
# password_to_check = "initialPassword"
# if auth_controller.authenticate(password_to_check):
#     print("Авторизация успешна.")
# else:
#     print("Неверный пароль.")


#-----------------проверка класса result, est ------------------------
# result = Result()
# # Создание соединения с базой данных
# if result.create_connection():
# # Добавление новой записи
#     times = [10.5, 9.8, 11.2, 10.0, 9.9]
#     number_of_errors = 2
#     result.add_new_result_query(times, number_of_errors)
#     print("success")
#     # Получение и вывод всех записей
#     all_results = result.get_all_results()
#     for record in all_results:
#         print(record)
#     res = result.get_latest_result()
#     print(res)
#     est = Estimation([12,34,54,23,34], 4)
#     print(est)

#----------------------команда pyside6-uic filename.ui -o filename.py --------------------