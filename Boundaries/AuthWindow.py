from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from Boundaries.UiAuthWindow import Ui_AuthWindow
from Boundaries.ResultsWindow import ResultsWindow
from Controllers.AuthController import AuthController


class AuthWindow(QMainWindow):
    def __init__(self, main_window, admin_account):
        super().__init__()
        self.__ui = Ui_AuthWindow()
        self.__ui.setupUi(self)
        self.__results_window = None

        # Сохраняем ссылку на главное окно и аккаунт администратора
        self.__main_window = main_window
        self.__auth_controller = AuthController(admin_account)

        # Подключаем кнопки
        self.__ui.toMainButton.clicked.connect(self._open_main_window)
        self.__ui.enterButton.clicked.connect(self._handle_auth)

    def _open_main_window(self):
        self.close()  # Закрываем окно авторизации
        self.__main_window.show()  # Показываем главное окно

    def _open_results_window(self):
        self.close()
        self.__results_window = ResultsWindow(self.__main_window, self.__auth_controller)
        self.__results_window.show()

    def _check_password(self, password):
        return self.__auth_controller.authenticate(password)

    def _handle_auth(self):
        password = self.__ui.passwordEdit.text()
        if self._check_password(password):
            self._open_results_window()
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Неверный пароль")
