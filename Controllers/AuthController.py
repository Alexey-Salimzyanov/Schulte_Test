class AuthController:
    def __init__(self, admin_account):
        self.__admin_account = admin_account
        self.__auth_status = False

    def authenticate(self, password):
        if self.__admin_account.get_password() == password:
            self.__auth_status = True
            return True
        else:
            return False

    def logout(self):
        self.__auth_status = False

    def get_auth_status(self):
        return self.__auth_status
