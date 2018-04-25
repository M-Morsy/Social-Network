# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:05:17 2018

@author: shimaa
"""
import Person as person
import Post as post


class Users(person.Person):
    # ** Data **##
    numUsers = 0  # Actual number of users in the site
    maxUsers = 0  # Max number of users in the site we can deal with
    Users = [0 for x in range(maxUsers)]  # all users
    edges = []  # [[0 for x in range(maxUsers)] for y in range(maxUsers)] # all connection between users
    marks = [0 for x in range(maxUsers)]  # mark user when search about special one

    ##** Constructor & Destrcutor **##
    def __init__(self, maxUsers):  # set the value of max users
        self.maxUsers = maxUsers
        for row in range(self.maxUsers):
            self.edges.append([])
            for col in range(self.maxUsers):
                self.edges[row].append(0)

    def __del__(self):  # nothing to do
        print("users: ", self.Users)

    ##** Graph functionality **##
    def MakeEmpty(self):  # delete every thing
        self.numUsers = 0
        self.maxUsers = 0
        del self.Users
        del self.edges
        del self.marks

    def IsEmpty(self):  # return true if no users
        if self.numUsers == 0:
            return bool(1)
        return bool(0)

    def IsFull(self):  # return true if limit of users is full
        if self.numUsers == self.maxUsers:
            return bool(1)
        return bool(0)

    def IndexIs(self, person):  # return index of special user
        i = 0
        for user in self.Users:
            if user == person:
                return i
            i += 1
        return

    def AddUser(self, person):  # add new user
        self.Users.append(person)
        self.marks.append(0)
        self.numUsers += 1

    def AddEdge(self, fromPesron, toPerson, weight):  # add new connection
        row = self.IndexIs(fromPesron)
        col = self.IndexIs(toPerson)
        self.edges[row][col] = weight

    def WeightIs(self, fromPesron, toPerson):  # add weight between two users
        row = self.IndexIs(fromPesron)
        col = self.IndexIs(toPerson)
        return self.edges[row][col]

    def GetToUsers(self, pesron):  # for searching algorithm
        print("nothing")

    def ClearMarks(self):  # delete all marks
        for i in range(self.numUsers):
            self.marks[i] = 0

    def MarkUser(self, pesron):  # mark user to ignore it in searching
        index = self.IndexIs(pesron)
        self.marks[index] = 1

    def IsMarked(self, pesron):  # is user marked?
        index = self.IndexIs(pesron)
        return bool(self.marks[index])

    # searching algorithm
    def DepthFirstSearch(self, startUser, endUser):
        print("nothing")

    def BreadthFirtsSearch(self, startUser, endUser):
        print("nothing")

    # more on users
    # I believe this can't be used here !
    def get_post_id (self):
        pass

    # **post** #
    def add_post(self, text):
        # first problem
        user_id = 0
        post.Post(text, user_id)
        pass

    def get_text(self, post_id):
        pass

    def edit_post(self, post_id):
        pass

    def post_view(self, post_id):
        pass

    # I believe this can't be used here !
    def get_post_id(self):
        pass

    def set_post_id(self, post_id):
        post.set_Post_ID(post_id)

    def get_user_id(self, post_id):
        pass

    # comment
    def add_comment (self, post_id):
        pass

    def edit_comment (self, post_id, comment_id):
        pass

    def delete_comment (self, post_id, comment_id):
        pass

    def get_comments_num (self, post_id):
        pass

