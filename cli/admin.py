from users import Users, comments

class Admin(Users):
    """ Admin class"""
    def __init__(self):
        self.user = Users('Admin')

    def edit(self, id, comment_str):
        """ Admin can edit any comment"""
        index, comment = self.user.fetch_comment(id)
        if comment:
            comment['body'] = comment_str
            return ("comment updated successfully %s", comment)
        else:
            return ("Comment not found %d", 404)

    def delete(self, id):
        """ Admin can delete any comment"""
        index, comment = self.user.fetch_comment(id)
        if comment:
            del comments[index]
            return "item deleted successfully"
        else:
            return "item not found"
