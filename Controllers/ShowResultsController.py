from Controllers.ResultDbController import ResultDbController
from Entities.Estimation import Estimation
from Controllers.AuthController import AuthController


class ShowResultsController:
    def __init__(self, auth_controller: AuthController):

        self.__auth_controller = auth_controller

    def get_results(self):
        if self.__auth_controller.get_auth_status():
            results = ResultDbController.get_all_results()
        else:
            latest_result = ResultDbController.get_latest_result()
            results = [latest_result] if latest_result else []

        # Формируем дополнительные метрики
        for result in results:
            if result is not None:
                estimation = Estimation(result)
                result.ER = estimation.ER
                result.VR = estimation.VR
                result.PU = estimation.PU

        return results
