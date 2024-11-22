class Estimation:
    def __init__(self, result):
        self.__ER = round(self.calculate_ER(result.get_times()), 2)
        self.__VR = round(self.calculate_VR(result.get_times()), 2)
        self.__PU = round(self.calculate_PU(result.get_times()), 2)

    @property
    def ER(self):
        return self.__ER

    @property
    def VR(self):
        return self.__VR

    @property
    def PU(self):
        return self.__PU

    def calculate_ER(self, times):
        return sum(times) / len(times) if times else 0

    def calculate_VR(self, times):
        er = self.calculate_ER(times)
        return times[0] / er if er else 0

    def calculate_PU(self, times):
        er = self.calculate_ER(times)
        return times[3] / er if er else 0
