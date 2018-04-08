class Users(): 
 #** Data **##
  numUsers = 0  
  maxUsers = 0
  Users = [] # or array(Person())
  edges = [][]
  marks = []
 ##** Constructor & Destrcutor **##
 def __init__(self, maxUsers):
        self.maxUsers     = maxUsers
 def __del__(self):
        print ("users: " , self.Users[])
 ##** Graph functionality **##
  def MakeEmpty():
  def IsEmpty():
  def IsFull():
  def AddUser(person):
        Users.append(person)
        numUsers++
  def AddEdge(fromPesron, toPerson, weight):
        row = IndexIs(Users, fromPesron)
        col = IndexIs(Users, toPerson)
        edges[row][col] = weight
  def WeightIs(fromPesron, toPerson):
        row = IndexIs(Users, fromPerson)
        col = IndexIs(vertices, toPerson);
        return edges[row][col]
  def GetToUsers(pesron, Quepesron<pesron>&):
  def ClearMarks():
  def MarkUser(pesron):
  def IsMarked(pesron):
  # searching algorithm
  def DepthFirstSearch(users<person> graph, person startUser, person endUser):
  def BreadthFirtsSearch(users<person> graph, person startUser, person endUser):
