from PySide6.QtWidgets import QMainWindow
from Boundaries.UiMainWindow import Ui_MainWindow
from Boundaries.AuthWindow import AuthWindow
from Boundaries.TestWindow import TestWindow
from Entities.AdminAccount import admin_account
from functools import partial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__auth_window = None
        self.__test_window = None

        # Подключаем событие нажатия на кнопку
        self.__ui.authButton.clicked.connect(partial(self._open_auth_window, admin_account))
        self.__ui.startTestButton.clicked.connect(self._open_test_window)

    def _open_auth_window(self, account):
        self.hide()  # Скрываем главное окно
        self.__auth_window = AuthWindow(self, account)
        self.__auth_window.show()  # Показываем окно авторизации

    def _open_test_window(self):
        self.hide()  # Скрываем главное окно
        self.__test_window = TestWindow(self)
        self.__test_window.show()
