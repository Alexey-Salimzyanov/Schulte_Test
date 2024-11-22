from Controllers.ResultDbController import ResultDbController
from Entities.Estimation import Estimation
from Controllers.AuthController import AuthController
from Entities.Result import Result


class ShowResultsController:
    def __init__(self, result_db: ResultDbController, auth_controller: AuthController):
        self.result_db = result_db
        self.result_db.create_connection()
        self.auth_controller = auth_controller

    def get_results(self):
        if self.auth_controller.auth_status:
            results = self.result_db.get_all_results()
        else:
            latest_result = self.result_db.get_latest_result()
            results = [latest_result] if latest_result else []

        # Формируем дополнительные метрики
        for result in results:
            if result is not None:
                estimation = Estimation(result)
                result.ER = estimation.ER
                result.VR = estimation.VR
                result.PU = estimation.PU

        return results
