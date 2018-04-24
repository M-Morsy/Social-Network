# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:40:59 2018

@author: maged
"""
import json

def dfs (mylist, data, start = 0):
    marked = [False for i in range (len(mylist))]
    dfs_in(mylist, marked, start, data)
    
    
def dfs_in (mylist, marked, start, data):
    index = start.IndexIs
    #PRE
    data["users"].append({"name":start.get_name(),"Email":start.get_Email(), 
        "password":start.get_password(), "ID":start.get_ID(),
        "friends":mylist[index], "posts":[]})
    num = len(data["users"])
    for post in start.posts:
        data["users"][num-1]["posts"].append({"text":post.text, "comments":[]})
        num1 = len(data["users"][num-1]["posts"])
        for comment in post.comments:
            data["users"][num-1]["posts"][num1-1]["comments"].append({"text":comment.text, "user_ID":comment.user_ID})
    #SEARCH
    marked[index] = True
    for x in mylist[index]:
        if marked[x.IndexIs] == False:
            dfs_in(mylist, marked, x)
    #POST
            
            
            
def save(graph) :
    data = {}
    data["max_users"] = graph.getMaxUsers()
    data["users"] = []
    dfs(graph.edges, data)
    with open('users_data.json', 'w') as f:
        json.dump(data, f)
    
