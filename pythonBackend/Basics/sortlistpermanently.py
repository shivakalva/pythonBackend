users = ['val', 'bob', 'mia', 'ron', 'ned']
first_user = users[0]
newest_user = users[-1]
#check = users.sort()
print(first_user)
print(newest_user)
###########################################################
users.append('bob')
users.append('mia')
###########################################################
users.insert(0, 'joe')
users.insert(3, 'bea')
###########################################################
users.sort()  # Sorting a list permanently
print(users)
###########################################################
#Sorting a list permanently in reverse alphabetical order
users.sort(reverse=True)
print(users)
###########################################################
#Sorting a list temporarily
print(sorted(users))
print(sorted(users, reverse=True))
###########################################################














