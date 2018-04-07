class users {

private:

int numUsers;

int maxUsers;

person* Users;

int **edges;

bool* marks;

Public:

users();

~users();

void MakeEmpty();

bool IsEmpty() const;

bool IsFull() const;

void AddUser(person);

void AddEdge(pesron, person, int);

int WeightIs(pesron, pesron);

void GetToUsers(pesron, Quepesron<pesron>&);

void ClearMarks();

void MarkUser(pesron);

bool IsMarked(pesron) const;

void DepthFirstSearch(users<person> graph, person startUser, person endUser);



void BreadthFirtsSearch(users<person> graph, person startUser, person endUser);

}
