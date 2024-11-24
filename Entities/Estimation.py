class Estimation:
    def __init__(self, result):
        self.__ER = round(self._calculate_ER(result.get_times()), 2)
        self.__VR = round(self._calculate_VR(result.get_times()), 2)
        self.__PU = round(self._calculate_PU(result.get_times()), 2)

    @property
    def ER(self):
        return self.__ER

    @property
    def VR(self):
        return self.__VR

    @property
    def PU(self):
        return self.__PU

    def _calculate_ER(self, times):
        return sum(times) / len(times) if times else 0

    def _calculate_VR(self, times):
        er = self._calculate_ER(times)
        return times[0] / er if er else 0

    def _calculate_PU(self, times):
        er = self._calculate_ER(times)
        return times[3] / er if er else 0
