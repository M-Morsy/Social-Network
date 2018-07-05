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
import hashing as hashing
import numpy as np
import Group as group

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
    edges = [[] for y in range(maxUsers)] # all connection between users
    marks = [0 for x in range(maxUsers)]  # mark user when search about special one
    Posts = []  # array of post
    Groups = []  # array of groups

    # ** Constructor & Destrcutor ** #
    def __init__(self, maxUsers):  # set the value of max users
        self.maxUsers = maxUsers
        for row in range(self.maxUsers):
            self.edges.append([])

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
        if person.age != None:
           ageRange = hashing.ageHashFunc(person.age)
           hashing.ageTable[ageRange].insert(person.get_age(),person.get_id())
        if person.name != None:
            nameRange = hashing.nameHashFunc(person.name)
            hashing.nameTable[nameRange].insert(person.get_name(), person.get_id())
        if person.location != None:
             countryRange = hashing.nameHashFunc(person.location)
             hashing.countryTable[countryRange].insert(person.get_location(), person.get_id())
        self.numUsers += 1
        if self.numUsers > self.maxUsers:
            self.edges.append([])
            self.maxUsers += 1

    def AddEdge(self, fromPesron, toPerson, weight):  # add new connection
        fromUser = self.IndexIs(fromPesron)
        toUser = self.IndexIs(toPerson)
        self.edges[fromUser].append([toUser, weight])

        if weight is 3 :  #if from parent to child
            self.edges[toUser].append([fromUser, 2])

        elif weight is 2 : #if from child to parent
            self.edges[toUser].append([fromUser, 3])
            
        else:           
            self.edges[toUser].append([fromUser, weight]) #for other relations

    def remove_edge(self, from_person, to_person): # remove connection between two users
        fromUser = self.IndexIs(from_person)
        toUser = self.IndexIs(to_person)
        for i in self.edges[fromUser]:
            if i[0] == toUser:
                self.edges[fromUser].remove(i)
        for i in self.edges[toUser]:
            if i[0] == fromUser:
                self.edges[toUser].remove(i)

    def WeightIs(self, fromPesron, toPerson):  # add weight between two users
        fromUser = self.IndexIs(fromPesron)
        toUser = self.IndexIs(toPerson)
        for i in self.edges[fromUser]:
            if i[0] == toUser:
                return i[1]
        return -1

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

    # ** searching algorithm ** #
    def search_by_age(self,age):
      key = hashing.ageHashFunc()
      self.ageTable[key]


    # **post** #
    def add_post(self, post, user_id):
        self.Users[user_id].add_post_id(self.num_posts)
        self.Posts.append(post)
        self.num_posts += 1

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

    def get_posts(self, user_id):
        print(user_id)
        posts_ids = self.Users[user_id].get_posts_ids()
        posts_num = posts_ids.__len__()
        if posts_num > 0:
            for i in posts_ids:
                print("post id[", i, "] for user:", user_id)
                self.Posts[i].post_view()
        else:
            return "NO posts from user", user_id

    def get_friends_posts (self, user_id):
        friends_ids = {}
        for i in self.edges[user_id]:
            self.get_posts(i[0])
        pass

    # post view for all the posts of that user >> timeline !
    def show_all_posts(self):
        print("numUsers", self.numUsers)
        for i in range(self.numUsers):
            self.get_posts(i)

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
    def add_relation(self, sender_id, receiver_id, weight=0):
        self.Users[sender_id].requests_sent[receiver_id] = weight   # save in sender that he/she sent
        if weight == 2: #from parent to child
            self.Users[receiver_id].requests_received[sender_id] = 3

        elif weight == 3: #from child to parent
            self.Users[receiver_id].requests_received[sender_id] = 2

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

    def search_friends(self, user_id, target_id):
        id_list = list()
        id_list = self.edges[user_id]
        return id_list.index(target_id)

    def show_friends(self, user_id):
        # to be changed later >> when id is more complex function: id_to_index(id = user_id) & vice versa
        id_list = self.edges[user_id]
        friends_list =[]
        # search in adj matrix row for that user_id
        for i in id_list:
            j = i[0]
            friends_list.append(self.Users[j].get_info())
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
        friends_list = []
        print("Posts from user", user_id, "friends are:")
        # search in adj matrix row for that user_id
        for i in id_list:
            j = i[0]
            friends_list.append(self.Users[j].get_id())
        friends_number = friends_list.__len__()
        print("friends list:", friends_list)
        if friends_number > 0:
            for i in friends_list:
                print("from user: ", i)
                print(self.get_posts(i))

        else:
            print("this user has no friends")

    def show_relation_string(self, id1, id2):

        weight = -1 
        for i in self.edges[id1]:
            if i[0] == id2:
                weight = i[1]
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
            return "No relation"

    def show_relation_number(self, id1, id2):
        for i in self.edges[id1]:
            if i[0] == id2:
                return i[1]
        return -1
    # ** Group ** #
    def add_group(self,admin_id, group_name,description = None):
        self.Groups.append(group.__init__(admin_id,group_name,description))
    def remove_group(self,group_id):
        for group in self.Groups:
            if group.group_id == group_id:
                self.Groups.remove(group)
    def add_post_in_group(self,group_id, post_id):
        for group in self.Groups:
            if group.group_id == group_id:
                group.add_post(post_id)
    def remove_post_from_group(self,group_id, post_id):
        for group in self.Groups:
            if group.group_id == group_id:
                group.remove_post(post_id)
    def add_member_in_group(self,group_id, person_id):
        for group in self.Groups:
            if group.group_id == group_id:
                group.add_member(person_id)
    def remove_member_from_group(self,group_id, person_id):
        for group in self.Groups:
            if group.group_id == group_id:
                group.remove_member(person_id)
    def add_admin_to_group(self, group_id, admin_id):
        for group in self.Groups:
            if group.group_id == group_id:
                group.add_admin(admin_id)
    def remove_admin_from_group(self, group_id, admin_id):
        for group in self.Groups:
            if group.group_id == group_id:
                group.remove_admin(admin_id)
    def update_group_info(self, group_id, admin_id = None, group_name = None, description = None):
        for group in self.Groups:
            if group.group_id == group_id:
                group.set_info(admin_id,group_name,description)


    # ** Visualization ** #
    
    def post_chart(self):
        fig, ax = plt.subplots()
        users = []
        posts_num = []
        for i in self.Users:
            if len(i.posts) > 0:
                users.append(i.ID)
                posts_num.append(len(i.posts))
        y_pos = np.arange(len(users))
        plt.bar(y_pos, posts_num, align='center', alpha=0.5)
        plt.xticks(y_pos, users)
        plt.ylabel('Number of posts')
        plt.title('Users activity')
        plt.show()
        
    def comment_chart(self):
        fig, ax = plt.subplots()
        users = []
        comments_num = []
        for i in self.Users:
            users.append(i.ID)
            comments_num.append(0)
            for p in self.Posts:
                for c in p.Comments:
                    if c.user_id == i.ID:
                        comments_num[-1] += 1
            if comments_num[-1] == 0:
                users.pop()
                comments_num.pop()
                
        y_pos = np.arange(len(users))
        plt.bar(y_pos, comments_num, align='center', alpha=0.5)
        plt.xticks(y_pos, users)
        plt.ylabel('Number of comments')
        plt.title('Users activity')
        plt.show()

    def show_graph(self, with_edges=False):
        g = nx.Graph()
        names = {}
        for i in range(self.numUsers):
            g.add_node(i)
            names[i] = self.Users[i].name
            for k in self.edges[i]:
                j = k[0]
                g.nodes[i]['name'] = self.Users[i].name

                g.add_edge(i, j)
                g.nodes[j]['name'] = self.Users[j].name
                g[i][j]['w'] = self.show_relation_number(i,j)
                '''parent and child returns 2 & 3 but graph is not directed'''

        pos = nx.spring_layout(g)
        #nx.draw_networkx_nodes(g, pos)
        Max = list(g.degree)[0]
        for i in g.degree:
            if i[1] > Max[1] :
                Max= i
        for i in g.degree:
            if i == Max:
                nx.draw_networkx_nodes(g, pos, nodelist= [i[0]], node_size=i[1]*200, node_color= 'b')
            else: nx.draw_networkx_nodes(g, pos, nodelist= [i[0]], node_size=50+i[1]*100)
        nx.draw_networkx_edges(g, pos)
        nx.draw_networkx_labels(g, pos, names)
        if with_edges:
            nx.draw_networkx_edge_labels(g, pos)
        plt.show()
        print(names)
        pass


    def is_sub_list(self, g, l):
        return all(True if x in g else False for x in l)

    def show_partial_graph(self, id_list):
        g = nx.Graph()
        names = {}
        for i in range(self.edges.__len__()):
            g.add_node(i)
            for j in range(self.edges.__len__()):
                g.nodes[i]['name'] = self.Users[i].name
                names[i] = self.Users[i].name
                if self.edges[i][j] != -1:
                    g.add_edge(i, j)
                    g.nodes[j]['name'] = self.Users[j].name
                    g[i][j]['w'] = self.show_relation_number(i, j)
                    

        path_list = [p for p in nx.shortest_path(g, source=id_list[0])]  # Target not specified
        l = id_list[1:]
        res = [x for x in path_list if self.is_sub_list(x, l)]
        return res
        # show the graph
        g = nx.Graph()
        pos = nx.spring_layout(g)
        nx.draw_networkx_nodes(g, pos)
        nx.draw_networkx_edges(g, pos)
        nx.draw_networkx_labels(g, pos, names)
        nx.draw_networkx_edge_labels(g, pos)
        plt.show()
        pass
