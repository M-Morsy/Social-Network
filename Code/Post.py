from datetime import datetime
import Person as person
class Comment:
    comment_id = 0

    def __init__ (self, text, user_id, post_id):
        self.text = text
        self.user_id = user_id
        self.post_id = post_id
        self.time = datetime.now()
        self.comment_id = Comment.comment_id
        Comment.comment_id += 1

    def __del__(self):
        pass

    def get_text(self):
        return self.text

    def get_post_id(self):
        try:
            return self.post_id
        except:
            print("access error")

    def get_comment_id(self):
        return self.comment_id

    def get_comment_time(self):
        return self.time

    def set_comment_id(self, comment_id):
        self.comment_id = comment_id

    def get_user_id(self):
        return self.user_id

    def edit(self, text):
        self.text = text

class Post(Comment, person.Person):
    post_count = 0
   
    def __init__ (self, text, user_id):
        self.text = text
        self.user_id = user_id
        self.post_id = Post.post_count
        self.time = str(datetime.now())
        Post.post_count += 1
        self.Comments = []

    def __del__(self):
        pass

    def get_post_id (self):
        return self.post_id

    def set_post_id (self, post_id):
        self.post_id = post_id

    def get_user_id (self):
        return self.user_id

    def get_text(self):
        return self.text

    def edit (self, text):
        self.text = text

    def get_time(self):
        return  self.time

    def add_comment (self, text, user_id):
        '''to be done after Soha's task: 30 user scenario'''
        #if(person.Person.Count < user_id):
         #   print("not a valid user")
        #else:
         #   self.Comments.append(Comment(text, user_id, self.post_id))
        self.Comments.append(Comment(text, user_id, self.post_id))


    def edit_comment(self, text, comment_count):
        try:
            self.Comments[comment_count].edit(text)
        except:
            print("Error in accessing the list")

    def delete_comment(self, comment_count):
        del self.Comments[comment_count]

    def get_comment_id(self, text):
        for i in range(self.Comments.__len__()):
            if self.Comments[i].get_text() == text:
                return i

    def get_comments_num(self):     # return local comments number
        return len(self.Comments)

    def get_comment_time(self, comment_id):
        return self.Comments[comment_id].get_comment_time()

    def post_view(self):
        post_contents = "{}\n \n".format(self.text)
        i = 0
        for x in self.Comments:
            post_contents += "     {}- {}: {} \n \n".format(i, x.user_id, x.text)
            i += 1

        return post_contents




