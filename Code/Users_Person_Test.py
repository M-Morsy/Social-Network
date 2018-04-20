# -*- coding: utf-8 -*-
import Users as users
import Person as person

admin = users.Users(5)
p1 = person.Person("ahmed", "hamada@gmail.com", "ahm;ol")
p2 = person.Person("hamda", "ham@gmail.com", "hamadaa25")
print(admin.IsEmpty())
print(admin.IsFull())
print(admin.numUsers)
print(admin.maxUsers)
admin.AddUser(p1)
admin.AddUser(p2)
print(admin.numUsers)
x = admin.IndexIs(p2)
print("x=",x)
admin.MarkUser(p1)
print(admin.IsMarked(p1))
print(admin.edges)
admin.AddEdge(p1,p2,20)
print(admin.WeightIs(p1,p2))
