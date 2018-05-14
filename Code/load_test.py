import Users as users
import Person as person
import Post as post
import LoadSave as SL

admin = users.Users(40)  # Note that the graph maxSize here is 5 but we loaded graph with 40 users
SL.load(admin)
admin.show_graph()
print(admin.numUsers)
admin.show_all_posts()
