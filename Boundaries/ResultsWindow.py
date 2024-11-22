from Controllers.ShowResultsController import ShowResultsController
from Controllers.ResultDbController import result_db
from Boundaries.UiResultsWindow import Ui_ResultsWindow
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem


class ResultsWindow(QMainWindow):
    def __init__(self, main_window, auth_controller):
        super().__init__()
        self.ui = Ui_ResultsWindow()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.auth_controller = auth_controller
        # Создаем контроллер результатов
        self.results_controller = ShowResultsController(result_db, auth_controller)

        self.ui.exitButton.clicked.connect(self.Exit)

        # Загрузка и отображение результатов
        self.load_results()

    def load_results(self):
        results = self.results_controller.get_results()
        self.ui.resultsTableWidget.setRowCount(len(results))

        for row_index, result in enumerate(results):
            self.ui.resultsTableWidget.setItem(row_index, 0, QTableWidgetItem(str(row_index + 1)))
            times = result.get_times()

            for col_index, time in enumerate(times):
                self.ui.resultsTableWidget.setItem(row_index, col_index + 1, QTableWidgetItem(str(time)))

            self.ui.resultsTableWidget.setItem(row_index, 6, QTableWidgetItem(str(result.get_num_of_errors())))
            self.ui.resultsTableWidget.setItem(row_index, 7, QTableWidgetItem(str(result.ER)))
            self.ui.resultsTableWidget.setItem(row_index, 8, QTableWidgetItem(str(result.VR)))
            self.ui.resultsTableWidget.setItem(row_index, 9, QTableWidgetItem(str(result.PU)))

    def Exit(self):
        self.auth_controller.auth_status = False
        self.close()  # Закрываем окно авторизации
        self.main_window.show()  # Показываем главное окно


