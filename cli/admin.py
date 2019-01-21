from users import Users

class Admin(Users):
    """ Admin class"""
    def __init__(self):
        self.user = Users('Admin')

    def edit(self, id, comment_str):
        """ Admin can edit any comment"""
        comment = self.user.fetch_comment(id)
        if comment:
            comment['body'] = comment_str
            print("comment updated successfully %s", comment)
        else:
            print("Comment not found %d", 404)
