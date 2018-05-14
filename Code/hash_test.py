
import Users as users
import Person as person
import Post as post
import hashing as hsh
import LoadSave as ls

# admin and user
admin = users.Users(15)
admin.AddUser(person.Person("hamda", "ham@gmail.com", "hamadaa25", 18, "egypt"))  # 0
admin.AddUser(person.Person("ahmed", "hamada@gmail.com", "ahm;ol", 18, "german"))  # 1
admin.AddUser(person.Person("yasseen", "yasse@gmail.com", "yasse", 17, "egypt"))  # 2
admin.AddUser(person.Person("mahdy", "mahd@gmail.com", "mahdy", 18, "egypt"))  # 3
admin.AddUser(person.Person("osama", "osama@gmail.com", "640os", 21, "lebanon"))  # 4
admin.AddUser(person.Person("ahmed", "a7med1@gmail.com", "a7med13", 18, "libya")) # 5
admin.AddUser(person.Person("yasseen", "yaas@gmail.com", "851yas", 26, "egypt"))  # 6
admin.AddUser(person.Person("mahdy", "mahd@gmail.com", "mahdy", 18, "egypt"))  # 7
print(hsh.search("age", 18, "country", "egypt"))   # [0, 3, 7]
print(hsh.search("age", 18, "name", "ahmed"))   # [1, 5]
print(hsh.search("age", 18, "name", "ahmed", "country", "libya"))  # [5]
print(hsh.search("age", 18, "name", "ahmed", "country", "sudan")) # []
print(hsh.search("name", "yasseen", "country", "egypt"))  # [2, 6]
print(hsh.search("name", "yasseen", "country", "egypt", "age", 21)) # []

