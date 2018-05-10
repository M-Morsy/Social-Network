# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:40:59 2018

@author: maged
"""
import json

'''def dfs (mylist, data, users, start = 0):
    marked = [False for i in range (len(mylist))]
    dfs_in(mylist, marked, start, users, data)
    
    
def dfs_in (mylist, marked, start, users, data):
    index = start.IndexIs
    #PRE
    data["users"].append({"name":users[start].get_name(),"Email":users[start].get_Email(), 
        "password":users[start].get_password(), "ID":users[start].get_ID(),
        "friends":mylist[start], "posts":[]})
    for post in users[start].posts:
        data["users"][-1]["posts"].append({"text":post.text, "comments":[]})
        for comment in post.comments:
            data["users"][-1]["posts"][-1]["comments"].append({"text":comment.text, "user_ID":comment.user_ID})
    #SEARCH
    marked[index] = True
    for x in mylist[index]:
        if marked[x.IndexIs] == False:
            dfs_in(mylist, marked, x)
    #POST'''
            
            
            
def save(graph) :
    data = {}
    data["numUsers"]= graph.numUsers 
    data["maxUsers"] = graph.maxUsers
    data["num_posts"] = graph.num_posts 
    data["Users"] = []
    for person in graph.Users:
        data["Users"].append({"name":person.name, "email":person.email, "password":person.password,
            "age":person.age, "location":person.location, "gender":person.gender,
            "groups":person.groups, "posts":person.posts, "admin": person.admin})
    data["edges"]= graph.edges
    data["Posts"]= []
    for post in graph.Posts:
        data["Posts"].append({"text":post.text, "user_id":post.user_id, "post_id":post.post_id,
            "time":post.time, "Comments":[]})
        for comment in post.Comments:
            data["Posts"][-1]["Comments"].append({"text":comment.text, "user_id":comment.user_id,
                "post_id":comment.post_id, "time":str(comment.time), "comment_id":comment.comment_id})
    
    with open('users_data.json', 'w') as f:
        json.dump(data, f)
    
