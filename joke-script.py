

import os
import random
import pickle


print("\t\t\t\t\t************************* Let's PLAYYYYYYYY in loop ****************************\n")
print("\t\t /\/\/\/\/\/\/\/\/\/\_____ ")
print("\t\t /\/\/\/\/\/\/\/\/\/\_____ ")
print("\t\t /\/\/\/\/\/\/\/\/\/\_____ ")




# creation of the file if it's existed yet and get all content 

dUsers = {}
try:
	with open('theUsers.pkl', 'rb') as t:
		userLoaded = pickle.load(t)
		dUsers = userLoaded
except:
	defautUser = {"negre-man" : 1}
	with open('theUsers.pkl', 'wb') as f:
		pickle.dump(defautUser, f)
		f.close()
	
	with open('theUsers.pkl', 'rb') as tt:
		userLoaded = pickle.load(tt)
		dUsers = userLoaded
	









computerValue = random.choice([3, 8, 15, 21, 26, 30, 31, 35, 37, 41, 44, 49])
uservalue = 0
userValueEntered = 0

# treatment about the nickname
userName = ""
score = 0
name = input("\t\t Enter your name before playing with us: \t")
nameTest = 0
while(nameTest == 0):
	if(len(name) == 0):
		print("\t\t\t You've entered nothing... \n ")
		name = input("\t\t Reentering...  \t")
		nameTest = 0
		continue
	else:	
		for char in name:
			if(char.isspace()):
				print("\t\t\t You've entered something containing \' SPACE\' \n ")
				name = input("\t\t Reentering...  \t")
				nameTest = 0
				break
			elif(char.isupper()):
				print("\t\t\t You've entered something with \' UPPERCASE\' \n ")
				name = input("\t\t Reentering...  \t")
				nameTest = 0
				break
			else:
				userName = name
				nameTest = 1
				
				
				

# Let's see if the user is already registered... Then, if yes, get his or her score
newUser = True
for user in dUsers.keys():	
	if user == userName:		
		print("\n\t\t\t\t Good to see you again ", userName)	
		newUser = False

if(newUser == False):
	score = dUsers[userName]
else:
	score = score
	print("\n\t\t\t\t Happy in having you {0} for the first time ".format(userName))
			

		
# getting values from users
print("\t\t .......")
print("\t\t .......")

valueStay = "stay"  
chance = 5
print("\t\t\t\t|_____________________ ************New Playing... \n\n")

while((valueStay != "k") and (valueStay !="K")):
	test1 = 0
	while test1 == 0:
		print("\t\t ....... Choose your expected number \n")
		try:
			userValueEntered = int(input("\t\t\t Between 3 and 49: \t"))
			test1 = 1
		except:
			print("\n\t\t\t~~~~~~~~~~You didn't enter un numeric... \n")
			test1 = 0
	
	while((userValueEntered < 3) or (userValueEntered > 49)):
		test = 0
		while test == 0:
			print("\t\t Bad value entered \n \t\t Get another one \n ")
			try:
				userValueEntered = int(input("\t\t\t Between 3 and 49: \t"))
				test = 1
			except:
				print("\n\t\t\t~~~~~~~~~~You didn't enter un numeric... \n")
				test = 0
	
	uservalue = userValueEntered
	
	if (computerValue > uservalue):
		print("\n\t\t The value entered is smaller")
		print("\t\t\t _______________ BAD choice ", userName)
		print("\t\t\t score: ", score)
		chance -= 1
		if(chance > 0):
			print("\n\t\t\tchance : ", chance)
			continue
	elif(uservalue > computerValue):
		print("\n\t\t The value entered is greater")
		print("\t\t\t _______________ BAD choice ", userName)
		print("\t\t\t score: ", score)
		chance -= 1 
		if(chance > 0):
			print("\n\t\t\tchance : ", chance)
			continue
		
	else:
		print("\n\t\t\t /\/\//\/\/\/_________ CONGRATULATION ", userName)
		score += 1
		print("\n\t\t\t score: ", score)
		computerValue = random.choice([3, 8, 15, 21, 26, 30, 31, 35, 37, 41, 44, 49])   # to get another random value
		if(chance > 0):
			print("\n\t\t\tchance : ", chance)
			continue
	
	
	
	if(chance < 1 ):
		print("\n\t\t\t___________ {0}, your all chances are over !!!".format(userName))
		print("\n\t\t\t___________final score: ", score)
		print("\n\t\t /\/\/\/\/\/\/\ --------- The computer value is {0} -------------/\/\/\/\/\/\/\/\/".format(computerValue))
		
		# updating the dictionnary
		if userName in dUsers.keys():	
			dUsers[userName] = score    #score updated
		else:
			dUsers.update({userName: score}) 	# adding as new user


		# updating of the file in removing the first one and create another in same name
		#dUsers1 = {}
		# 1__ Removing
		os.remove("theUsers.pkl")
		# another one in the same name
		
		with open('theUsers.pkl', 'wb') as f:
			pickle.dump(dUsers, f)
			f.close()
		
		

		valueStay = input("\n\t\t To keep continue, 'press anything', to quit, just -----> 'k' or 'K'\t")
		if((valueStay != "k") and (valueStay != "K")):
			print("\n\t\t Great to keep continue ", userName) 
			chance = 5
			print("\n\t\t\tchance : ", chance)
		else:
			print("\n\t\t\t Waiting for you {0} another time".format(userName))










