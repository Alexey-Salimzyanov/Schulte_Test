from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from Boundaries.UiAuthWindow import Ui_AuthWindow
from Boundaries.ResultsWindow import ResultsWindow
from Controllers.AuthController import AuthController


class AuthWindow(QMainWindow):
    def __init__(self, main_window, admin_account):
        super().__init__()
        self.ui = Ui_AuthWindow()
        self.ui.setupUi(self)
        self.results_window = None

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
        self.results_window = ResultsWindow(self.main_window, self.auth_controller)  # Создаем экземпляр окна результата
        self.results_window.show()  # Показываем окно результатов

    def check_authentication(self):
        password = self.ui.passwordEdit.text()
        if self.auth_controller.authenticate(password):
            QtWidgets.QMessageBox.information(self, "Успех", "Авторизация успешна")
            self.open_results_window()  # Переход на окно результатов при успешной авторизации
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Неверный пароль")
