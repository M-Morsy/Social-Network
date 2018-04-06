class person ():
    #** Data **##
    dict = {
                "ID"       : [], # generated
                "Name"     : [], # Just user name not sir name
                "Email"    : [], # Normal Email
                "Password" : [] # four digits password = 10^4 users    
            }
    Posts  = [] # Posts'  IDs >> Linked list >> To Be Done
    Groups = [] # groups' IDs >> Linked list >> To Be Done
    Admin  = [] # groups' IDs >> Linked list >> To Be Done
    next = None
    Count = 0
    
    ##** Constructor & Destrcutor **##
    def __init__(self, Name , Email , Password):
        self.dict['ID']       = 0 + Count # To be replaced by random ID
        self.dict['Name']     = Name
        self.dict['Email']    = Email
        self.dict['Password'] = Password
        Count += 1

    def __del__(self):
        print ("person: " , self.dict['Name'] , "with ID: ", self.dict['ID'] , "died")
    ##** Getters and Setters **##
    def get_ID (self):
        return self.dict['ID']
    def set_ID (self , ID):
        self.dict['ID'] = ID   
    def get_Name (self):
        return self.dict['Name']
    def get_Name (self , Name):
        self.dict['Name'] = Name   
    def get_Email (self):
        return self.dict['Email']
    def set_Email (self , Email):
        self.dict['Email'] = Email
    def get_Password (self):
        return self.dict['Password']
    def get_Password (self , Password):
        self.dict['Password'] = Password
    ##** getters and setters for whole information **##
    def get_info (self):
        return [self.dict['ID'] , self.dict['Name'] , self.dict['Email'] , self.dict['Password']]
    def set_info (self , ID = None , Name = None , Email = None , Password = None):
        if ID is None:
            pass
        else:
            self.dict['ID'] = ID
        if Name is None: 
            pass
        else:
            self.dict['Name'] = Name
        if Email is None:
            pass
        else:
            self.dict['Email'] = Email
        if Password is None:
            pass
        else:
            self.dict['Password'] = Password   
    
    ##** adding **##
    def add_post (self , Post_ID):
        self.Posts.append(Post_ID)
    def add_Group (self , Group_ID):
        self.Groups.append(Group_ID)
    def Add_Admin_Group (self , Group_ID):
        self.Admin.append(Group_ID)
        
    # when a user is declared Admin, he will be declared here and in groups class or its equivilant  
    
    ##** removing **##
    def remove_post (self , Post_ID):
        if (self.Posts.index(Post_ID)):
            self.Posts.remove(Post_ID)
        else:
            print ("error") # TBR
    def remove_Group (self , Group_ID):
        if (self.Groups.index(Group_ID)):
            self.Groups.remove(Group_ID)
        else:
            print ("error") # TBR
    def remove_Admin_Group (self , Group_ID):
        if (self.Admin.index(Group_ID)):
            self.Admin.remove(Group_ID)
        else:
            print ("error") # TBR
