# Binary Tree Class
class Node:

    def __init__(self, data , id):

        self.left = None
        self.right = None
        self.data = data
        self.id = id

    def insert(self, data , id):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data,id)
                else:
                    self.left.insert(data,id)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data,id)
                else:
                    self.right.insert(data,id)
            else:
                if self.left is None:
                    self.left = Node(data,id)
                else:
                    self.left.insert(data,id)
        else:
            self.data = data
            self.id = id

# Print the tree from largest element to lowest one
    def PrintTree(self):
        if self.right:
            self.right.PrintTree()
        print(self.data, self.id)
        if self.left:
            self.left.PrintTree()

# Hash Tables For Fast Searching #
ageRoot9 = Node(int(9 / 2) + 1, -1)
ageRoot19 = Node(int(19 / 2) + 1, -1)
ageRoot29 = Node(int(29 / 2) + 1, -1)
ageRoot39 = Node(int(39 / 2) + 1, -1)
ageRoot49 = Node(int(49 / 2) + 1, -1)
ageRoot59 = Node(int(59 / 2) + 1, -1)
ageRoot69 = Node(int(69 / 2) + 1, -1)
ageRoot79 = Node(int(79 / 2) + 1, -1)
ageRoot89 = Node(int(89 / 2) + 1, -1)
ageRoot99 = Node(int(99 / 2) + 1, -1)
ageRoot109 = Node(int(109 / 2) + 1, -1)
ageRoot119 = Node(int(119 / 2) + 1, -1)

# ** HashTables functionality ** #
def ageHashFunc(age):
        if 0 <= age <= 9:
            return 9
        elif 10 <= age <= 19:
            return 19
        elif 20 <= age <= 29:
            return 29
        elif 30 <= age <= 39:
            return 39
        elif 40 <= age <= 49:
            return 49
        elif 50 <= age <= 59:
            return 59
        elif 60 <= age <= 69:
            return 69
        elif 70 <= age <= 79:
            return 79
        elif 80 <= age <= 89:
            return 89
        elif 90 <= age <= 99:
            return 99
        elif 100 <= age <= 109:
            return 109
        else:
            return 119

def addNodeToAgeTree(age, id, personAge):
    if age == 9:
        ageRoot9.insert(personAge, id)
    elif age == 19:
        ageRoot19.insert(personAge, id)
    elif age == 29:
        ageRoot29.insert(personAge, id)
    elif age == 39:
        ageRoot39.insert(personAge, id)
    elif age == 49:
        ageRoot49.insert(personAge, id)
    elif age == 59:
        ageRoot59.insert(personAge, id)
    elif age == 69:
        ageRoot69.insert(personAge, id)
    elif age == 79:
        ageRoot79.insert(personAge, id)
    elif age == 89:
        ageRoot89.insert(personAge, id)
    elif age == 99:
        ageRoot99.insert(personAge, id)
    elif age == 109:
        ageRoot109.insert(personAge, id)
    else:
        ageRoot119.insert(personAge, id)
"""
root = Node(10,-1)
root.insert(5,1)
root.insert(15,2)
root.insert(10,0)
#root.PrintTree()
ww = ageHashFunc(5)
addNodeToAgeTree(9,1,5)
ageRoot9.PrintTree()
"""