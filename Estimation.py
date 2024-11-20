class Estimation:
    def __init__(self, times, num_of_errors):
        self.ER = round(self.calculate_ER(times), 2)
        self.VR = round(self.calculate_VR(times), 2)
        self.PU = round(self.calculate_PU(times), 2)
        self.num_of_errors = num_of_errors

    def calculate_ER(self, times):
        return sum(times) / len(times) if times else 0

    def calculate_VR(self, times):
        er = self.calculate_ER(times)
        return times[0] / er if er else 0

    def calculate_PU(self, times):
        er = self.calculate_ER(times)
        return times[3] / er if er else 0

    def __str__(self):
        return (f"Estimation(num_of_errors={self.num_of_errors}, "
                f"ER={self.ER:.2f}, VR={self.VR:.2f}, PU={self.PU:.2f})")

