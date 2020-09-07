# Peer 2 Peer compare in Manhattan model distance
def manhattanDistance(user1, user2):
    # Distance for putting sum of distance between two users with key: value sets
    distance = 0
    for key in user1:
        # If any keys of user1 will be in keys of user2
        if key in user2:
            distance += abs(user1[key] - user2[key])
    return distance


# one user to any users compare
def listRecommendation(users, username):
    # Create an array to save our users distance with name and their distance
    distances = []
    for user in users:
        if user != username:
            distance = manhattanDistance(users[user], users[username])
            distances.append((user, distance))
    distances.sort()
    return distances


# Both of the two above functions have a skow data and lose a lot or little data for any users
# if one user as A has {a, b, c, d, e} and user B has {a, f, g, d, e}, we have only two same parameter
# in between and lose {c, d, f, g} this is bad way
# When Manhattan distance works as well, it has same data in per parameters

# Between time we will have Minkowski formula for doing that is true and we found following function:

def minkowski(user1, user2, r):
    distance = 0
    for key in user1:
        if key in user2:
            distance += pow(abs(user1[key] - user2[key]), r)
    finalOperation = pow(distance, 1 / r)
    return finalOperation


# one user to any users compare in case of minkowskey
def listMinkowskiRecommendation(users, username):
    # Create an array to save our users distance with name and their distance
    distances = []
    for user in users:
        if user != username:
            distance = minkowski(users[user], users[username], 2)
            distances.append((user, distance))
    distances.sort()
    return distances


# Sometimes we cann't use from some algorithm like Minkowski or Manhattan or etc
# because some users may be uncurrect rate to any music albums or any product
# so we use form Pearson algorithm

# Section of of Pearson Algorithm
# In the top of div
def getMultiplicationPearson(user1, user2):
    distance = 0
    for key in user1:
        if key in user2:
            distance += abs(user1[key] * user2[key])
    return distance

def getDummy(user1, user2):
    distance = 0
    user1Sum = 0
    user2Sum = 0
    countThingUser1 = 0
    countThingUser2 = 0
    for key in user1:
        if key in user2:
            user1Sum += user1[key]
            countThingUser1 += 1

    for key in user2:
        if key in user1:
            user2Sum += user2[key]
            countThingUser2 += 1

    if countThingUser1 == countThingUser2:
        distance = (user1Sum * user2Sum) / countThingUser1
    else:
        distance = 0
        return distance

    return distance

# In the bottom of div
def usersBottom(user):
    userSumSection1 = 0
    userSumSection2 = 0
    for key in user:
        userSumSection1 += pow(abs(user[key]), 2)

    for key in user:
        userSumSection2 += abs(user[key])

    userSumSection2 = pow(userSumSection2, 2) / len(user)

    final = userSumSection1 - userSumSection2
    pow(final, 1/2)
    return final


# Main function of Pearson to link any section of formula
def pearsonRecommedation(user1, user2):
    # Getting section one for two (users)
    # Top is صورت
    userMulti = getMultiplicationPearson(user1, user2)
    userDummy = getDummy(user1, user2)

    finalTop = userMulti - userDummy
    # Bottom is مخرج
    bottomUser1 = usersBottom(user1)
    bottomUser2 = usersBottom(user2)

    finalBottom = bottomUser1 * bottomUser2
    # The Final Result is
    result = finalTop / finalBottom

    return result