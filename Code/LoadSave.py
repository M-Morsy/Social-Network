# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:40:59 2018

@author: maged
"""
import json
import Users as users
import Person as person
import Post as post
import Group as group

                        
    #takes the whole graph represnting the system and save it in a json file
def save(graph) :
    data = {}
    data["numUsers"]= graph.numUsers 
    data["maxUsers"] = graph.maxUsers
    data["num_posts"] = graph.num_posts 
    data["Users"] = []
    for person in graph.Users:
        data["Users"].append({"name":person.name, "email":person.email, "password":person.password,
            "age":person.age, "location":person.location, "gender":person.gender,
            "groups":person.groups, "posts":person.posts, "admin": person.admin,
            "requests_sent":{}, "requests_received": {}})
        for x in person.requests_sent:
            if type (person.requests_sent[x]) == int:
                data["Users"][-1]["requests_sent"][x]= person.requests_sent[x]
            else:
                data["Users"][-1]["requests_sent"][x]= person.requests_sent[x].value
                
        for x in person.requests_received:
            if type (person.requests_received[x]) == int:
                data["Users"][-1]["requests_received"][x]= person.requests_received[x]
            else:
                data["Users"][-1]["requests_received"][x]= person.requests_received[x].value
            
            
    data["edges"]= graph.edges
    
    data["Posts"]= []
    for post in graph.Posts:
        data["Posts"].append({"text":post.text, "user_id":post.user_id, "post_id":post.post_id,
            "time":post.time, "Comments":[]})
        for comment in post.Comments:
            data["Posts"][-1]["Comments"].append({"text":comment.text, "user_id":comment.user_id,
                "post_id":comment.post_id, "time":str(comment.time), "comment_id":comment.comment_id})
    
    data["Groups"]= []
    for group in graph.Groups:
        data["Groups"].append({"admin_id":group.admin_id, "group_id":group.group_id,
            "group_name":group.group_name, "group_description":group.group_description,
            "group_members":group.group_members, "group_posts":group.group_posts,
            "group_count":group.group_count})
    
    with open('users_data.json', 'w') as f:
        json.dump(data, f)
    
#load func. to extract the data from a json file containing it,
#and put it back into a given 'Users' object representing a graph
def load(graph):
    with open('users_data.json') as f:
        data = json.load(f)
        
    graph.numUsers = 0
    graph.maxUsers = int(data["maxUsers"]) 
    graph.num_posts = int(data["num_posts"])
    for one in data["Users"]:
        graph.AddUser(person.Person(one["name"], one["email"], one["password"], one["age"], 
                                         one["location"], one["gender"]))
        graph.Users[-1].groups = [int(i) for i in one["groups"]]
        graph.Users[-1].posts = [int(i) for i in one["posts"]]
        graph.Users[-1].admin = [int(i) for i in one["admin"]]
        for x in one["requests_sent"]:
            graph.Users[-1].requests_sent[int(x)] = int(one["requests_sent"][x])
            
        for x in one["requests_received"]:
            graph.Users[-1].requests_received[int(x)] = int(one["requests_received"][x])
        
        
    graph.edges=[]
    for row in range(0, len(data["edges"])):
        graph.edges.append([])
        for col in range(0, len(data["edges"][row])):
            graph.edges[row].append([int(data["edges"][row][col][0]), int(data["edges"][row][col][1])])         
            
    for i in data["Posts"]:
        graph.Posts.append(post.Post(i["text"], int(i["user_id"])))
        graph.Posts[-1].post_id = int(i["post_id"])
        graph.Posts[-1].time = i["time"]
        for j in i["Comments"]:
            graph.Posts[-1].Comments.append(post.Comment(j["text"], int(j["user_id"]), int(j["post_id"])))
            graph.Posts[-1].Comments[-1].time = j["time"]
            graph.Posts[-1].Comments[-1].comment_id = int(j["comment_id"])
    
    for g in data["Groups"]:
        graph.Groups.append(group.Group(0, g["group_name"], g["group_description"]))
        graph.Groups[-1].admin_id= [int(i) for i in g["admin_id"]]
        graph.Groups[-1].group_id= int(g["group_id"])
        graph.Groups[-1].group_members= [int(i) for i in g["group_members"]]
        graph.Groups[-1].group_posts= [int(i) for i in g["group_posts"]]
        graph.Groups[-1].group_count= int(g["group_count"])


def getUsersNum():
    with open('users_data.json') as f:
        data = json.load(f)   
    return data["numUsers"]
