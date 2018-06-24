import LoadSave as SL
import Users as users
import Person as person
import re

# ** functions used ** #
def binary_edge_search (val):

    upper = admin.Users.edges.Length - 1
    lower = 0
    while lower <= upper:
        mid = (upper + lower) / 2
        if val > admin.Users.edges[mid]:
            lower = mid + 1
        elif val < admin.Users.edges[mid]:
            upper = mid - 1
        elif val == admin.Users.edges[mid]:
            return mid
    return -1

# ** normal user ** #

# load graph data
num = SL.getUsersNum()
admin = users.Users(num*2)
SL.load(admin)

print(admin.numUsers)
print(admin.maxUsers)

# login
print("Welcome to TR")
print("do you need to login or register ?")
print("login : 1    register : 2")
option = input()
if option == '1':
    print("Please enter your email and password")
    flag = False
    while flag is not True:
        email = input("email: ")
        email = email.strip()
        if re.match("\A(?P<name>[\w\-_.]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
            flag = True
        else:
            print("Email is invalid")
    password = input("password: ")

    # check if user exists : binary search
    flag = False
    user_num = -1
    for i in range(num):
        if (admin.Users[i].get_email() == email) and (admin.Users[i].get_password() == password):
            flag == True
            user_num = i
            break
    print(user_num)

elif option == '2':
    flag = False
    print("please enter the following data: ")
    name = input("name:")
    while flag is not True:
        email = input("email: ")
        email = email.strip()
        if re.match("\A(?P<name>[\w\-_.]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
            flag = True
        else:
            print("Email is invalid")

    flag = False
    password = input("password: ")
    age = input("age: ")
    age = int (age)
    location = input("location: ")
    print("Male / Female")
    while flag is not True:
        gender = input("gender: ")
        if gender == "Male" or gender == "male" or gender == "Female" or gender == "female":
            flag = True

    admin.AddUser(person.Person(name, email, password, age, location, gender))


    admin.show_graph()
    SL.save(admin)




# aurora@gmail.com  hamada@gmail.com
# aurora;ol7        ahm;ol

# options
