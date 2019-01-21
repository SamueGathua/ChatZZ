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

    def edit(self, comment_id, comment_update):
        '''edit comment'''
        # fetch comment
        user_obj = self.get_user(self.user_id)
        if self.user_id == comment_update['userid'] and user_obj['role'] == self.user_obj.user:
            index, comment = self.user.fetch_comment(comment_id)
            if comment:
                comment = comment_update
                comments[index] = comment
                return "Comment edited to {}".format(comment['comment'])
        return None