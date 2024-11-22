class AuthController:
    def __init__(self, admin_account):
        self._admin_account = admin_account
        self.auth_status = False

    def authenticate(self, password):
        if self._admin_account.get_password() == password:
            self.auth_status = True
            return True
        else:
            return False

    def logout(self):
        self.auth_status = False
