# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:40:59 2018

@author: maged
"""
import json
import Users as users
import Person as person
import Post as post

                        
            
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
    data["edges"]= []
    
    for row in graph.edges:
        data["edges"].append([])
        for col in row:
            if type(col)== int:
                data["edges"][-1].append(col)
            else:
                data["edges"][-1].append(col.value)
    
    data["Posts"]= []
    for post in graph.Posts:
        data["Posts"].append({"text":post.text, "user_id":post.user_id, "post_id":post.post_id,
            "time":post.time, "Comments":[]})
        for comment in post.Comments:
            data["Posts"][-1]["Comments"].append({"text":comment.text, "user_id":comment.user_id,
                "post_id":comment.post_id, "time":str(comment.time), "comment_id":comment.comment_id})
    
    with open('users_data.json', 'w') as f:
        json.dump(data, f)
    
    
def load(graph):
    with open('users_data.json') as f:
        data = json.load(f)
        
    graph.numUsers = int(data["numUsers"])
    graph.maxUsers = int(data["maxUsers"]) 
    graph.num_posts = int(data["num_posts"])
    for one in data["Users"]:
        graph.Users.append(person.Person(one["name"], one["email"], one["password"], one["age"], 
                                         one["location"], one["gender"]))
        graph.Users[-1].groups = [int(i) for i in one["groups"]]
        graph.Users[-1].posts = [int(i) for i in one["posts"]]
        graph.Users[-1].admin = [int(i) for i in one["admin"]]
        
    graph.edges=[]
    for row in range(0, len(data["edges"])):
        graph.edges.append([])
        for col in range(0, len(data["edges"][row])):
            if int(data["edges"][row][col]) == -1 :
                graph.edges[row].append(-1)
            elif int(data["edges"][row][col]) == 0 :
                graph.edges[row].append(users.relation.Friend)
            elif int(data["edges"][row][col]) == 1 :
                graph.edges[row].append(users.relation.Sibling)
            elif int(data["edges"][row][col]) == 2 :
                graph.edges[row].append(users.relation.Parent)
            elif int(data["edges"][row][col]) == 3 :
                graph.edges[row].append(users.relation.Child)
            elif int(data["edges"][row][col]) == 4 :
                graph.edges[row].append(users.relation.Relative)
            elif int(data["edges"][row][col]) == 5 :
                graph.edges[row].append(5)
            else : graph.edges[row].append(int(data["edges"][row][col]))         
            
    for i in data["Posts"]:
        graph.Posts.append(post.Post(i["text"], int(i["user_id"])))
        graph.Posts[-1].post_id = int(i["post_id"])
        graph.Posts[-1].time = i["time"]
        for j in i["Comments"]:
            graph.Posts[-1].Comments.append(post.Comment(j["text"], int(j["user_id"]), int(j["post_id"])))
            graph.Posts[-1].Comments[-1].time = j["time"]
            graph.Posts[-1].Comments[-1].comment_id = int(j["comment_id"])
        