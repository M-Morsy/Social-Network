# -*- coding: utf-8 -*-
import Users as users
import Person as person
import Post as post

admin = users.Users(5)
print(admin.IsEmpty())
print(admin.IsFull())
print(admin.numUsers)
print(admin.maxUsers)
p1 = person.Person("ahmed", "hamada@gmail.com", "ahm;ol")
admin.AddUser(p1)
admin.AddUser(person.Person("hamda", "ham@gmail.com", "hamadaa25"))

print(p1.get_id())
# print("user number 1 name is", admin.Users[1].get_name())
'''
print(admin.numUsers)
x = admin.IndexIs(admin.Users[1])
print("x=",x)
admin.MarkUser(admin.Users[1])
print(admin.IsMarked(admin.Users[1]))
print(admin.edges)
admin.AddEdge(admin.Users[0],admin.Users[1],20)
print(admin.WeightIs(admin.Users[0],admin.Users[1]))
print(admin.Users[0].get_name())
print(admin.Users[0].get_password())
admin.Users[0].set_password("1234")
print(admin.Users[0].get_password())
'''

admin.User[1].add_post("test text")