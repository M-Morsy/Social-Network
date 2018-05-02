# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:38:07 2018

@author: maged
"""

from Post import *

post1 = Post('yalla nro7 el so5na', 125)
post1.add_comment('mashy', 8)
post1.add_comment('la fakss', 36)
post1.add_comment('msh fady', 98)
post1.add_comment('lih yagd3aaan!!', 125)
post1.add_comment('fih final bokra!', 98)
post1.add_comment('ya 7ywan ya mot5lf.. enta yatrash', 36)
post1.edit_comment("edited comment", 3)
post2 = Post('el so7ab fi agaza', 125)
post2.add_comment ("let's see", 200)
print(post2.get_text())
print(post1.post_view())
print(post2.post_view())
print(post1.get_comments_num())
print()
# integration between comment and post
print("TESTING INTEGRATION BETWEEN POST AND COMMENT:")
print("----------------------------------------------")
print("comment 0 in post1 text: ", post1.Comments[0].get_text())
print("comment 1 in post1 global id: ", post1.Comments[1].get_comment_id())
print("comment 1 in post1 local id: ", post1.get_comment_id('la fakss'))
print("comment 0 in post2 global id: ", post2.Comments[0].get_comment_id())
print("comment 0 in post2 local id: ", post2.get_comment_id("let's see"))


# get id of a comment
print(post1.Comments[3].get_comment_id)
# print(post1.get_comment_id('ya 7ywan ya mot5lf.. enta yatrash'))
print()
# ** get post time ** #
print("TESTING THE TIME ATTRIBUTE: ")
print("------------------------------")
print("first post time is: ", post1.time)
print("second post time is: ", post2.time)
print()
print("TESTING TIME COMPARISONS: ")
print("------------------------------")
print("post1.time > post2.time: ", post1.time > post2.time)
print("post1.time < post2.time: ", post1.time < post2.time)
print("post1.time == post2.time:", post1.time == post2.time)
print("type of time is: ", type(post1.time))

print("comment 0 on post 1 time with local id: ", post1.get_comment_time(0))  # use local comment id here
print("comment 0 on post 2 time with local id: ", post2.get_comment_time(0))
