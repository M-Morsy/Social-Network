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
admin.AddEdge(admin.Users[0],admin.Users[1],20)
print(admin.WeightIs(admin.Users[0],admin.Users[1]))
print(admin.Users[0].get_name())
print(admin.Users[0].get_password())
admin.Users[0].set_password("1234")
print(admin.Users[0].get_password())

# post
print ("\nPost Testing: \n")
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
