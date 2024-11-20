from PySide6 import QtWidgets, QtSql

class Result:

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('schulte_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Ошибка", "Не получилось открыть базу данных", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS results (ID integer primary key AUTOINCREMENT,"
                   " Time_1 real, Time_2 real, Time_3 real, Time_4 real, Time_5 real, Num_of_errors integer)")

        return True

    def execute_query(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for value in query_values:
                query.addBindValue(value)

        query.exec()
        return query

    def add_new_result_query(self, times: list, n_of_errors):
        print("QUERY ADDED")

        # Округление времен до сотых
        rounded_times = [round(time, 2) for time in times]

        # Создание параметров запроса с округленными временами
        params = rounded_times + [n_of_errors]

        # SQL-запрос для вставки данных
        sql_query = ("INSERT INTO results (Time_1, Time_2, Time_3, Time_4, Time_5, Num_of_errors)"
                     " VALUES (?, ?, ?, ?, ?, ?)")

        # Выполнение запроса
        self.execute_query(sql_query, params)
        print(self.get_all_results())

    def get_all_results(self):
        query = self.execute_query("SELECT * FROM results")
        results = []

        while query.next():
            record = {
                'ID': query.value(0),
                'Time_1': query.value(1),
                'Time_2': query.value(2),
                'Time_3': query.value(3),
                'Time_4': query.value(4),
                'Time_5': query.value(5),
                'Num_of_errors': query.value(6),
            }
            results.append(record)

        return results

    def get_latest_result(self):
        query = self.execute_query("SELECT * FROM results ORDER BY ID DESC LIMIT 1")
        if query.next():
            record = {
                'ID': query.value(0),
                'Time_1': query.value(1),
                'Time_2': query.value(2),
                'Time_3': query.value(3),
                'Time_4': query.value(4),
                'Time_5': query.value(5),
                'Num_of_errors': query.value(6),
            }
            return record

        return None


result = Result()
result.create_connection()
