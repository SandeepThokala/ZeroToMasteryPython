#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
Player = {'age': 16, 'username': 'Shikamaru', 'weapons': ['Shadow Possesssion Jutsu', 'Analytical Skill'], 'is_active': True, 'clan': 'Nara'}

#2 iterate and print all the keys in the above user.
for i in Player.keys():
	print(i)

#3 Add a new weapon to your user.
Player['weapons'].append('Asuma\'s Blades')
print(Player)

#4 Add a new key to include 'is_banned'. Set it to false
Player['is_banned'] = False
print(Player)

#5 Ban the user by setting the previous key to True
Player['is_banned'] = True
print(Player)

#6 create a new user2 my copying the previous user and update the age value and username value. 
Player2 = Player.copy().update(age = 19, username = 'Shikamaru Nara')
print(Player2)