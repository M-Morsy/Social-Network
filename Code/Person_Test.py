from Code import Person
# from Person import *

# person adding and getters
p1 = Person.Person("ahmed", "hamada@gmail.com", "ahm;ol")
print(p1.get_id())
print(p1.get_name())
print(p1.get_email())
print(p1.get_password())
print(p1.get_info())

p2 = Person.Person("hamda", "ham@gmail.com", "hamadaa25")
print(p2.get_email())
print(p2.get_id())
print(p2.get_name())
print(p2.get_password())
print(p2.get_info())
print("Count = ", Person.Person.Count)

# post addition and removal testing
print ("added post ID 2")
p2.add_post(2)
p2.add_post(10)
print(p2.get_posts_ids())
print(p2.posts.index(10))
print ("removed post ID 2")
p2.remove_post(2)
print(p2.get_posts_ids())
# post

# print (Person.name) >> error
# print(Person.dict)
