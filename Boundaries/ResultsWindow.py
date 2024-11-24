from Controllers.ShowResultsController import ShowResultsController
from Controllers.ResultDbController import ResultDbController
from Boundaries.UiResultsWindow import Ui_ResultsWindow
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem


class ResultsWindow(QMainWindow):
    def __init__(self, main_window, auth_controller):
        super().__init__()
        self.__ui = Ui_ResultsWindow()
        self.__ui.setupUi(self)
        self.__main_window = main_window
        self.__auth_controller = auth_controller
        # Создаем контроллер результатов
        self.__show_results_controller = ShowResultsController( auth_controller)

        self.__ui.exitButton.clicked.connect(self._exit)

        # Загрузка и отображение результатов
        self._load_results()

    def _load_results(self):
        results = self.__show_results_controller.get_results()
        self.__ui.resultsTableWidget.setRowCount(len(results))

        for row_index, result in enumerate(results):
            self.__ui.resultsTableWidget.setItem(row_index, 0, QTableWidgetItem(str(result.get_id())))
            times = result.get_times()

            for col_index, time in enumerate(times):
                self.__ui.resultsTableWidget.setItem(row_index, col_index + 1, QTableWidgetItem(str(time)))

            self.__ui.resultsTableWidget.setItem(row_index, 6, QTableWidgetItem(str(result.get_num_of_errors())))
            self.__ui.resultsTableWidget.setItem(row_index, 7, QTableWidgetItem(str(result.ER)))
            self.__ui.resultsTableWidget.setItem(row_index, 8, QTableWidgetItem(str(result.VR)))
            self.__ui.resultsTableWidget.setItem(row_index, 9, QTableWidgetItem(str(result.PU)))

    def _exit(self):
        self.__auth_controller.auth_status = False
        self.close()  # Закрываем окно авторизации
        self.__main_window.show()  # Показываем главное окно


