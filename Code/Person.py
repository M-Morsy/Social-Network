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
    Posts = []   # Posts'  IDs >> Linked list >> To Be Done
    Groups = []  # groups' IDs >> Linked list >> To Be Done
    Admin = []   # groups' IDs >> Linked list >> To Be Done
    next = None
    Count = 0
    
    # ** Constructor & Destructor **##
    def __init__(self, name, email, password):
        Person.Count += 1
        self.ID = self.Count
        self.name = name
        self.email = email
        self.password = password
        # self.dict['ID'].append(self.Count)  # To be replaced by random ID
        # self.dict['Name'].append(name)
        # self.dict['Email'].append(email)
        # self.dict['Password'].append(password)

    def __del__(self):
        print ("person: ", self.name, "with ID: ", self.ID, "died")
    # ** Getters and Setters **##

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
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

    def set_password (self, password):
        self.password = password
        # self.dict['Password'].append(password)

    # ** getters and setters for whole information **##
    def get_info(self):
        return [self.ID, self.name, self.email , self.password]

    def set_info(self, ID=None, name=None, email=None, password=None):
        if ID is None:
            pass
        else:
            self.set_ID(ID)
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
    def add_post(self, post_ID):
        self.Posts.append(post_ID)

    def add_group (self, group_ID):
        self.Groups.append(group_ID)

    def add_admin_group (self, group_ID):
        self.Admin.append(group_ID)
        
    # when a user is declared Admin, he will be declared here and in groups class or its equivilant  
    
    # ** removing **##
    def remove_post (self , post_ID):
        if (self.Posts.index(post_ID)):
            self.Posts.remove(post_ID)
        else:
            print ("error")  # TBR

    def remove_group (self, group_ID):
        if (self.Groups.index(group_ID)):
            self.Groups.remove(group_ID)
        else:
            print ("error")  # TBR

    def remove_admin_group (self, group_ID):
        if (self.Admin.index(group_ID)):
            self.Admin.remove(group_ID)
        else:
            print ("error")  # TBR




