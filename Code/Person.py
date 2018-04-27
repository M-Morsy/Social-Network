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
    def __init__(self, name, email, password, age=None, location=None, gender=None):
        Person.Count += 1
        self.ID = self.Count
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.location = location
        self.gender = gender
        self.groups = []
        self.posts = []
        self.admin = []
        self.requests_sent = {}
        self.requests_received = {}

    def __del__(self):
        print("person: ", self.name, "with ID: ", self.ID, "died")

    # ** Getters and Setters **##

    def get_id(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

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

    # ** setters **#
    def set_id(self, ID):
        self.ID = ID
        # self.dict['ID'].append(ID)

    def set_name(self, name):
        self.name = name
        # self.dict['Name'].append(name)

    def set_email(self, email):
        self.email = email
        # self.dict['Email'].append(email)

    def set_password(self, password):
        self.password = password
        # self.dict['Password'].append(password)

    # ** adding **##
    def add_post_id(self, post_id):
        self.posts.append(post_id)

    def add_group_id(self, group_id):
        self.groups.append(group_id)

    def add_admin_group(self, group_id):
        self.admin.append(group_id)

    def add_friend_request(self, user_id, weight):
        self.requests_received[user_id] = weight

    # when a user is declared Admin, he will be declared here and in groups class or its equivilant  

    # ** removing **##
    ''' TBD: search for try and catch in the index method '''
    def remove_post(self, post_id):
        self.posts.remove(post_id)

    def remove_group(self, group_id):
        self.groups.remove(group_id)

    def remove_admin_group(self, group_id):
        self.Admin.remove(group_id)



