class Users(): 
  #** Data **##
  numUsers = 0  # Actual number of users in the site 
  maxUsers = 0 # Max number of users in the site we can deal with
  Users = [0 for x in range(maxUsers)] # all users
  edges = [[0 for x in range(maxUsers)] for y in range(maxUsers)] # all connection between users
  marks = [0 for x in range(maxUsers)] # mark user when search about special one
  ##** Constructor & Destrcutor **##
  def __init__(self, maxUsers): # set the value of max users
        self.maxUsers     = maxUsers 
  def __del__(self): # nothing to do 
       print ("users: ")
  ##** Graph functionality **##
  def MakeEmpty(self): # delete every thing
      self.numUsers = 0
      self.maxUsers = 0
      del self.Users
      del self.edges
      del self.marks
  def IsEmpty(self): # return true if no users
      if self.numUsers == 0:
        return bool(1)
      return bool(0)
  def IsFull(self): # return true if limit of users is full
      if self.numUsers == self.maxUsers:
          return bool(1)
      return bool(0)
  def IndexIs(self,person): # return index of special user
      i = 0
      for user in self.Users:
          if user == person:
              return i
          i += 1
      return
  def AddUser(self,person): # add new user
      self.Users.append(person)
      self.numUsers += 1
  def AddEdge(self,fromPesron, toPerson, weight): # add new connection
      row = self.IndexIs(fromPesron)
      col = self.IndexIs(toPerson)
      self.edges[row][col] = weight
  def WeightIs(self,fromPesron, toPerson): # add weight between two users
      row = self.IndexIs(fromPesron)
      col = self.IndexIs(toPerson)
      return self.edges[row][col]
  def GetToUsers(self,pesron): #for searching algorithm
      print("nothing")
  def ClearMarks(self): # delete all marks
      del self.marks
      self.marks = [0 for x in range(self.maxUsers)]
  def MarkUser(self,pesron): # mark user to ignore it in searching 
      index = self.IndexIs(pesron)
      self.marks[index] = 1
  def IsMarked(self,pesron): # is user marked?
      index = self.IndexIs(pesron)
      return bool(self.marks[index])
  # searching algorithm
  def DepthFirstSearch(self, startUser, endUser):
      print("nothing")
  def BreadthFirtsSearch(self, startUser, endUser):
      print("nothing")
