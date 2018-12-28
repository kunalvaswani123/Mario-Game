from board import Board as createboard	

class Person(createboard):
	
	def spawnplayer(self,positionx,positiony):
		j=positionx
		i=positiony
		self.grid[i][j]="@"
		self.grid[i+1][j]="/"
		self.grid[i][j+1]="@"
		self.grid[i+1][j+1]="\\"

	def spawnenemy(self,positionx,positiony):
		j=positionx
		i=positiony
		self.grid[i][j]=chr(177)
		self.grid[i+1][j]=chr(9608)
		self.grid[i][j+1]=chr(177)
		self.grid[i+1][j+1]=chr(9608)

	def spawnboss(self,positionx,positiony):
		j=positionx
		i=positiony
		for x in range(j,j+3):
			self.grid[i][x]=chr(9608)
		for x in range(i+1,i+3):
			for y in range(j+1,j+4):
				self.grid[x][y]=chr(9608)
		self.grid[i+3][j+1]=chr(9608)
		self.grid[i+3][j+3]=chr(9608)

class Player(Person):

	def __init__(self,playerx,playery):
		self.playerx=playerx
		self.playery=playery
	
	def spawn(self):
		self.spawnplayer(self.playerx,self.playery)

class Enemy(Person):

	def __init__(self,enemyx,enemyy):
		self.enemyx=enemyx
		self.enemyy=enemyy

	def spawn(self):
		self.spawnenemy(self.enemyx,self.enemyy)

class Boss(Person):

	def __init__(self,enemyx,enemyy):
		self.bossx=bossx
		self.bossy=bossy

	def spawn(self):
		self.spawnboss(self.bossx,self.bossy)
