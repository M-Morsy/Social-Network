from Code import Person
from Person import *

p1 = Person("ahmed", "hamada@gmail.com", "ahm;ol")
print(p1.get_ID())
print(p1.get_name())
print(p1.get_email())
print(p1.get_password())
print(p1.get_info())

p2 = Person ("hamda" , "ham@gmail.com" , "hamadaa25")
print(p2.get_email())
print(p2.get_ID())
print(p2.get_name())
print(p2.get_password())
print(p2.get_info())

print ("Count = ", Person.Count)

# print (Person.name) >> error
# print(Person.dict)