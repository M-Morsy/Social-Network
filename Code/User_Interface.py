import LoadSave as SL
import Users as users
import Person as person
import Post as post
import re
import hashing as hsh
import Group as group

def binary_edge_search(val):
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


def add_relation(user_num):
    print("send a request to a user from the list:")
    for i in range(admin.numUsers):
        print(i, admin.Users[i].name)
    #input()
    user_num_2 = input("select user id to send him/her a request")
    relation = input(""" What is your relation to the user ?
                        friend: 1
                        parent/child: 2
                        sibling: 3
                        relative: 4
                        """)
    admin.add_relation(sender_id=int(user_num), receiver_id=int(user_num_2), weight=int(relation))
    print("waiting for confirmation from other user to establish relation")
    SL.save(admin)


def accept_relation(user_num):
    print("Users who sent you requests")
    for i in admin.Users[2].requests_received:
        print(i, ":", admin.Users[i].name)
    user_num_2 = input("enter the user's id: ")
    admin.accept_relation(int(user_num), int(user_num_2))
    SL.save(admin)


def write_post(user_num):
   # input("please enter your post text")
    admin.add_post(post.Post(input("please enter your post text: "), user_num), user_num)
    SL.save(admin)

def comment(user_num):
    post_id = input("Which post id ?")
    post_id = int(post_id)
    admin.Posts[post_id].add_comment(input("please enter your comment text: "), user_num)
    SL.save(admin)

def group_stuff(user_num):
    choose = 10
    while choose != 9:
        print("What do you want? \n 1: create new group \n 2: join group \n 3: leave group \n 4: add new admin to the group"
              + "\n 5: remove admin from the group \n 6: add post to the group \n 7: remove post from the group \n 8: update group information\n 9: Back")
        choose = int(input())
        if choose == 1:
                print("group name:")
                name = input()
                print("group description:")
                des = input()
                #admin.add_group(user_num, name, des),
        elif choose == 2:
                print("group id:")
                id = input()
                #admin.add_member_in_group(id, user_num)
        elif choose == 3:
                print("group id:")
                id = input()
                #admin.remove_member_from_group(id, user_num)
        elif choose == 4:
                print("group id:")
                id = input()
                #admin.add_admin_to_group(id, user_num)
        elif choose == 5:
                print("group id:")
                id = input()
                #admin.remove_admin_from_group(id, user_num)
        elif choose == 6:
                print("group id:")
                id = input()
                print("post id:")
                id_post = input()
                #admin.add_post_in_group(id, id_post)
        elif choose == 7:
                print("group id:")
                id = input()
                print("post id:")
                id_post = input()
                #admin.remove_post_from_group(id, id_post)
        elif choose == 8:
                print("group id:")
                id = input()
                print("group name:")
                name = input()
                print("group description:")
                des = input()
                #admin.update_group_info(id, user_num, name, des)
        #SL.save(admin)


def actions(user_num):
    option = input("""Do you wanna add actions ?
            yes : 1
            no : 2""")
    option = int(option)
    if option == 1:
        pass
    elif option == 2:
        return 2
    else:
        print("Error")
        return -1
    option2 = input("""Do you want to: 
                post: 1
                comment: 2
                add relation: 3
                accept relation: 4
                group: 5
                """)
    option2 = int(option2)
    if option2 == 1:
        write_post(user_num)
    elif option2 == 2:
        comment(user_num)
    elif option2 == 3:
        add_relation(user_num)
    elif option2 == 4:
        accept_relation(user_num)
    elif option2 == 5:
        group_stuff(user_num)

def admin():
    print("WELCOME TO ADMIN SIDE:")
    print("your network graph:")
    admin.show_graph()
    print("Histogram of the most effective users")
    print("POSTS CHART:")
    admin.post_chart()
    print("COMMENTS CHART:")
    admin.comment_chart()

    option = input("""Do you want to search some users of the same properties ?
    yes : 1
    no : 2\n""")
    option = int(option)
    if option == 2:
        print("thanks")
        pass

    flag = False
    while flag != True:
        name = input("If you wish to enter a name enter it, or enter 0 instead \n")
        age = input("If you wish to enter a age enter it, or enter 0 instead\n")
        age = int(age)
        country = input("If you wish to enter a country enter it, or enter 0 instead\n")
        if name == "0" and age == "0" and country == "0":
            print("not a valid search")
            pass
        elif name != "0" and age != "0" and country != "0":
            print("searching with name, age, and country")
            print(hsh.search("age", age, "name", name, "country", country))
            pass

        elif name != "0" and age != 0:
            print("searching with name and age")
            print(hsh.search("name", name, "age", age))

        elif country != "0" and age != 0:
            print("searching with country and age")
            print(hsh.search("country", country, "age", age))

        elif name != "0" and country != "0":
            print("searching with name and country")
            print(hsh.search("name", name, "country", country))

        elif name == "0" and age == 0:
            print("searching with country only")
            print(hsh.search("country", country))

        elif country == "0" and age == 0:
            print("searching with name only")
            print(hsh.search("name", name))

        elif name == "0" and country == "0":
            print("searching with age only")
            print(hsh.search("age", age))

        decide = input("""do you wish to search again ?
         yes : 1
         no : 2 \n""")
        if decide == "2":
            flag = True


def navigate(val, user_num=None):
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
        #input()
        #actions(user_num)

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

        # check if user exists
        flag = False
        user_num = -1
        for i in range(num):
            if (admin.Users[i].get_email() == email) and (admin.Users[i].get_password() == password):
                flag = True
                user_num = i
                break

        if flag == True:
            return user_num

        elif email == "admin@tirope.com" and password == "super_admin":

            print("WELCOME TO ADMIN SIDE:")
            print("your network graph:")
            admin.show_graph()
            print("Histogram of the most effective users")
            print("POSTS CHART:")
            admin.post_chart()
            print("COMMENTS CHART:")
            admin.comment_chart()

            option = input("""Do you want to search some users of the same properties ?
            yes : 1
            no : 2\n""")
            option = int(option)
            if option == 2:
                print("thanks")
                pass

            flag = False
            while flag != True:
                name = input("If you wish to enter a name enter it, or enter 0 instead \n")
                age = input("If you wish to enter a age enter it, or enter 0 instead\n")
                age = int(age)
                country = input("If you wish to enter a country enter it, or enter 0 instead\n")
                if name == "0" and age == "0" and country == "0":
                    print("not a valid search")
                    pass
                elif name != "0" and age != "0" and country != "0":
                    print("searching with name, age, and country")
                    print(hsh.search("age", age, "name", name, "country", country))
                    pass

                elif name != "0" and age != 0:
                    print("searching with name and age")
                    print(hsh.search("name", name, "age", age))

                elif country != "0" and age != 0:
                    print("searching with country and age")
                    print(hsh.search("country", country, "age", age))

                elif name != "0" and country != "0":
                    print("searching with name and country")
                    print(hsh.search("name", name, "country", country))

                elif name == "0" and age == 0:
                    print("searching with country only")
                    print(hsh.search("country", country))

                elif country == "0" and age == 0:
                    print("searching with name only")
                    print(hsh.search("name", name))

                elif name == "0" and country == "0":
                    print("searching with age only")
                    print(hsh.search("age", age))

                decide = input("""do you wish to search again ?
                 yes : 1
                 no : 2 \n""")
                if decide == "2":
                    flag = True
            return -2
        else:

            return -1
            # login


# load graph data
num = SL.getUsersNum()
admin = users.Users(num * 2)
SL.load(admin)

print(admin.numUsers)
print(admin.maxUsers)

# interface
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
print(user_num)
if user_num == -1:
    print("Error")

elif user_num == -2:
    print("Thanks ADMIN !!")
else:
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
        navigate(3, user_num)  # profile info
        input()
        navigate(2, user_num)  # Timeline
        input()
    elif option == '2':
        navigate(2, user_num)
        input()
    while True:
        num = actions(user_num)
        if num != 1:
            break

    print("Thanks !")
    input("TitRope Closed !!")
