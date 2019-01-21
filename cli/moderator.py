from users import Users, comments, users

class ModerateUser(Users):
    '''A Moderate user class'''

    def __init__(self):
        self.user_obj = Users("user")
        self.user_id = 2


    def edit_comment(self,id) :
        '''Edits their own comments'''
        index,edit_item = fetch_comment()
        if edit_item and userid == self.user_id:
            comments.insert([index,edit_item])
            print("Comment successfully edited")
        else:
            print("Comment not found")
