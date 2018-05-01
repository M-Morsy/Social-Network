# -*- coding: utf-8 -*-
import Users as users
import Person as person
import Post as post


# admin and user
admin = users.Users(5)
print(admin.IsEmpty())
print(admin.IsFull())
print(admin.numUsers)
print(admin.maxUsers)
p1 = person.Person("ahmed", "hamada@gmail.com", "ahm;ol")
admin.AddUser(p1)
admin.AddUser(person.Person("hamda", "ham@gmail.com", "hamadaa25"))

print(p1.get_id())
print("user number 1 name is", admin.Users[1].get_name())

print(admin.numUsers)
x = admin.IndexIs(admin.Users[1])
print("x=", x)
admin.MarkUser(admin.Users[1])
print(admin.IsMarked(admin.Users[1]))
print(admin.edges)
admin.AddEdge(admin.Users[0], admin.Users[1], 20)
print(admin.edges)
print(admin.WeightIs(admin.Users[0],admin.Users[1]))
print(admin.Users[0].get_name())
print(admin.Users[0].get_password())
admin.Users[0].set_password("1234")
print(admin.Users[0].get_password())

# post
print ("\nPOST TESTING:")
print("--------------")
admin.add_post(post.Post("test text", 1), 1)
print(admin.Posts[0].post_view())
print(admin.post_view(0), "\n")

# comment
admin.Posts[0].add_comment("my first comment", user_id=0)
print(admin.Posts[0].post_view())
admin.add_comment("my second comment", post_id=0, user_id=0)
print(admin.Posts[0].post_view())
admin.Posts[0].delete_comment(comment_count=1)
print(admin.Posts[0].post_view())

# adding and removing people
print ("TESTING PEOPLE'S RELATIONS:")
print("----------------------------")
admin.add_relation(sender_id=1, receiver_id=0)
print("Request sent as friend - default")
print("Relation still like before\n", admin.edges)
admin.accept_relation(1,0)
print("Request accepted:\n", admin.edges, "\n")

weight = users.relation.Parent
admin.add_relation(sender_id=1, receiver_id=0, weight=weight)
print("Request sent as", weight)
print("Relation still like before\n", admin.edges)
admin.accept_relation(1,0)
print("Request accepted:\n", admin.edges)
admin.remove_relation(1,0)
print("Relation Removed: \n", admin.edges, "\n")

# show friends & search
print("TESTING SHOW FRIENDS:")
print("--------------------")
admin.add_relation(sender_id=1, receiver_id=0, weight = 5)
admin.accept_relation(1,0)
print("\nUser with ID 0 friends are: ")
admin.show_friends(0)   #  problem with id = 0 >> edges = 0 also
print("\nUser with ID 1 friends are: ")
admin.show_friends(1)
admin.AddUser(person.Person("noFriend", "no_fr@gmail.com", "NoFriendsAtall"))
print("\nuser number 2 name is", admin.Users[2].get_name())
print("User with ID 2 friends are: ")
admin.show_friends(2)

admin.AddUser(person.Person("ManyFriends", "many_fr@gmail.com", "ManyFriends"))
print("\nuser number 3 name is", admin.Users[3].get_name())
print("User with ID 3 friends are: ")
admin.show_friends(3)
admin.add_relation(sender_id=3, receiver_id=0)
admin.add_relation(sender_id=3, receiver_id=1)
admin.add_relation(sender_id=3, receiver_id=2)
print("\nPerson with ID 3 sent requests:", admin.show_sent_requests(3))
admin.accept_relation(3, 0)
admin.accept_relation(3, 1)
admin.accept_relation(3, 2)
print("\nUser with ID 3 friends are: ")
admin.show_friends(3)
print("\n")

print("TESTING SHOW FRIENDS POSTS:")
print("--------------------")
admin.show_friends_posts(0)# Not working
print()
admin.show_friends_posts(1)
print()
admin.show_friends_posts(2)
print()
admin.show_friends_posts(3)
print()