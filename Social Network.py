class User:
	def__init__(self, username):
		self.username = username
		self.id = Id
		self.connections = []

	def editUsername(newUsername):
		self.name = newUsername

	def getUsername(self):
		return self.username


	def getUserID(self):
		return self.id

	
	def addConnection(self,connectionId):
		self.connections.append(connectionId)

	def getConnection(self):
		return self.connections


class Network:
	def __init__(self):
		self.users = []

	
	def addUser(self, username):
		for user in self.users:
			if username == user.getUserName():
				print("Sorry that name is taken. Try another name.")
				return 
		
		Id = len(self.users)
		self.users.append(User(username,Id))

		
	def numUsers(self):
		return len(self.users)

	def getUserId(self,username):
		Id = -1
		for user in self.users:
			if username == user.getUsername():
				Id = user


	def addConnection(self, user1, user2):
		user1ID = self.getUserID(user1)
		user2ID = self.getUserID(user2)

		user1 = self.users[user1ID]
		user2 = self.users[user2ID]


		if(user1ID == -1 or user2ID == -1):
			print("One or more usernames aren't correct. Please try again.")

		elif(user1ID == user2ID):
			print("Connections must be made between two different users. Please try again.")

		elif(user2ID in user1.getConnection()):
			print("You({}) are already connected with {}" .format(user1.getUsername(), user2.getUsername()))

		else:
			self.users[user1ID].addConnection(user2ID)
			self.users[user2ID].addConnection(user1ID)
		return True

	def printUsers(self):
		print("Social Network Users\t")
		for user in self.users:
			print("User {} : {}" .format(user.getUserName(), user.getUserID()))


	def allConnections(self, username):
		user = self.users[self.getUserID(username)]
		connections = user.getConnections()
		print("{}'s Connections : " .format(user.getUserName()))
		for friends in connection:
			friend = self.users[friends]
			print("\t{}" .format(friend.getUsername()))

	def main():
		mynetwork = Network()
    	done = False
    	while not done:
        	action = input("""\nWhat would you like to do?
            	Add a user (u), print users (p),
            	add connection (c), print connections (pc),
            	quit (q)?
            	""")

        	if action == "p":
            	mynetwork.printUsers()
        	elif action == "u":
            	username = input("What username? ")
            	mynetwork.addUser(username)               
        	elif action == "pc":
            	user = input("For which user? ")
            	mynetwork.printConnections(user)
        	elif action == "c":
            	if mynetwork.numUsers() < 2:
                	print("You need at least two users to make a connection.")
                	continue
            	user1 = input("First username: ")
            	user2 = input("Second username: ")
            	mynetwork.addConnection(user1, user2)
        	elif action == "q":
            	print("Sorry to see you go so soon!")
            	break
        	else:
            	print("Sorry, I didn't understand that.")
