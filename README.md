# Social-Network
## Introduction
 A project made by third year students, Computer and Systems Department, Ain Shames University. It aims to simulate a social network application like facebook, twitter, and others.
## Contributers
1.Mohamed Morsy  
2.Shimaa Hassan  
3.Soha Alaa  
4.Maged Mabrouk  
## Code Structure
### Files
1. Person.py: class to hold each user's basic information
2. Post.py: class to hold the comment and post classes to enable users to post and comment on each others' posts
3. hashing.py: An extra data structure 
4. LoadSave.py: To load and save out Network
5. Users.py: class to hold users' data structure, a graph.  
with all the related algorithms
6. Testing files (some may be removed with time):  
    * Test senarios.py
    * User_Person_Test.py
    * posttest.py
    * Person_Test.py
    * Relation hints.py

### Details on each file
### Person.py
Each person has a set of attributes like:
* ID: for system identification
* name: user name 
* email
* password: used later on in registration
* age
* location: countries 
* gender
* posts: list of posts IDs
* groups: list of group IDs *To be done later*
* admin: list of group IDs where this person is the group admin *To be done later*
* requests_sent: dictionary with all other users' ids that this user sent friend requests to
* requests_received: dictionary with all other users' ids that this user received friend requests from
* setters and getters for all attributes
* interface with post class:
    1. add post
    2. remove post
* interface with group class:  
    *To be done later - check future work*


### Users.py
This file is divided into sections each section delivers a certain functionality
#### section one:  
* class attributes and static data 
* constructor and destructor
* Graph functionality 

#### section two: searching algorithims
 *To Be Done*

#### section three: Posts
One static attribute is Posts, which is a list of Post objects to enable use of all Post methods  
Also an interface with Comment class through Post class, not directly.  
But some extra functions are needed here like 
* add_post(self, post, user_id)  
   to add Post objects to the static Post list in class
* get_posts(self, user_id): to view all posts in the network

#### section four: Operation on a group
This section mainly is interested in relations between users, sending requests and accepting them or rejecting them  
* It's also possible to show all friends of a certain user with show_friends()  
* It's possible to show all friends' posts of a certain user, *his/her timeline*, with show_friends_posts()
* It's possible to check relation between two users

#### section five: Extract trees and graphs
This section is interested in finding the shortest path between users and returning sub trees of graphs.  
This should interface with hashing.py in the future  

*To be Done*
#### section six: Visualization
This section is intersted in visualizing graphs of sub-graphs
* show_graph(): to give a draw the whole network

*Further work needed*

####  Section Seven: Analysis on the graph
*To be done later*

### Post.py
#### Each post have some attributes:
* a string representing the post text  
* user_id: the unique ID of the user who wrote the post  
* post_id: a unique post ID to access it  
* the exact date and time when the post written  
* a list of comments objects
* each comment have the same attributes as the post  
#### Also contains some methods:  
* setters and getters for the attirbutes 
* delete post  
* edit the post text  
* delete comment  
* edit comment  
* post view to show the post and its comment contents 

#### LoadSave.py
##### The Save function  
Our network system relys on a graph containing all the users of the system connected together, this function take alll the users data and attributes like name, age, gender, posts, comments,.. etc. and save it in a dictionary within a json file to use it another time.  

##### The Load function  
it takes back the saved data from the json file. like all the users and their connections and data. and load it into its suitable data structure to become usable.

## Future work
1. Groups class
2. registration and authorization system
3. Advanced operations on the graph

