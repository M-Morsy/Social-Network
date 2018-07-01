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

def option:

def navigate(val, user_num = None):
    if val == 1:
        # registeration
        flag = False
        print("please enter the following data: ")
        name = input("name:")
        while flag is not True:
            email = input("email: ")
            email = email.strip()
            if re.match("\A(?P<name>[\w\-_.]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z", email, re.IGNORECASE):
                flag = True
            else:
                print("Email is invalid")

        flag = False
        password = input("password: ")
        age = input("age: ")
        age = int(age)
        location = input("location: ")
        print("Male / Female")
        while flag is not True:
            gender = input("gender: ")
            if gender == "Male" or gender == "male" or gender == "Female" or gender == "female":
                flag = True

        admin.AddUser(person.Person(name, email, password, age, location, gender))


        pass
    elif val == 2:
        # timeline
        print("YOUR TIMELINE: ")
        print("---------------")
        admin.get_friends_posts(user_num)
        pass
    elif val == 3:
        # profile, more data
        print("name     : ", admin.Users[user_num].name)
        print("email    : ", admin.Users[user_num].email)
        print("age      : ", admin.Users[user_num].age)
        print("gender   : ", admin.Users[user_num].gender)
        print("location : ", admin.Users[user_num].location)
        pass
    elif val == 4:
        # login
        print("Please enter your email and password")
        flag = False
        while flag is not True:
            email = input("email: ")
            email = email.strip()
            if re.match("\A(?P<name>[\w\-_.]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z", email, re.IGNORECASE):
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
        return user_num
        # login


# ** normal user ** #

# load graph data
num = SL.getUsersNum()
admin = users.Users(num*2)
SL.load(admin)

print(admin.numUsers)
print(admin.maxUsers)

# login
print("Welcome to TR")
print("do you need to register ?")
print("yes : 1    no : 2")
option = input()
if option == '1':
    navigate(1)
    admin.show_graph()
    SL.save(admin)
    # code to login


user_num = navigate(4)

# print(user_num) # aurora@gmail.com  aurora;ol7  # 16
print("Your Profile")
print("-----------")
print("name: ", admin.Users[user_num].name)
print("email: ", admin.Users[user_num].email)
print(" What do you wish to do ?")
option = input(""" More Information : 1
          Timeline : 2
          """)

if option == '1':
    navigate(3, user_num)
    print()
    navigate(2, user_num)
elif option == '2' :
    navigate(2, user_num)


