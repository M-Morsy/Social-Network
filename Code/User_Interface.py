import LoadSave as SL
import Users as users
import re



# ** normal user ** #

# load graph data
num = SL.getUsersNum()
admin = users.Users(num)
SL.load(admin)

# login
print("Welcome to TR")
print("do you need to login or register ?")
print("login : 1    register : 2")
option = input()
if option == '1':
    print("Please enter your email and password")
    flag = False
    while flag != True:
        email = input("email: ")
        email = email.strip()
        if re.match("\A(?P<name>[\w\-_.]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
            flag = True
        else:
            print("Email is invalid")
    password = input("password: ")

    # check if user exists
    flag = False
    user_num = -1
    for i in range(num):
        #print(admin.Users[i].get_email())
        #print(admin.Users[i].get_password())
        if (admin.Users[i].get_email() == email) and (admin.Users[i].get_password() == password):
            flag == True
            user_num = i
            break
    print(user_num)


# aurora@gmail.com  hamada@gmail.com
# aurora;ol7        ahm;ol

# options
