from person import Player as player
from person import Enemy as enemy
from person import Boss as boss
from obstacleandbackground import Obstacle as obstacle
import time

class game(player,obstacle):

	def __init__(self,playerx,playery):
		player.__init__(self,playerx,playery)

	def deleteplayer(self):
		self.grid[self.playery][self.playerx]=' '
		self.grid[self.playery+1][self.playerx]=' '
		self.grid[self.playery][self.playerx+1]=' '
		self.grid[self.playery+1][self.playerx+1]=' '

	def moveforward(self):
		self.deleteplayer()
		if self.grid[self.playery][self.playerx+2] == chr(9608):
			pass
		elif self.grid[self.playery+1][self.playerx+2] == chr(9608):
			pass
		elif self.grid[self.playery][self.playerx+2] == '?':
			pass
		elif self.grid[self.playery+1][self.playerx+2] == '?':
			pass
		else:
			self.playerx+=1
		self.spawn()

	def movebackward(self):
		self.deleteplayer()
		if self.playerx <= 1:
			pass
		else:
			if self.grid[self.playery][self.playerx-1] == chr(9608):
				pass
			elif self.grid[self.playery+1][self.playerx-1] == chr(9608):
				pass
			elif self.grid[self.playery][self.playerx-1] == '?':
				pass
			elif self.grid[self.playery+1][self.playerx-1] == '?':
				pass
			else:
				self.playerx-=1				
		self.spawn()

	def jumpup(self,val):
		self.deleteplayer()
		flag=0
		if self.grid[self.playery+2][self.playerx] in {chr(9608),'?'}:
			flag=1
		if self.grid[self.playery+2][self.playerx+1] in {chr(9608),'?'}:
			flag=1
		if flag is 1:
			for i in range(0,val):
				if self.grid[self.playery-1][self.playerx] == chr(9608):
					break
				if self.grid[self.playery-1][self.playerx+1] == chr(9608):
					break
				if self.grid[self.playery-1][self.playerx] is '?':
					self.bonus+=50
					j=self.playerx-2
					finalj=self.playerx+2
					while j<=finalj:
						if self.grid[self.playery-1][j] is '?':
							self.grid[self.playery-1][j]=chr(9608)
							self.grid[self.playery-2][j]=chr(9608)
						j+=1
					self.grid[self.playery-3][self.playerx]='0'
					self.printgrid()
					time.sleep(0.1)		
					self.grid[self.playery-3][self.playerx]=' '
					break
				if self.grid[self.playery-1][self.playerx+1] is '?':
					self.bonus+=50
					j=self.playerx+1
					finalj=self.playerx+3
					while j<=finalj:
						if self.grid[self.playery-1][j] is '?':
							self.grid[self.playery-1][j]=chr(9608)
							self.grid[self.playery-2][j]=chr(9608)
						j+=1
					self.grid[self.playery-3][self.playerx+1]='0'
					self.printgrid()
					time.sleep(0.1)		
					self.grid[self.playery-3][self.playerx+1]=' '
					break								
				self.playery-=1
		self.spawn()

	def fall(self):
		self.deleteplayer()
		if self.grid[self.playery+2][self.playerx] == chr(9608):
			pass
		elif self.grid[self.playery+2][self.playerx+1] == chr(9608):
			pass
		elif self.grid[self.playery+2][self.playerx] == '?':
			pass
		elif self.grid[self.playery+2][self.playerx+1] == '?':
			pass
		else:
			self.playery+=1
		if self.grid[self.playery+1][self.playerx] is chr(177):
			self.enemy_kill=1
		if self.grid[self.playery+1][self.playerx+1] is chr(177):
			self.enemy_kill=1
		if self.grid[self.playery+1][self.playerx-1] is chr(177):
			self.enemy_kill=1
		self.spawn()
		if self.playery>=37:
			self.quit=1
	
	def spawnbullet(self,bulletx,bullety):
		self.grid[bullety][bulletx]="o"
		
class moveenemy(enemy):

	direction=1
	def __init__(self,enemyx,enemyy):
		self.enemyx=enemyx
		self.enemyy=enemyy

	def deleteenemy(self):
		self.grid[self.enemyy][self.enemyx]=' '
		self.grid[self.enemyy+1][self.enemyx]=' '
		self.grid[self.enemyy][self.enemyx+1]=' '
		self.grid[self.enemyy+1][self.enemyx+1]=' '

	def move(self):

		if self.grid[self.enemyy][self.enemyx+2] in {chr(9608),'?','*'}:		
			self.direction=0
		elif self.grid[self.enemyy+1][self.enemyx+2] in {chr(9608),'?','*'}:		
			self.direction=0
		elif self.grid[self.enemyy][self.enemyx-1] in {chr(9608),'?','*'}:
			self.direction=1
		elif self.grid[self.enemyy+1][self.enemyx-1] in {chr(9608),'?','*'}:
			self.direction=1

		if self.grid[self.enemyy][self.enemyx+2] is '@':		
			self.quit=1
		elif self.grid[self.enemyy+1][self.enemyx+2] in {'\\','/'}:		
			self.quit=1
		elif self.grid[self.enemyy][self.enemyx-1] is '@':
			self.quit=1
		elif self.grid[self.enemyy+1][self.enemyx-1] in {'\\','/'}:
			self.quit=1
		elif self.grid[self.enemyy][self.enemyx+1] is '@':		
			self.quit=1
		elif self.grid[self.enemyy+1][self.enemyx+1] in {'\\','/'}:		
			self.quit=1
		elif self.grid[self.enemyy][self.enemyx] is '@':
			self.quit=1
		elif self.grid[self.enemyy+1][self.enemyx] in {'\\','/'}:
			self.quit=1
		else:	
			if self.direction is 1:
				self.enemyx+=1
			else:
				self.enemyx-=1

		if self.grid[self.enemyy][self.enemyx+2] is 'o':
			self.bullet_kill[0]=1
			self.bullet_kill[1]=self.enemyx
		elif self.grid[self.enemyy][self.enemyx-1] is 'o':
			self.bullet_kill[0]=1
			self.bullet_kill[1]=self.enemyx

class moveboss(boss):

	health=10
	direction=1
	def __init__(self,bossx,bossy):
		self.bossx=bossx
		self.bossy=bossy

	def deleteboss(self):
		j=self.bossx
		i=self.bossy
		for x in range(j,j+3):
			self.grid[i][x]=' '
		for x in range(i+1,i+3):
			for y in range(j+1,j+4):
				self.grid[x][y]=' '
		self.grid[i+3][j+1]=' '
		self.grid[i+3][j+3]=' '

	def move(self):
		
		self.deleteboss()
		j=self.bossx
		i=self.bossy
		if self.bossy>=32:
			self.direction=0
		elif self.bossy<=26:
			self.direction=1

		if self.direction is 1:
			self.bossy+=1
		else:
			self.bossy-=1
		self.spawn()

	def checkbullets(self):

		j=self.bossx
		i=self.bossy
		if self.grid[i][j-1] is 'o':
			self.health-=1
		if self.grid[i+1][j] is 'o':
			self.health-=1
		if self.grid[i+2][j] is 'o':
			self.health-=1
		if self.grid[i+3][j] is 'o':
			self.health-=1
		if self.grid[i][j+3] is 'o':
			self.health-=1
		if self.grid[i+1][j+4] is 'o':
			self.health-=1
		if self.grid[i+2][j+4] is 'o':
			self.health-=1
		if self.grid[i+3][j+4] is 'o':
			self.health-=1
		if self.grid[i][j-1] is '@':
			self.quit=1
		if self.grid[i+1][j] is '@':
			self.quit=1
		if self.grid[i+2][j] is '@':
			self.quit=1
		if self.grid[i+3][j] is '@':
			self.quit=1
		if self.grid[i][j+3] is '@':
			self.quit=1
		if self.grid[i+1][j+4] is '@':
			self.quit=1
		if self.grid[i+2][j+4] is '@':
			self.quit=1
		if self.grid[i+3][j+4] is '@':
			self.quit=1		
		if self.grid[i+3][j+1] is '@':
			self.quit=1		
		if self.grid[i+3][j+2] is '@':
			self.quit=1		
		