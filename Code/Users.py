# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:05:17 2018

@author: shimaa
"""
import Person as person
import Post as post
from enum import Enum
import matplotlib.pyplot as plt
import networkx as nx


class relation(Enum):
    Friend = 0
    Sibling = 1
    Parent = 2
    Child = 3
    Relative = 4

class Users(person.Person):
    # ** Data ** #
    numUsers = 0  # Actual number of users in the site
    maxUsers = 0  # Max number of users in the site we can deal with
    num_posts = 0  # Actual number of posts in the graph
    Users = [0 for x in range(maxUsers)]  # all users
    edges = [[0 for x in range(maxUsers)] for y in range(maxUsers)] # all connection between users
    marks = [0 for x in range(maxUsers)]  # mark user when search about special one
    Posts = []  # array of post
    Groups = []  # array of groups

    # ** Constructor & Destrcutor ** #
    def __init__(self, maxUsers):  # set the value of max users
        self.maxUsers = maxUsers
        for row in range(self.maxUsers):
            self.edges.append([])
            for col in range(self.maxUsers):
                self.edges[row].append(-1)

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
        if weight is 0:
            self.edges[col][row] = relation.Friend 
            self.edges[row][col] = relation.Friend
        elif weight is 3:
            self.edges[col][row] = relation.Parent
            self.edges[row][col] = relation.Child
        elif weight is 2:
            self.edges[col][row] = relation.Child
            self.edges[row][col] = relation.Parent
        elif weight is 4:
            self.edges[col][row] = relation.Relative
            self.edges[row][col] = relation.Relative
        elif weight is 1:
            self.edges[col][row] = relation.Sibling
            self.edges[row][col] = relation.Sibling
        else:
           self.edges[col][row] = weight #for other relations

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
        self.Users[user_id].add_post_id(self.num_posts)
        self.num_posts += 1
        self.Posts.append(post)

    # post getters
    def get_text(self, post_id):
        return self.Posts[post_id].get_text()

    def post_view(self, post_id):
        return self.Posts[post_id].post_view()

    # I believe this can't be used here !
    def get_post_id(self, post_id):
        post.get_Post_id(post_id)

    def get_posts_ids(self, user_id):
        return self.Users[user_id].get_posts_ids()

    # post view for all the posts of that user >> timeline !
    def get_posts(self, user_id):
        posts_ids = self.Users[user_id].get_posts_ids()
        posts_num = posts_ids.__len__()
        if posts_num > 0:
            for i in posts_ids:
                return self.Posts[posts_ids[i]].post_view()
        else:
            return "NO posts from user", user_id

    # post setters
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

    # ** Operation on a group ** #
    def add_relation(self, sender_id, receiver_id, weight=relation.Friend):
        self.Users[sender_id].requests_sent[receiver_id] = weight   # save in sender that he/she sent
        if weight == relation.Parent:
            self.Users[receiver_id].requests_received[sender_id] = relation.Child

        elif weight == relation.Child:
            self.Users[receiver_id].requests_received[sender_id] = relation.Parent

        else:
            self.Users[receiver_id].requests_received[sender_id] = weight

    def accept_relation(self, sender_id, receiver_id):
        # check if weight is the same at both
        weight = self.Users[sender_id].requests_sent[receiver_id]   # weight by sender
        self.AddEdge(self.Users[sender_id], self.Users[receiver_id], weight)
        # we need try & except here
        del self.Users[sender_id].requests_sent[receiver_id]
        del self.Users[receiver_id].requests_received[sender_id]

    def reject_relation(self, sender_id, receiver_id):
        # we need try & except here
        del self.Users[sender_id].requests_sent[receiver_id]
        del self.Users[receiver_id].requests_received[sender_id]

    def remove_relation (self, person_one, person_two):
        self.remove_edge(self.Users[person_one], self.Users[person_two])

    def show_sent_requests(self, user_id):
        return self.Users[user_id].requests_sent

    def show_received_requests (self, user_id):
        return self.Users[user_id].requests_received

    def search_friends(self, user_id, taget_id):
        id_list = list()
        id_list = self.edges[user_id]
        return id_list.index(taget_id)

    def show_friends(self, user_id):
        # to be changed later >> when id is more complex function: id_to_index(id = user_id) & vice versa
        id_list = self.edges[user_id]
        count = 0
        friends_list =[]
        # search in adj matrix row for that user_id
        for i in id_list:
            if type(i) == relation or (type(i) == int and i >= 0):
                j = count
                friends_list.append(self.Users[j].get_info())
            count += 1
        friends_number = friends_list.__len__()
        if friends_number > 0:
            if friends_number == 1:
                #  1 friend
                print(friends_number, "friend")
                print(friends_list)
            else:
                #  2 or more friendS
                print(friends_number, "friends")
                print(friends_list)
        else:
            print("No Friends")

    def show_friends_posts (self, user_id):
        id_list = self.edges[user_id]
        count = 0
        friends_list = []
        print("Posts from user", user_id, "friends are:")
        # search in adj matrix row for that user_id
        for i in id_list:
            if type(i) == relation or (type(i) == int and i >= 0):
                j = count
                friends_list.append(self.Users[j].get_id())
            count += 1
        friends_number = friends_list.__len__()
        print("friends list:", friends_list)
        printed_posts=[]
        if friends_number > 0:
            for i in friends_list:
                print("from user: ", i)
                print(self.get_posts(i))

        else:
            print("this user has no friends")

    def show_relation_string(self, id1, id2):

        weight = self.edges[id1][id2]
        if weight is 0:
            return "Friends"
        elif weight is 3:
            return "Child"
        elif weight is 2:
            return "Parent"
        elif weight is 4:
            return "Relatives"
        elif weight is 1:
            return "Siblings"
        else:
            return weight

    def show_relation_number(self, id1, id2):
        weight = self.edges[id1][id2]
        if weight is 0 or weight is relation.Friend:
            return 0
        elif weight is 3 or weight is relation.Child:
            return 3
        elif weight is 2 or weight is relation.Parent:
            return 2
        elif weight is 4 or weight is relation.Relative:
            return 4
        elif weight is 1 or weight is relation.Sibling:
            return 1
        else:
            return weight

    def bounded_search (self):
        # Search for some one who is not my friend (by email or ID?)
        pass

    # ** Speed Access & Update Time ** #

    # ** Extract trees and graphs ** #

    # ** visualize current graph ** #

    def show_graph(self):
        G = nx.Graph()
        ids = {}
        names = {}
        for i in range(self.edges.__len__()):
            G.add_node(i)
            for j in range(self.edges.__len__()):
                G.nodes[i]['name'] = self.Users[i].name
                names[i] = self.Users[i].name
                if self.edges[i][j] != -1:
                    G.add_edge(i, j)
                    G.nodes[j]['name'] = self.Users[j].name
                    G[i][j]['w'] = self.show_relation_number(i,j)
                    '''parent and child returns 2 & 3 but graph is not directed'''

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, names)
        nx.draw_networkx_edge_labels(G, pos)
        plt.show()
        pass
