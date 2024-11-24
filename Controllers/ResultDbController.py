from PySide6 import QtWidgets, QtSql
from Entities.Result import Result


class ResultDbController:
    @staticmethod
    def create_connection():
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('schulte_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Ошибка", "Не получилось открыть базу данных", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS results (ID integer primary key AUTOINCREMENT,"
                   " Time_1 real, Time_2 real, Time_3 real, Time_4 real, Time_5 real, Num_of_errors integer)")

        return True

    @staticmethod
    def _execute_query(sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for value in query_values:
                query.addBindValue(value)

        query.exec()
        return query

    @staticmethod
    def add_new_result(result: Result):
        times = result.get_times()
        num_of_errors = result.get_num_of_errors()

        # Создание параметров запроса с округленными временами
        params = times + [num_of_errors]

        # SQL-запрос для вставки данных
        sql_query = ("INSERT INTO results (Time_1, Time_2, Time_3, Time_4, Time_5, Num_of_errors)"
                     " VALUES (?, ?, ?, ?, ?, ?)")

        # Выполнение запроса
        ResultDbController._execute_query(sql_query, params)

    @staticmethod
    def get_all_results():
        query = ResultDbController._execute_query("SELECT * FROM results")
        results = []

        while query.next():
            result = Result(
                id=query.value(0),
                times=[query.value(1), query.value(2), query.value(3), query.value(4), query.value(5)],
                num_of_errors=query.value(6)
            )
            results.append(result)

        return results

    @staticmethod
    def get_latest_result():
        query = ResultDbController._execute_query("SELECT * FROM results ORDER BY ID DESC LIMIT 1")
        if query.next():

            result = Result(
                id=query.value(0),
                times=[query.value(1), query.value(2), query.value(3), query.value(4), query.value(5)],
                num_of_errors=query.value(6)
            )
            return result

        return None


ResultDbController.create_connection()
