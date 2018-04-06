class Post:
    Post_ID = 0
    def __init__ (self, text, user_ID):
        self.text = text
        self.user_ID = user_ID
        Post.Post_ID += 1
        self.Post_ID = Post.Post_ID
        self.Comments=[]
        self.CommentCount = 0
    def edit (self, text):
        self.text = text
    def AddComment(self, text, user_ID):
        self.CommentCount +=1
        self.Comments.append(Comment(text, user_ID, self.Post_ID, self.CommentCount))
    def editComment(self, text, CommentCount):
        self.Comments[CommentCount].text = text
    def deleteComment(self, CommentCount):
        del self.Comments[CommentCount]
    
class Comment:
    Comment_ID = 0
    def __init__ (self, text, user_ID, Post_ID, CommentCount):
        self.text = text 
        self.user_ID = user_ID
        self.Post_ID = Post_ID
        Comment.Comment_ID += 1
        self.Comment_ID = Comment.Comment_ID
        self.CommentCount = CommentCount
        
