class AdminAccount:
    def __init__(self, password):
        self.__password = password

    def get_password(self):
        return self.__password


admin_account = AdminAccount('12345')
