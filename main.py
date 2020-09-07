# This is a test about, Creating recommendation system with Python with little our data in data folder!
# My simple user data set
import data.users as data
import functions.fun as sysFun
users = data.users
secondryUsers = data.secondryUsers

# -------------------------TESTING SECTION-------------------------
# Manhattan description:
# When will we use from Manhattan distance?
# When we have all data with out skow nad losing data
# When all our data is full complete.
# try:
#     getManhattan = sysFun.manhattanDistance(users['Chan'], users['Dan']) # will return 14
#     print(getManhattan)
# except:
#     print("Error!!")

# -------------------------TESTING SECTION-------------------------
# one user to any users compare
# distances = sysFun.listRecommendation(users, 'Dan')
# user = 0
# rate = 1
# for i in distances:
#     print(i[0], i[1])

# Both of the two above functions have a skow data and lose a lot or little data for any users
# if one user as A has {a, b, c, d, e} and user B has {a, f, g, d, e}, we have only two same parameter
# in between and lose {c, d, f, g} this is bad way
# When Manhattan distance works as well, it has same data in per parameters

# Between time we will have Minkowski formula for doing that is true and we found following function:


# -------------------------MINKOWSKI (GENERALIZATION FORM) TESTING SECTION 1--------------

# minkowski = sysFun.minkowski(users['Chan'], users['Dan'], 5)
# print(minkowski)

# -------------------------MINKOWSKI (GENERALIZATION FORM) TESTING SECTION 2--------------
#
# minkowski = sysFun.listMinkowskiRecommendation(users, 'Dan')
# print(minkowski)

# ------------------------PEARSON ALGORITHM SECTION 1---------------
# print(len(users['Veronica']))
# print(sysFun.pearsonRecommedation(secondryUsers['Chan'], secondryUsers['Dan']))
