from Result import Result
from Result import result
from Estimation import Estimation
from AuthController import AuthController

class ResultsController:
    def __init__(self, result_db: Result, auth_controller: AuthController):
        self.result_db = result_db
        self.result_db.create_connection()
        self.auth_controller = auth_controller
    def get_results(self):
        if self.auth_controller.auth_status:
            results = self.result_db.get_all_results()
            print("auth yepta")
        else:
            print("NOT auth yepta")
            latest_result = self.result_db.get_latest_result()
            results = [latest_result] if latest_result else []
        # Формируем дополнительные метрики
        for record in results:
            estimation = Estimation(
                [record['Time_1'], record['Time_2'], record['Time_3'], record['Time_4'], record['Time_5']],
                record['Num_of_errors']
            )
            record['ER'] = estimation.ER
            record['VR'] = estimation.VR
            record['PU'] = estimation.PU
        return results