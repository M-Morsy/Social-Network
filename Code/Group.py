# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:46:32 2018

@author: 14E0071
"""

class Group:
    group_count = 0
    
    # ** Constructor & Destructor **##
    def __init__(self, admin, name, description = None):
        self.admin_id = []
        self.admin_id.append(admin)
        self.group_id = self.group_count
        self.group_name = name
        self.group_description = description
        self.group_members = []
        self.group_posts = []
        self.group_count += 1

    def __del__(self):
        print("group: ", self.group_name, "with ID: ", self.group_id, "died")


    # ** Getters and Setters **##

    def get_group_id(self):
        return self.group_id

    def get_group_name(self):
        return self.group_name

    def get_admin_id(self):
        return self.admin_id

    def get_group_description(self):
        return self.group_description

    def get_group_posts(self):
        return self.group_posts

    def get_group_count(self):
        return self.group_count
    
    def get_group_members(self):
        return self.group_members
    
    def get_info(self):
        return self.__dict__
    def get_groups_number(self):
        return self.group_count

    def set_info(self, admin=None, name=None, description=None):
        if admin is None:
            pass
        else:
            self.admin_id = admin
        if name is None:
            pass
        else:
            self.group_name = name
        if description is None:
            pass
        else:
            self.description = description

    def set_group_id(self,id):
         self.group_id = id

    def set_group_name(self, name):
         self.group_name = name

    def set_group_description(self, description):
         self.group_description = description

    def set_group_count(self, num):
         self.group_count = num
    
    # ** adding **##
    def add_post(self, post_id):
        self.group_posts.append(post_id)

    def add_admin(self, id):
        self.admin_id.append(id)

    def add_member(self, person_id):
        self.group_members.append(person_id)

    # ** removing **##
    def remove_post(self, post_id):
        self.group_posts.remove(post_id)

    def remove_admin(self, admin_id):
        self.admin_id.remove(admin_id)
        
    def remove_member(self, person_id):
        self.group_members.remove(person_id)