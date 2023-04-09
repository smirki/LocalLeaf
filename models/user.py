class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        print(f"Email: {self.email}")
