import datetime

class Users():
    def __init__(self, user_type):
        self.logged_in = False
        self.user = user_type

    def log_in(self):
        self.logged_in = True
        logged_in_at = str(datetime.datetime.now())
        return ("Logged in at %s as %s", logged_in_at, self.user)

    def log_out(self):
        self.logged_in = False
        logged_out_at = str(datetime.datetime.now())
        return ("Logged out at %s", logged_out_at)

    def create_comment(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass
