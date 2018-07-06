import Users as users
import Person as person
import Post as post
import LoadSave as SL
import hashing as hsh
# ** building the graph ** #
admin = users.Users(40)
print(admin.IsEmpty())
print(admin.IsFull())
print(admin.numUsers)
print(admin.maxUsers)

p1 = person.Person("ahmed", "hamada@gmail.com", "ahm;ol")
admin.AddUser(p1)
p2 = person.Person("Oleg Kolesnichenko", "oleg_Kolesnichenko@gmail.com", "oleg;o2"  ,22, "Bolivie" , "Male" )
admin.AddUser(p2)
p3 = person.Person("Amiya", "amiya@gmail.com", "amiya;o3", 30 , "Russia" , "Female")
admin.AddUser(p3)
p4 = person.Person("Russell", "russell@gmail.com", "russell;o4" , 21 , "Brazil" , "Male")
admin.AddUser(p4)
p5 = person.Person("Juggornot", "juggornot@gmail.com", "juggornot;o5", 23, "Bolivia" , "Male")
admin.AddUser(p5)
p6 = person.Person("Wone", "one_eyed@gmail.com", "one_eyed;o6", 23, "Angola" , "Male")
admin.AddUser(p6)
p7 = person.Person("Muboy", "muboy@gmail.com", "muboy;o7" ,35, "Antarctica" , "Male")
admin.AddUser(p7)
p8 = person.Person("Monu", "monu@gmail.com", "monu;o8",42 , "Usa" , "Male")
admin.AddUser(p8)
p9 = person.Person("Fynn", "fynn@gmail.com", "fynn;o9" ,13, "Poland" , "Female")
admin.AddUser(p9)
p10 = person.Person("Joe", "joe@gmail.com", "joe;o10" ,53, "Serbia" , "Male")
admin.AddUser(p10)
p11 = person.Person("Albie", "albie@gmail.com", "albie;o1l",20, "Usa" , "Female")
admin.AddUser(p11)
p12 = person.Person("Carter", "carter@gmail.com", "carter;ol2", 44,"France" , "Male")
admin.AddUser(p12)
p13 = person.Person("Jace", "jace@gmail.com", "jace;ol3",30, "England" , "Male")
admin.AddUser(p13)
p14 = person.Person("Lucien", "lucien@gmail.com", "lucien;ol4",22,"South-Africa" , "Male")
admin.AddUser(p14)
p15 = person.Person("TJ", "tJ@gmail.com", "tJ;ol5",15, "Newzland" , "Male")
admin.AddUser(p15)
p16 = person.Person("Hallie", "hallie@gmail.com", "hallie;o16", 62,"Uganda" , "Female")
admin.AddUser(p1)
p17 = person.Person("Aurora", "aurora@gmail.com", "aurora;ol7", 41,"Tunisia" , "Female")
admin.AddUser(p17)
p18 = person.Person("Luna", "luna@gmail.com", "luna;ol8", 28,"Syria" , "Female")
admin.AddUser(p18)
p19 = person.Person("Orla", "orla@gmail.com", "orla;ol9",21, "Lebanon" , "Female")
admin.AddUser(p19)
p20 = person.Person("Harper", "harper@gmail.com", "harper;o20",25, "Egypt" , "Female")
admin.AddUser(p20)
p21 = person.Person("Bonnie", "bonnie@gmail.com", "bonnie;o21",28, "Slovakia" , "Female")
admin.AddUser(p21)
p22 = person.Person("Zara", "zara@gmail.com", "zara;o22", 32,"Spain" , "Female")
admin.AddUser(p22)
p23 = person.Person("Ivy", "ivy@gmail.com", "ivy;o23",44, "	Sri-Lanka" , "Female")
admin.AddUser(p23)
p24 = person.Person("Lotti", "lotti@gmail.com", "lotti;o24",29, "Somalia" , "Female")
admin.AddUser(p24)
p25 = person.Person("Clara", "clara @gmail.com", "clara;o25",34, "Algeri" , "Female")
admin.AddUser(p25)
p26 = person.Person("Aubrey", "aubrey@gmail.com", "aubrey;o26",51, "AbuDabi" , "Female")
admin.AddUser(p26)
p27 = person.Person("Aliza", "aliza@gmail.com", "aliza;o27",37, "Switherlands" , "Female")
admin.AddUser(p27)
p28 = person.Person("Nyla", "nyla@gmail.com", "nyla;o28",45, "Ukraine" , "Female")
admin.AddUser(p28)
p29 = person.Person("Margot", "margot@gmail.com", "margot;o29",67, "Egypt" , "Female")
admin.AddUser(p29)
p30 = person.Person("Nova", "nova@gmail.com", "nova;o30", 62,"Usa" , "Female")
admin.AddUser(p30)
p31 = person.Person("Dottie", "dottie@gmail.com", "dottie;o31",39, "Uganda" , "Female")
admin.AddUser(p31)
p32 = person.Person("Winnie", "winnie@gmail.com", "winnie;o32", 70,"Spain" , "Female")
admin.AddUser(p32)
p33 = person.Person("Carys", "carys@gmail.com", "carys;o33", 25, "Female")
admin.AddUser(p33)
p34 = person.Person("Adeline", "adeline@gmail.com", "adeline;o34",35, "Usa" , "Female")
admin.AddUser(p34)
p35 = person.Person("Sydney", "sydney@gmail.com", "sydney;o35",18,"France" , "Female")
admin.AddUser(p35)
p36 = person.Person("Floriana", "floriana@gmail.com", "floriana;o36",19, "Egypt" , "Female")
admin.AddUser(p36)
p37 = person.Person("Rubena", "rubena @gmail.com", "rubena;o37",17, "Serbia" , "Female")
admin.AddUser(p37)
p38 = person.Person("Lexis", "lexis@gmail.com", "lexis;o38",26, "Angola" , "Female")
admin.AddUser(p1)
p39 = person.Person("Tayah", "tayah@gmail.com", "tayah;o39", 16,"Syria" , "Female")
admin.AddUser(p39)
p40 = person.Person("Agata", "agata@gmail.com", "agata;o40",36, "France" , "Female")
admin.AddUser(p40)



print(admin.edges)


print(admin.numUsers)


# ** relations ** #
admin.add_relation(sender_id=1, receiver_id=2, weight=2)

admin.accept_relation(1, 2)


admin.add_relation(sender_id=2, receiver_id=7, weight=0)
admin.accept_relation(2, 7)

admin.add_relation(sender_id=7, receiver_id=6, weight=3)
admin.accept_relation(7, 6)

admin.add_relation(sender_id=6, receiver_id=1, weight=4)
admin.accept_relation(6, 1)

admin.add_relation(sender_id=2, receiver_id=8, weight=1)
admin.accept_relation(2, 8)

admin.add_relation(sender_id=3, receiver_id=8, weight=2)
admin.accept_relation(3, 8)

admin.add_relation(sender_id=8, receiver_id=4, weight=0)
admin.accept_relation(8, 4)

admin.add_relation(sender_id=4, receiver_id=1, weight=2)
admin.accept_relation(4, 1)

admin.add_relation(sender_id=5, receiver_id=10, weight=3)
admin.accept_relation(5, 10)

admin.add_relation(sender_id=9, receiver_id=5, weight=0)
admin.accept_relation(9, 5)

admin.add_relation(sender_id=6, receiver_id=11, weight=0)
admin.accept_relation(6, 11)

admin.add_relation(sender_id=7, receiver_id=12, weight=0)
admin.accept_relation(7, 12)

admin.add_relation(sender_id=8, receiver_id=13, weight=2)
admin.accept_relation(8, 13)

admin.add_relation(sender_id=14, receiver_id=9, weight=0)
admin.accept_relation(14, 9)

admin.add_relation(sender_id=10, receiver_id = 15, weight = 2)
admin.accept_relation(10, 15)

admin.add_relation(sender_id=11, receiver_id=20, weight=1)
admin.accept_relation(11, 20)

admin.add_relation(sender_id=12, receiver_id=16, weight=2)
admin.accept_relation(12, 16)

admin.add_relation(sender_id=13, receiver_id=17, weight=3)
admin.accept_relation(13, 17)

admin.add_relation(sender_id=14, receiver_id=18, weight=4)
admin.accept_relation(14, 18)

admin.add_relation(sender_id=15, receiver_id=19, weight=1)
admin.accept_relation(15, 19)

admin.add_relation(sender_id=21, receiver_id=20, weight=4)
admin.accept_relation(21, 20)

admin.add_relation(sender_id=16, receiver_id=22, weight=0)
admin.accept_relation(16, 22)

admin.add_relation(sender_id=17, receiver_id=23, weight=2)
admin.accept_relation(17, 23)

admin.add_relation(sender_id=18, receiver_id=24, weight=1)
admin.accept_relation(18, 24)

admin.add_relation(sender_id=19, receiver_id=25, weight=0)
admin.accept_relation(19, 25)

admin.add_relation(sender_id=22, receiver_id=26, weight=2)
admin.accept_relation(22, 26)

admin.add_relation(sender_id=23, receiver_id=27, weight=1)
admin.accept_relation(23, 27)

admin.add_relation(sender_id=24, receiver_id=28, weight=2)
admin.accept_relation(24, 28)

admin.add_relation(sender_id=25, receiver_id=29, weight=0)
admin.accept_relation(25, 29)

admin.add_relation(sender_id=21, receiver_id=30, weight=4)
admin.accept_relation(21, 30)

admin.add_relation(sender_id=36, receiver_id=26, weight=3)
admin.accept_relation(36, 26)

admin.add_relation(sender_id=37, receiver_id=27, weight=2)
admin.accept_relation(37, 27)

admin.add_relation(sender_id=38, receiver_id=28, weight=0)
admin.accept_relation(38, 28)

admin.add_relation(sender_id=39, receiver_id=29, weight=0)
admin.accept_relation(39, 29)

admin.add_relation(sender_id=31, receiver_id=37, weight=2)
admin.accept_relation(31, 37)

admin.add_relation(sender_id=38, receiver_id=32, weight=0)
admin.accept_relation(38, 32)

admin.add_relation(sender_id=33, receiver_id=39, weight=2)
admin.accept_relation(33, 39)

admin.add_relation(sender_id=34, receiver_id=35, weight=0)
admin.accept_relation(34, 35)
print("Some Data on the users:")
print(admin.Users[5].get_name())
print(admin.Users[6].get_password())
admin.Users[6].set_password("1234")
print(admin.Users[6].get_password())

# ** show graph ** #

admin.show_graph()

print(admin.edges)

# ** posts and comments ** #
admin.add_post(post.Post("Set your goals high, and don’t stop till you get there", 1), 1 )
admin.Posts[0].add_comment("Motivation will almost always beat mere talent", 3)
admin.Posts[0].add_comment("Don't cry because it's over, smile because it happened", 4)
admin.Posts[0].add_comment("Motivation will almost always beat mere talent", 5)
admin.Posts[0].add_comment("I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best", 6)


admin.add_post(post.Post("It’s always too early to quit", 3), 3 )
admin.Posts[1].add_comment("With self-discipline most anything is possible", 4)


admin.add_post(post.Post("Out of difficulties grow miracles", 5), 5 )
admin.Posts[2].add_comment("my first comment", 6)
admin.Posts[2].add_comment("my second comment :D" , 8)
admin.Posts[2].add_comment("my third comment <3 <3 <3 ", 9)


admin.add_post(post.Post("The purpose of our lives is to be happy", 7), 7 )
admin.Posts[3].add_comment("If you have never failed you have never lived", 8)
admin.Posts[3].add_comment("Be yourself; everyone else is already taken", 10)


admin.add_post(post.Post("A jug fills drop by drop", 9), 9 )
admin.Posts[4].add_comment("The harder I work, the luckier I get", 10)



admin.add_post(post.Post("If there is no struggle, there is no progress", 11), 11 )
admin.Posts[5].add_comment("Believe and act as if it were impossible to fail", 12)
admin.Posts[5].add_comment("Two things are infinite: the universe and human stupidity; and I'm not sure about the universe", 13)

admin.add_post(post.Post("Dream big and dare to fail", 13), 13 )
admin.Posts[6].add_comment("Turn your wounds into wisdom", 14)
admin.Posts[6].add_comment("Turn your wounds into wisdom", 15)


admin.add_post(post.Post("Great ideas often receive violent opposition from mediocre minds Albert Einstein", 15), 15 )
admin.Posts[7].add_comment("Don’t count the days, make the days count.” – Muhammad Ali", 16)
admin.Posts[7].add_comment("So many books, so little time", 19)


admin.add_post(post.Post("Either I will find a way, or I will make one", 17), 17 )
admin.Posts[8].add_comment("After a storm comes a calm", 18)
admin.Posts[8].add_comment("After a storm comes a calm", 21)



admin.add_post(post.Post("Your big opportunity may be right where you are now Napoleon Hill",19), 19)
admin.Posts[9].add_comment("Whoever is happy will make others happy too", 20)
admin.Posts[9].add_comment("Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind", 22)


admin.add_post(post.Post("Never, never, never give up", 21), 21 )
admin.Posts[10].add_comment("Wherever you go, go with all your heart", 22)
admin.Posts[10].add_comment("Wherever you go, go with all your heart", 23)



admin.add_post(post.Post("Wherever you go, go with all your heart", 23), 23 )
admin.Posts[11].add_comment("Problems are not stop signs, they are guidelines", 24)
admin.Posts[11].add_comment("A room without books is like a body without a soul", 25)
admin.Posts[11].add_comment("A room without books is like a body without a soul", 24)


admin.add_post(post.Post("Things do not happen. Things are made to happen", 25), 25 )
admin.Posts[12].add_comment("Even if you fall on your face, you’re still moving forward", 26)



admin.add_post(post.Post("The dumbest people I know are those who know it all", 27), 27 )
admin.Posts[13].add_comment("Do something wonderful, people may imitate it", 28)


admin.add_post(post.Post("Life is short. Build stuff that matters", 29), 29 )
admin.Posts[14].add_comment("Everything’s got a moral, if only you can find it", 30)
admin.Posts[14].add_comment("""You've gotta dance like there's nobody watching,
Love like you'll never be hurt,
Sing like there's nobody listening,
And live like it's heaven on earth""", 36)



admin.add_post(post.Post("When I let go of what I am, I become what I might be", 31), 31 )
admin.Posts[15].add_comment("If you want to lift yourself up, lift up someone else", 32)
admin.Posts[15].add_comment("You know you're in love when you can't fall asleep because reality is finally better than your dreams", 35)

admin.add_post(post.Post("Once you choose hope, anything’s possible", 33), 33 )



admin.add_post(post.Post("Live what you love", 35), 35 )
admin.Posts[17].add_comment("All things are possible if you believe", 36)
admin.Posts[17].add_comment("You only live once, but if you do it right, once is enough.", 38)


admin.add_post(post.Post("What consumes your mind, controls your life", 37), 37 )
admin.Posts[18].add_comment("You are stronger then you think", 38)
admin.Posts[18].add_comment("Be the change that you wish to see in the world", 39)



admin.add_post(post.Post("Hope is a waking dream", 39), 39 )
admin.Posts[18].add_comment("You miss 100% of the shots you don’t take", 39)
admin.Posts[18].add_comment("In three words I can sum up everything I've learned about life: it goes on", 34)


admin.add_post(post.Post("The mind is everything. What you think you become", 39), 39 )
admin.Posts[19].add_comment("Dream big and dare to fail", 39)
admin.Posts[19].add_comment("If you want to know what a man's like, take a good look at how he treats his inferiors, not his equals", 35)



admin.add_post(post.Post("Do one thing every day that scares you", 33), 33 )
admin.Posts[20].add_comment("Tough times never last, but tough people do", 32)
admin.Posts[20].add_comment("""Don’t walk in front of me… I may not follow
Don’t walk behind me… I may not lead
Walk beside me… just be my friend""", 30)


admin.add_post(post.Post("Live each day as if your life had just begun", 29), 29 )
admin.Posts[21].add_comment("Education costs money. But then so does ignorance", 27)
admin.Posts[21].add_comment("""If you tell the truth, you don't have to remember anything
. But then so does ignorance""", 26)


admin.add_post(post.Post("Set your goals high, and don’t stop till you get there", 2), 2 )
admin.Posts[22].add_comment("Motivation will almost always beat mere talent", 1)
admin.Posts[22].add_comment("Don't cry because it's over, smile because it happened", 2)
admin.Posts[22].add_comment("I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best", 1)


admin.add_post(post.Post("It’s always too early to quit", 4), 4 )
admin.Posts[23].add_comment("With self-discipline most anything is possible", 6)


admin.add_post(post.Post("Out of difficulties grow miracles", 11), 11 )
admin.Posts[24].add_comment("my first comment", 37)
admin.Posts[24].add_comment("my second comment :D " , 36)
admin.Posts[24].add_comment("my third comment <3 <3 <3 ", 9)


admin.add_post(post.Post("The purpose of our lives is to be happy", 15), 15 )
admin.Posts[25].add_comment("If you have never failed you have never lived", 28)
admin.Posts[25].add_comment("Be yourself; everyone else is already taken", 34)


admin.add_post(post.Post("A jug fills drop by drop", 34), 34 )
admin.Posts[26].add_comment("The harder I work, the luckier I get", 40)



admin.add_post(post.Post("If there is no struggle, there is no progress", 38), 38 )
admin.Posts[27].add_comment("Believe and act as if it were impossible to fail", 20)
admin.Posts[27].add_comment("Two things are infinite: the universe and human stupidity; and I'm not sure about the universe", 5)

admin.add_post(post.Post("Dream big and dare to fail", 12), 12 )
admin.Posts[28].add_comment("Turn your wounds into wisdom", 2)
admin.Posts[28].add_comment("Turn your wounds into wisdom", 3)


admin.add_post(post.Post("Great ideas often receive violent opposition from mediocre minds Albert Einstein", 26), 26 )
admin.Posts[29].add_comment("Don’t count the days, make the days count.” – Muhammad Ali", 12)
admin.Posts[29].add_comment("So many books, so little time", 11)


admin.add_post(post.Post("Either I will find a way, or I will make one", 6), 6 )
admin.Posts[30].add_comment("After a storm comes a calm", 7)
admin.Posts[30].add_comment("After a storm comes a calm", 11)



admin.add_post(post.Post("Your big opportunity may be right where you are now Napoleon Hill",8), 8)
admin.Posts[31].add_comment("Whoever is happy will make others happy too", 13)
admin.Posts[31].add_comment("Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind", 17)


admin.add_post(post.Post("Never, never, never give up", 14), 14 )
admin.Posts[32].add_comment("Wherever you go, go with all your heart", 15)
admin.Posts[32].add_comment("Wherever you go, go with all your heart", 23)



admin.add_post(post.Post("Wherever you go, go with all your heart", 10), 10 )
admin.Posts[33].add_comment("Problems are not stop signs, they are guidelines", 14)
admin.Posts[33].add_comment("A room without books is like a body without a soul", 17)
admin.Posts[33].add_comment("A room without books is like a body without a soul", 21)


admin.add_post(post.Post("Things do not happen. Things are made to happen", 36), 36 )
admin.Posts[34].add_comment("Even if you fall on your face, you’re still moving forward", 33)



admin.add_post(post.Post("The dumbest people I know are those who know it all", 24), 27 )
admin.Posts[35].add_comment("Do something wonderful, people may imitate it", 33)


admin.add_post(post.Post("Life is short. Build stuff that matters", 18), 18 )
admin.Posts[36].add_comment("Everything’s got a moral, if only you can find it", 37)
admin.Posts[36].add_comment("""You've gotta dance like there's nobody watching,
Love like you'll never be hurt,
Sing like there's nobody listening,
And live like it's heaven on earth""", 29)



admin.add_post(post.Post("When I let go of what I am, I become what I might be", 20), 20 )
admin.Posts[37].add_comment("If you want to lift yourself up, lift up someone else", 18)
admin.Posts[37].add_comment("You know you're in love when you can't fall asleep because reality is finally better than your dreams", 19)

admin.add_post(post.Post("Once you choose hope, anything’s possible", 22), 22 )
admin.Posts[38].add_comment("If you want to lift yourself up, lift up someone else", 25)


admin.add_post(post.Post("Live what you love", 16), 16 )
admin.Posts[39].add_comment("All things are possible if you believe", 29)
admin.Posts[39].add_comment("You only live once, but if you do it right, once is enough.", 31)


admin.add_post(post.Post("What consumes your mind, controls your life", 28), 28 )
admin.Posts[40].add_comment("You are stronger then you think", 16)
admin.Posts[40].add_comment("Be the change that you wish to see in the world", 31)



admin.add_post(post.Post("Hope is a waking dream", 39), 39 )
admin.Posts[41].add_comment("You miss 100% of the shots you don’t take", 31)
admin.Posts[41].add_comment("In three words I can sum up everything I've learned about life: it goes on", 34)


admin.add_post(post.Post("The mind is everything. What you think you become", 30), 30 )
admin.Posts[42].add_comment("Dream big and dare to fail", 39)
admin.Posts[42].add_comment("If you want to know what a man's like, take a good look at how he treats his inferiors, not his equals", 35)



admin.add_post(post.Post("Do one thing every day that scares you", 32), 32 )
admin.Posts[43].add_comment("Tough times never last, but tough people do", 32)
admin.Posts[43].add_comment("""Don’t walk in front of me… I may not follow
Don’t walk behind me… I may not lead
Walk beside me… just be my friend""", 30)


admin.add_post(post.Post("Live each day as if your life had just begun", 39), 39 )
admin.Posts[44].add_comment("Education costs money. But then so does ignorance", 27)
admin.Posts[44].add_comment("""If you tell the truth, you don't have to remember anything
. But then so does ignorance""", 26)
admin.add_post(post.Post("Hope is a waking dream", 39), 39 )
admin.Posts[45].add_comment("You miss 100% of the shots you don’t take", 40)
admin.Posts[45].add_comment("In three words I can sum up everything I've learned about life: it goes on", 34)




admin.add_post(post.Post("Live what you love", 15),15 )
admin.Posts[46].add_comment("All things are possible if you believe", 36)
admin.Posts[46].add_comment("You only live once, but if you do it right, once is enough.", 38)


admin.add_post(post.Post("What consumes your mind, controls your life", 27), 27 )
admin.Posts[47].add_comment("You are stronger then you think", 38)
admin.Posts[47].add_comment("Be the change that you wish to see in the world", 39)




admin.add_post(post.Post("The mind is everything. What you think you become", 30), 30 )
admin.Posts[48].add_comment("Dream big and dare to fail", 39)
admin.Posts[48].add_comment("If you want to know what a man's like, take a good look at how he treats his inferiors, not his equals", 35)



admin.add_post(post.Post("Do one thing every day that scares you", 23), 23 )
admin.Posts[49].add_comment("Tough times never last, but tough people do", 32)
admin.Posts[49].add_comment("Don’t walk in front of me… I may not follow
Don’t walk behind me… I may not lead
Walk beside me… just be my friend", 30)


admin.add_post(post.Post("Live each day as if your life had just begun", 37), 37 )
admin.Posts[50].add_comment("Education costs money. But then so does ignorance", 27)
admin.Posts[50].add_comment("If you tell the truth, you don't have to remember anything
. But then so does ignorance", 26)


admin.add_post(post.Post("Set your goals high, and don’t stop till you get there", 12), 12 )
admin.Posts[51].add_comment("Motivation will almost always beat mere talent", 1)
admin.Posts[51].add_comment("Don't cry because it's over, smile because it happened", 2)
admin.Posts[51].add_comment("I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best", 1)


admin.add_post(post.Post("It’s always too early to quit", 14), 14 )
admin.Posts[52].add_comment("With self-discipline most anything is possible", 6)


admin.add_post(post.Post("Out of difficulties grow miracles", 17), 17 )
admin.Posts[53].add_comment("my first comment", 37)
admin.Posts[53].add_comment("my second comment :""D , 36)
admin.Posts[53].add_comment("my third comment <3 <3 <3 ", 9)


admin.add_post(post.Post("The purpose of our lives is to be happy", 25), 25 )
admin.Posts[54].add_comment("If you have never failed you have never lived", 28)
admin..Posts[54].add_comment("Be yourself; everyone else is already taken", 34)


admin.add_post(post.Post("A jug fills drop by drop", 24), 24 )
admin.Posts[55].add_comment("The harder I work, the luckier I get", 40)



admin.add_post(post.Post("If there is no struggle, there is no progress", 18), 18 )
admin.Posts[56].add_comment("Believe and act as if it were impossible to fail", 20)
admin.Posts[56].add_comment("Two things are infinite: the universe and human stupidity; and I'm not sure about the universe", 5)

admin.add_post(post.Post("Dream big and dare to fail", 22), 22 )
admin.Posts[57].add_comment("Turn your wounds into wisdom", 2)
admin.Posts[57].add_comment("Turn your wounds into wisdom", 3)



admin.add_post(post.Post("Hope is a waking dream", 19), 19 )
admin.Posts[58].add_comment("You miss 100% of the shots you don’t take", 40)
admin.Posts[58].add_comment("In three words I can sum up everything I've learned about life: it goes on", 34)





# ** hashing test ** #
'''
p9 = person.Person("Fynn", "fynn@gmail.com", "fynn;o9" ,13, "Poland" , "Female")
admin.AddUser(p9)
p10 = person.Person("Joe", "joe@gmail.com", "joe;o10" ,53, "Serbia" , "Male")
admin.AddUser(p10)
p11 = person.Person("Albie", "albie@gmail.com", "albie;o1l",20, "Usa" , "Female")
admin.AddUser(p11)
p12 = person.Person("Carter", "carter@gmail.com", "carter;ol2", 44,"France" , "Male")
admin.AddUser(p12)
p13 = person.Person("Jace", "jace@gmail.com", "jace;ol3",30, "England" , "Male")
admin.AddUser(p13)
p14 = person.Person("Lucien", "lucien@gmail.com", "lucien;ol4",22,"South-Africa" , "Male")
p36 = person.Person("Floriana", "floriana@gmail.com", "floriana;o36",19, "Egypt" , "Female")
admin.AddUser(p36)
'''
print(hsh.search("age", 13, "country", "Poland"))   # [8]
print(hsh.search("age", 53, "name", "Joe")) # [9]
print(hsh.search("age", 20, "name", "Albie", "country", "Usa"))  # [10]
print(hsh.search("age", 44, "name", "Carter", "country", "France"))  # [11]
print(hsh.search("country", "Egypt"))   # [19, 28, 35]
print(hsh.search("name", "lyla"))   # should print []
# ** save and load ** #
SL.save(admin)
# check file:  users_data.json to check data base
# run file: load_test.py to test loading


