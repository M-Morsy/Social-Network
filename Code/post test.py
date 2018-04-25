# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:38:07 2018

@author: maged
"""

from Post import *
post1 = Post('yalla nro7 el so5na', 125)
post1.AddComment('la fakss', 36)
post1.AddComment('msh fady', 98)
post1.AddComment('lih yagd3aaan!!', 125)
post1.AddComment('fih final bokra!', 98)
post1.AddComment('ya 7ywan ya mot5lf.. enta yatrash', 36)

post2 = Post('el so7ab fi agaza', 125)
print(post2.get_text())
print(post1.post_view())
print(post2.post_view())