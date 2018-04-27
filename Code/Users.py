# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:05:17 2018

@author: shimaa
"""
import Person as person
import Post as post
from enum import Enum

relation = Enum('relation', 'Friend Sibling Parent Child Relative')



class Users(person.Person, post.Post):
    # ** Data ** #
    numUsers = 0  # Actual number of users in the site
    maxUsers = 0  # Max number of users in the site we can deal with
    num_posts = 0  # Actual number of posts in the graph
    Users = [0 for x in range(maxUsers)]  # all users
    edges = []  # [[0 for x in range(maxUsers)] for y in range(maxUsers)] # all connection between users
    marks = [0 for x in range(maxUsers)]  # mark user when search about special one
    Posts = []  # array of post

    # ** Constructor & Destrcutor ** #
    def __init__(self, maxUsers):  # set the value of max users
        self.maxUsers = maxUsers
        for row in range(self.maxUsers):
            self.edges.append([])
            for col in range(self.maxUsers):
                self.edges[row].append(0)

    def __del__(self):  # nothing to do
        print("users: ", self.Users)

    # ** Graph functionality ** #
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
        if weight == relation.Parent:
            self.edges[col][row] = relation.Child

        elif weight == relation.Child:
            self.edges[col][row] = relation.Parent

        else:
            self.edges[col][row] = weight
        """Not working for child & parent"""

    def remove_edge(self, from_person, to_person): # remove connection between two users
        row = self.IndexIs(from_person)
        col = self.IndexIs(to_person)
        self.edges[row][col] = 0
        self.edges[col][row] = 0

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

    # **post** #
    def add_post(self, post, user_id):
        self.num_posts += 1
        self.Posts.append(post)
        self.Users[user_id].add_post_id(self.num_posts)

    # ** post getters ** #
    def get_text(self, post_id):
        return self.Posts[post_id].get_text()

    def post_view(self, post_id):
        return self.Posts[post_id].post_view()

    # I believe this can't be used here !
    def get_post_id(self, post_id):
        post.get_Post_id(post_id)
        pass

    def get_posts_ids(self, user_id):
        return self.Users[user_id].get_posts_ids()

    # post view for all the posts of that user >> timeline !
    def get_posts(self, user_id):
        posts_ids = self.Users[user_id].get_posts_ids()
        for i in range(posts_ids):
            return self.Posts[posts_ids[i]].Post_view()

    # ** post setters ** #
    def set_post_id(self, post_id):
        post.set_Post_id(post_id)

    def get_user_id(self, post_id):
        post.get_user_id(post_id)

    def edit_post(self, post_id, text):
        self.Posts[post_id].edit(text)

    # comment
    def add_comment (self,text ,post_id, user_id):
        self.Posts[post_id].add_comment(text, user_id)

    def edit_comment (self, text, post_id, comment_id):
        self.Posts[post_id].edit_comment(text, comment_id)

    def delete_comment (self, post_id, comment_id):
        self.Posts[post_id].delete_comment(comment_id)

    def get_comments_num(self, post_id):
        self.Posts[post_id].get_comments_num()

    # Operation on a group
    def add_relation(self, sender_id, receiver_id, weight=relation.Friend):
        self.Users[sender_id].requests_sent[receiver_id] = weight   # save in sender that he/she sent
        if weight == relation.Parent:
            self.Users[receiver_id].requests_received[sender_id] = relation.Child

        elif weight == relation.Child:
            self.Users[receiver_id].requests_received[sender_id] = relation.Parent

        else:
            self.Users[receiver_id].requests_received[sender_id] = weight
        pass

    def accept_relation(self, sender_id, receiver_id):
        # check if weight is the same at both
        weight = self.Users[sender_id].requests_sent[receiver_id]   # weight by sender
        self.AddEdge(self.Users[sender_id], self.Users[receiver_id], weight)
        # we need try & except here
        del self.Users[sender_id].requests_sent[receiver_id]
        del self.Users[receiver_id].requests_received[sender_id]
        pass

    def reject_relation(self, sender_id, receiver_id):
        # we need try & except here
        del self.Users[sender_id].requests_sent[receiver_id]
        del self.Users[receiver_id].requests_received[sender_id]
        pass

    def remove_relation (self, person_one, person_two):
        self.remove_edge(self.Users[person_one], self.Users[person_two])
        pass

    def search_friends (self):
        pass

    def show_friends (self):
        pass

    def show_friends_posts (self):
        pass

    def bounded_search (self):
        # Search for some one who is not my friend (by email or ID?)
        pass
