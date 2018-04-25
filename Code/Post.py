class Post:
    post_id = 0
   
    def __init__ (self, text, user_id):
        self.text = text
        self.user_id = user_id
        Post.post_id += 1
        self.post_id = Post.post_id
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

    def add_comment(self, text, user_id):
        self.Comments.append(Comment(text, user_id, self.post_id))

    def edit_comment(self, text, comment_count):
        self.Comments[comment_count].edit(text)

    def delete_comment(self, comment_count):
        del self.Comments[comment_count]

    def get_comments_num(self):
        return len(self.Comments)

    def post_view(self):
        post_contents = "{}\n \n".format(self.text)
        i = 1
        for x in self.Comments:
            post_contents += "     {}- {}: {} \n \n".format(i, x.user_ID, x.text)
            i += 1

        return post_contents


class Comment:
    comment_id = 0

    def __init__ (self, text, user_id, post_id):
        self.text = text 
        self.user_id = user_id
        self.post_id = post_id
        Comment.comment_id += 1
        self.comment_id = Comment.comment_id

    def __del__(self):
        pass        

    def get_text(self):
        return self.text

    def get_post_id(self):
        return self.post_id

    def get_comment_id(self):
        return self.comment_id

    def set_comment_id(self, comment_id):
        self.comment_id = comment_id

    def get_user_id(self):
        return self.user_id

    def edit(self, text):
        self.text = text

