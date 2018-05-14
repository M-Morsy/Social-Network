import hashing as hashing

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
        Person.Count += 1

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

    def get_age(self):
        return self.age

    def get_location(self):
        return self.location

    def get_gender(self):
        return self.gender

    def get_posts_ids(self):
        return self.posts

    def get_groups_ids (self):
        return self.groups

    def get_admin_groups (self):
        return self.admin
    # ** getters and setters for person's whole information **##

    def get_info(self):
        return self.__dict__

    # ** setters for persons information **#
    def set_id(self, ID):
        self.ID = ID

    def set_name(self, name):
        oldName = hashing.nameHashFunc(self.name)
        hashing.nameTable[oldName].delete(self.get_id())
        self.name = name
        newName = hashing.nameHashFunc(self.name)
        hashing.nameTable[newName].insert(self.name,self.get_id())

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def set_age(self, age):
        oldAge = hashing.ageHashFunc(self.age)
        hashing.ageTable[oldAge].delete(self.get_id())
        self.age = age
        newAge = hashing.ageHashFunc(self.age)
        hashing.ageTable[newAge].insert(self.age,self.get_id())

    def set_location(self, location):
        oldLocation = hashing.nameHashFunc(self.location)
        hashing.countryTable[oldLocation].delete(self.get_id())
        self.location = location
        newLocation = hashing.nameHashFunc(self.location)
        hashing.countryTable[newLocation].insert(self.location,self.get_id())

    def set_gender(self, gender):
        self.gender = gender

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

    # ** adding posts or groups **##
    def add_post_id(self, post_id):
        self.posts.append(post_id)

    def add_group_id(self, group_id):
        self.groups.append(group_id)

    def add_admin_group(self, group_id):
        self.admin.append(group_id)

    def add_friend_request(self, user_id, weight):
        self.requests_received[user_id] = weight

    # when a user is declared Admin, he will be declared here and in groups class or its equivilant  

    # ** removing posts or groups **##
    def remove_post(self, post_id):
        self.posts.remove(post_id)

    def remove_group(self, group_id):
        self.groups.remove(group_id)

    def remove_admin_group(self, group_id):
        self.Admin.remove(group_id)



