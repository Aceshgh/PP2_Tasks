# ---Booleans---
# print(10>9)    =true
# print(10==9)   =false
# print(10<9)    =false

# -
# aA = 199
# bB = 198

# if bB > aA:
#   print("bB is greater than aA")
# else:
#   print("bB is not greater than aA")     =bB is not greater than aA

# -
# x = "Goodbye"
# y = 100

# print(bool(x))   =true
# print(bool(y))   =true

# -
# def function() :
#   return True

# if function():
#   print("YES")
# else:
#   print("NO")    =YES






# ---Operators---
# print((15 - 5) + (25 - 10))   =25
# -
# print(150 + 10 * 10)   =250
# -
# print(20 + 15 - 22 + 4)   =17







# ---Lists---
# listd = ["Monday", "Tuesday", "Wednesday", "Thursday"]
# print(listd)   =["Monday", "Tuesday", "Wednesday", "Thursday"]

# -
# listd = ["Monday", "Tuesday", "Wednesday", "Thursday"]
# print(len(listd))   =4

# -
# listf = ["EAAAAA", 66, True, 6, "AAARRGGGHHHHHH"]
# print(listf)   =["EAAAAA", 66, True, 6, "AAARRGGGHHHHHH"]

# -
# thislist = list(("LALA", "NANA", "DADA"))
# print(thislist)   =["LALA", "NANA", "DADA"]

# -
# thatlist = ["SEL", "MEDVED", "VMACHINU"]
# print(thatlist[-1])   =VMACHINU

# -
# thislist = ["ODNAZHDIY", "HEMENGUIEI", "POSPORIL"]
# thislist[1] = "ALBERTEINSTEIN"
# print(thislist)  =["ODNAZHDIY", "ALBERTEINSTEIN", "POSPORIL"]

# -
# fruits = ["KAK", "AKAK", "DAD", "MAD", "ISSON"]
# newlist = []

# for x in XZCHTOETO:
#   if "K" in x:
#     newlist.append(x)
# print(newlist)   =["KAK", "AKAK"]







# ---Tuple---
# Ztuple = ("MANGO", "ManGo", "MANgo")
# print(Ztuple)   =("MANGO", "ManGo", "MANgo")

# -
# Ztuple = ("MANGO", "ManGo", "MANgo")
# print(Ztuple(2))   =MANgo

# -
# x = ("MANGO", "ManGo", "MANgo")
# z = list(x)
# z[1] = "mango"
# x = tuple(z)

# print(x)  =("MANGO", "mango", "MANgo")

# -
# fru = ("app", "ban", "che")

# (gree, yell, re) = fru

# print(gree)   =app
# print(yell)   =ban
# print(re)     =che








# ---Python Sets---
# Goidaset = {"Shel", "MedVed", "POlesu"}
# print(Goidaset)   ={"Shel", "MedVed", "POlesu"}

# -
# sset = {"ap", "ba", "ch"}
# print("ba" not in sset)   =False

# -
# setR = {"app", "ban", "cher"}
# setR.add("ora")
# print(setR)    ={"app","ora", "ban", "cher"}

# -
# setR = {"app", "ban", "cher"}
# setR.remove("app")
# print(setR)    ={"ban", "cher"}

# -
# setR = {"app", "ban", "cher"}
# for Z in setR:
#   print(Z)    = app  ban  cher

# -
# setone = {"ab", "ba", "cc"}
# settwo = {1, 2, 3}

# setthree = setone.union(settwo)
# print(setthree)     ={"ab", 1, "ba", 2, "cc", 3}







# ---Python Dictionaries---
# CarDict = {
#   "brand": "Mersedes"
#   "year": 1980
# }
# print(thisdict)    ={"brand": "Mersedes", "year": 1980}

# -
# CarDict = {
#   "brand": "Mersedes"
#   "year": 1980
# }
# thisdict["year"] = 2018
# print(thisdict)    ={"brand": "Mersedes", "year": 2018}

# -
# CarDict = {
#   "brand": "Mersedes"
#   "year": 1980
# }
# thisdict["color"] = blue
# print(thisdict)    ={"brand": "Mersedes", "year": 2018, "color": "blue"}

# -
# CarDict = {
#   "brand": "Mersedes"
#   "year": 1980
# }
# for x in thisdict.values():
#   print(x)      =Mersedes   1980





#---Python If ... Else---
#a = 33
#b = 200
#if b > a:
#  print("b is greater than a")    = b is greater than a

#-
#a = 200
#b = 33
#if b > a:
#  print("b is greater than a")
#elif a == b:
#  print("a and b are equal")
#else:
#  print("a is greater than b")      = a is greater than b

#-
#a = 2
#b = 330
#print("A") if a > b else print("B")   = B

#-
#x = 41

#if x > 10:
#  print("Above ten,")
#  if x > 20:
#    print("and also above 20!")
#  else:
#    print("but not above 20.")






#---Python While Loops---
#i = 1
#while i < 7:
#  print(i)
#  i += 1     = 1 2 3 4 5 6

#-
#i = 1
#while i < 6:
#  print(i)
#  i += 1
#else:
#  print("i is no longer less than 6")     = 1 2 3 4 5 i is no longer less than 6




#---Python For Loops---
#fruits = ["elppa", "ananab", "yrrehc"]
#for x in fruits:
#  print(x)        = elppa ananab yrrehc

#-
#fruits = ["elppa", "ananab", "yrrehc"]
#for x in fruits:
#  print(x)       
#  if x == "ananab":
#    break             = elppa ananab

#-
#for x in range(2, 6):
#  print(x)             = 2 3 4 5

#-
#for x in range(6):
#  if x == 3: break
#  print(x)
#  else:
#  print("Finally finished!")     = 0 1 2

#-
#adj = ["red", "big", "tasty"]
#fruits = ["apple", "banana", "cherry"]
#
#for x in adj:
#  for y in fruits:
#    print(x, y)
# =
#red apple
#red banana
#red cherry
#big apple
#big banana
#big cherry
#tasty apple
#tasty banana
#tasty cherry