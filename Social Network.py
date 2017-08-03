class User:
	def__init__(self, username):
		self.username = username
		self.id = Id
		self.connections = []

	def editUsername(newUsername):
		self.name = newUsername

	def getUsername(self):
		return self.username


	def getId(self):
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



IdList = []

def main():
