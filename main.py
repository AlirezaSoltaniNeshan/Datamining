# This is a test about, Creating recommendation system with Python with little our data in data folder!
# My simple user data set

import data.users as data
import functions.fun as sysFun
# users = data.users
users = data.secondryUsers

# -------------------------TESTING SECTION-------------------------
# try:
#     getManhattan = sysFun.manhattanDistance(users['Chan'], users['Dan']) # will return 14
#     print(getManhattan)
# except:
#     print("Error!!")

# one user to any users compare
# -------------------------TESTING SECTION-------------------------
# distances = sysFun.listRecommendation(users, 'Dan')
# user = 0
# rate = 1
# for i in distances:
#     print(i[0], i[1])

# -------------------------MINKOWSKI TESTING SECTION 1--------------

# minkowski = sysFun.minkowski(users['Chan'], users['Dan'], 5)
# print(minkowski)

# -------------------------MINKOWSKI TESTING SECTION 2--------------
#
# minkowski = sysFun.listMinkowskiRecommendation(users, 'Dan')
# print(minkowski)

# print(len(users['Veronica']))

# print(sysFun.pearsonRecommedation(users['Clara'], users['Dan']))
