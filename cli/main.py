from normaluser import NormalUser
from moderator import ModerateUser
def main():
    """Added Bundler"""
    print("\t=====Welcome to Chazz======")
    print("""\n
            Choose a role:
            1: Normal User
            2: Moderator User
            3: Admin
        """)
    choose_id =input("\n\n Please Select A user to login: ")

    if choose_id == 1:
        normalusr_obj = NormalUser()
        # login user
        print(normalusr_obj.user_obj.log_in())
        comment = input("\n Create a comment: ")
        print(normalusr_obj.create_comment(comment))
        print("\n Edit comment: ")
        comment_id = input("\n Comment id: ")
        comment_update = input("\n Comment body: ")
        comment_update = str(comment_update)
        print(normalusr_obj.edit(comment_id,comment_update))
        print("\n\n User log out")
        print(normalusr_obj.user_obj.log_out())
        
    if choose_id == 2:
        # login moderate user
        moderateusr_obj = ModerateUser()
        print(moderateusr_obj.user_obj.log_in())
        comment = input("\n Create a comment: ")
        print(moderateusr_obj.create_comment(comment))
        print("\n Edit comment: ")
        comment_id = input("\n Comment id: ")
        comment_update = input("\n Comment body: ")
        comment_update = str(comment_update)
        print(moderateusr_obj.edit(comment_id,comment_update))
        print("\n\n User log out")
        print(moderateusr_obj.log_out())

if __name__ == "__main__":
    main()
