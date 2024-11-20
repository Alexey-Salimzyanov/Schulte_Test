from ResultsController import ResultsController
from Result import result
from ResultsWindow import Ui_ResultsWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton,QWidget,QTableWidget,QWidget,QVBoxLayout

class ResultsWindow(QMainWindow):
    def __init__(self, main_window, auth_controller):
        super().__init__()
        self.ui = Ui_ResultsWindow()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.auth_controller = auth_controller
        # Создаем контроллер результатов
        self.results_controller = ResultsController(result, auth_controller)

        self.ui.exitButton.clicked.connect(self.Exit)

        # Загрузка и отображение результатов
        self.load_results()

    def load_results(self):
        results = self.results_controller.get_results()
        self.ui.resultsTableWidget.setRowCount(len(results))

        for row_index, record in enumerate(results):
            self.ui.resultsTableWidget.setItem(row_index, 0, QTableWidgetItem(str(record['ID'])))
            self.ui.resultsTableWidget.setItem(row_index, 1, QTableWidgetItem(str(record['Time_1'])))
            self.ui.resultsTableWidget.setItem(row_index, 2, QTableWidgetItem(str(record['Time_2'])))
            self.ui.resultsTableWidget.setItem(row_index, 3, QTableWidgetItem(str(record['Time_3'])))
            self.ui.resultsTableWidget.setItem(row_index, 4, QTableWidgetItem(str(record['Time_4'])))
            self.ui.resultsTableWidget.setItem(row_index, 5, QTableWidgetItem(str(record['Time_5'])))
            self.ui.resultsTableWidget.setItem(row_index, 6, QTableWidgetItem(str(record['Num_of_errors'])))
            self.ui.resultsTableWidget.setItem(row_index, 7, QTableWidgetItem(str(record['ER'])))
            self.ui.resultsTableWidget.setItem(row_index, 8, QTableWidgetItem(str(record['VR'])))
            self.ui.resultsTableWidget.setItem(row_index, 9, QTableWidgetItem(str(record['PU'])))

    def Exit(self):
        self.auth_controller.auth_status = False
        self.close()  # Закрываем окно авторизации
        self.main_window.show()  # Показываем главное окно