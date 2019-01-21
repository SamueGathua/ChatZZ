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
    
    def fetch_comment(self, id_):
        if comments:
            for index, comment in enumerate(comments):
                if comment['id'] == id_:
                    return index, comment
        return None

    def get_user(self, id_):
        for user in users:
            if id_ == user['id']:
                return user
        return None

comments =[]
users = [
    {
        'id': 1,
        'name': 'Maggy',
        'role': 'user'
    },
    {
        'id': 2,
        'name': 'Philip',
        'role': 'moderator'
    },
    {
        'id': 3,
        'name': 'Sam',
        'role': 'admin'
    }
]
