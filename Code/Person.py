class Person:
    # ** Data ** ##
    """
    dict = {
                "ID": [],  # generated
                "Name": [],  # Just user name not sir name
                "Email": [],  # Normal Email
                "Password": []  # four digits password = 10^4 users
            }
    """
    next = None
    Count = 0

    # ** Constructor & Destructor **##
    def __init__(self, name, email, password):
        Person.Count += 1
        self.ID = self.Count
        self.name = name
        self.email = email
        self.password = password
        self.groups = []
        self.posts = []
        self.admin = []
        # self.dict['ID'].append(self.Count)  # To be replaced by random ID
        # self.dict['Name'].append(name)
        # self.dict['Email'].append(email)
        # self.dict['Password'].append(password)

    def __del__(self):
        print("person: ", self.name, "with ID: ", self.ID, "died")

    # ** Getters and Setters **##

    def get_id(self):
        return self.ID

    def set_id(self, ID):
        self.ID = ID
        # self.dict['ID'].append(ID)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        # self.dict['Name'].append(name)

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
        # self.dict['Email'].append(email)

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
        # self.dict['Password'].append(password)

    def get_posts_ids (self):
        return self.posts

    def get_groups_ids (self):
        return self.groups

    def get_admin_groups (self):
        return self.admin
    # ** getters and setters for whole information **##

    def get_info(self):
        return self.__dict__

    def set_info(self, id=None, name=None, email=None, password=None):
        if id is None:
            pass
        else:
            self.set_id(id)
        if name is None:
            pass
        else:
            self.set_name(name)
        if email is None:
            pass
        else:
            self.set_email(email)
        if password is None:
            pass
        else:
            self.set_password(password)

    # ** adding **##
    def add_post_id(self, post_id):
        self.posts.append(post_id)

    def add_group_id(self, group_id):
        self.groups.append(group_id)

    def add_admin_group(self, group_id):
        self.admin.append(group_id)

    # when a user is declared Admin, he will be declared here and in groups class or its equivilant  

    # ** removing **##
    ''' TBD: search for try and catch in the index method '''
    def remove_post(self, post_id):
        self.posts.remove(post_id)

    def remove_group(self, group_id):
        self.groups.remove(group_id)

    def remove_admin_group(self, group_id):
        self.Admin.remove(group_id)



