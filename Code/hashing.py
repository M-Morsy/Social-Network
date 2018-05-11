# ** Binary Tree Class ** #
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

    def delete(self, key):
        """ delete the node with the given key and return the
        root node of the tree """

        if self.id == key:
            # found the node we need to delete

            if self.right and self.left:

                # get the successor node and its parent
                [psucc, succ] = self.right._findMin(self)

                # splice out the successor
                # (we need the parent to do this)

                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                # reset the left and right children of the successor

                succ.left = self.left
                succ.right = self.right

                return succ

            else:
                # "easier" case
                if self.left:
                    return self.left  # promote the left subtree
                else:
                    return self.right  # promote the right subtree
        else:
            if self.key > key:  # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(key)
                # else the key is not in the tree

            else:  # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(key)

        return self

# ** Hash Tables For Fast Searching ** #

# age binary trees
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

# name binary trees
nameRoot0 = Node("l",-1)
nameRoot1 = Node("m",-1)
nameRoot2 = Node("n",-1)
nameRoot3 = Node("o",-1)
nameRoot4 = Node("p",-1)
nameRoot5 = Node("q",-1)
nameRoot6 = Node("r",-1)
nameRoot7 = Node("s",-1)
nameRoot8 = Node("t",-1)
nameRoot9 = Node("u",-1)
nameRoot10 = Node("v",-1)
nameRoot11 = Node("w",-1)

# country graph
countryRoot0 = Node("l",-1)
countryRoot1 = Node("m",-1)
countryRoot2 = Node("n",-1)
countryRoot3 = Node("o",-1)
countryRoot4 = Node("p",-1)
countryRoot5 = Node("q",-1)
countryRoot6 = Node("r",-1)
countryRoot7 = Node("s",-1)
countryRoot8 = Node("t",-1)
countryRoot9 = Node("u",-1)
countryRoot10 = Node("v",-1)
countryRoot11 = Node("w",-1)

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
def nameHashFunc(name):
    sum = 0
    for char in name:
        sum += ord(char) * 70
    return  sum%12

# Hash Tables For Fast Searching #
nameTable = {0: nameRoot0, 1: nameRoot1, 2: nameRoot2, 3: nameRoot3, 4: nameRoot4,
                    5: nameRoot5, 6: nameRoot6, 7: nameRoot7, 8: nameRoot8, 9: nameRoot9,
                    10: nameRoot10, 11: nameRoot11}
countryTable = {0: countryRoot0, 1: countryRoot1, 2: countryRoot2, 3: countryRoot3,
                    4: countryRoot4, 5: countryRoot5, 6: countryRoot6, 7: countryRoot7,
                    8: countryRoot8, 9: countryRoot9, 10: countryRoot10, 11: countryRoot11}
ageTable = {9: ageRoot9, 19: ageRoot19, 29: ageRoot29, 39: ageRoot39,
                49: ageRoot49, 59: ageRoot59, 69: ageRoot69, 79: ageRoot79,
                89: ageRoot89, 99: ageRoot99, 109: ageRoot109, 119: ageRoot119}


"""
root = Node(10,-1)
root.insert(5,1)
root.insert(15,2)
root.insert(10,0)
#root.PrintTree()
ww = ageHashFunc(5)
addNodeToAgeTree(9,1,5)
ageRoot9.PrintTree()
# 0,1,2
a = nameHashFunc("waleed")
print(a)
"""