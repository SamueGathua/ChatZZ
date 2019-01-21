from users import Users, comments, users

class NormalUser(Users):
    '''A normal user class'''

    def __init__(self):
        self.user_obj = Users("user")
        self.user_id = 1
    
    def create_comment(self, comment: str):
        '''create a comment'''
        id_ = len(comments)+1

        comment_dict = {
            'id': id_,
            'userid': 1,
            'comment': comment
        }
        comments.append(comment_dict)
        return comment_dict