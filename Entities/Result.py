class Result:
    def __init__(self, id: int, times: list, num_of_errors: int):
        self.__id = id
        self.__times = [round(time, 2) for time in times]
        self.__num_of_errors = num_of_errors

    def get_id(self):
        return self.__id
    def get_times(self):
        return self.__times

    def get_num_of_errors(self):
        return self.__num_of_errors

    def set_id(self, id: int):
        self.__id = id

    def set_times(self, times: list):
        self.__times = [round(time, 2) for time in times]

    def set_num_of_errors(self, num_of_errors: int):
        self.__num_of_errors = num_of_errors


