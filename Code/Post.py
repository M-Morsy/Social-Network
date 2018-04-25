class Post:
    Post_ID = 0
   
    def __init__ (self, text, user_ID):
        self.text = text
        self.user_ID = user_ID
        Post.Post_ID += 1
        self.Post_ID = Post.Post_ID
        self.Comments=[]
    def __del__(self):
        pass        
    def get_Post_ID (self):
        return self.Post_ID
    def set_Post_ID (self, Post_ID):
        self.Post_ID = Post_ID
    def get_user_ID (self):
        return self.user_ID
    def get_text(self):
        return self.text
    def edit (self, text):
        self.text = text
    def AddComment(self, text, user_ID):
        self.Comments.append(Comment(text, user_ID, self.Post_ID))
    def editComment(self, text, CommentCount):
        self.Comments[CommentCount].edit(text)
    def deleteComment(self, CommentCount):
        del self.Comments[CommentCount]
    def get_Comments_num(self):
        return len(self.Comments)
    def Post_view (self):
        Post_contents = "{}\n \n".format(self.text)
        i = 1
        for x in self.Comments:
            Post_contents += "     {}- {}: {} \n \n".format(i, x.user_ID, x.text)
            i += 1
        return Post_contents
    
class Comment:
    Comment_ID = 0

    def __init__ (self, text, user_ID, Post_ID):
        self.text = text 
        self.user_ID = user_ID
        self.Post_ID = Post_ID
        Comment.Comment_ID += 1
        self.Comment_ID = Comment.Comment_ID
    def __del__(self):
        pass        
    def get_text(self):
        return self.text
    def get_Post_ID(self):
        return self.Post_ID
    def get_Comment_ID(self):
        return self.Comment_ID
    def set_Comment_ID(self, Comment_ID):
        self.Comment_ID = Comment_ID
    def get_user_ID(self):
        return self.user_ID
    def edit (self, text):
        self.text = text

