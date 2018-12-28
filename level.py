from move import game

class level1(game):

	def __init__(self,playerx,playery,levelno):
		game.__init__(self,playerx,playery)
		self.levelno=levelno

	def display(self):
		cloudtype=0
		for i in range(40,740,30):
			if cloudtype is 1:
				self.create_small_cloud(i,12)
				cloudtype=0
			else:
				self.create_big_cloud(i,10)
				cloudtype=1
		coins_1={30,47,53}
		blocks_1={44,50,56}
		for coins in coins_1:
			self.createcoins(coins,31)
		for blocks in blocks_1:
			self.createblocks(blocks,31,1,2)
		self.createcoins(50,26)
		self.createpipes_small(90,33)
		self.createpipes_big(140,31)
		self.createpipes_big(180,31)
		self.createvalley(210,36)
		self.createvalley(270,36)
		self.createcoins(230,29)
		self.createblocks(240,23,1,20)
		self.createblocks(270,23,1,20)
		self.createcoins(290,23)
		self.createcoins(290,29)
		self.createblocks(310,29,1,10)
		self.createcoins(340,29)
		self.createcoins(350,29)
		self.createcoins(360,29)
		self.createcoins(350,23)
		self.createvalley(380,36)
		self.createpipes_big(385,31)
		self.createpipes_big(460,31)
		self.createvalley(470,36)

		''' view of SSAD ''' 

		self.createblocks(400,26,2,2)
		self.createblocks(408,27,3,2)
		self.createblocks(403,27,1,3)
		self.createblocks(405,27,1,3)
		self.createblocks(400,24,1,10)
		self.createblocks(400,31,1,7)
		self.createblocks(408,31,1,2)

		self.createblocks(414,26,2,2)
		self.createblocks(422,27,3,2)
		self.createblocks(417,27,1,3)
		self.createblocks(419,27,1,3)
		self.createblocks(414,24,1,10)
		self.createblocks(414,31,1,7)
		self.createblocks(422,31,1,2)

		self.createblocks(428,31,1,2)
		self.createblocks(430,29,1,1)
		self.createblocks(431,25,3,1)
		self.createblocks(433,24,1,2)
		self.createblocks(436,25,3,1)
		self.createblocks(437,29,1,1)
		self.createblocks(430,28,0,5)
		self.createblocks(438,31,1,2)

		self.createblocks(443,24,8,2)
		self.createblocks(445,24,1,6)
		self.createblocks(445,31,1,6)
		self.createblocks(452,25,6,2)

		''''''
		
		self.createcoins(500,30)
		self.createblocks(505,25,1,15)
		self.createblocks(525,25,1,7)
		self.createcoins(532,25)
		self.createblocks(535,25,1,7)
		self.createblocks(529,30,1,10)
		self.createcoins(529,30)
		self.createstairs(575,35)
		self.createvalley(584,36)
		self.createstairs_reverse(590,35)
		self.createstairs(650,35)
		self.createstairs_reverse(665,35)	

		'''end game:'''

		self.createcoins(700,30)
		self.createblocks(709,30,1,4)
		self.createblocks(740,33,0,8)
		self.grid[34][744]=chr(9608)
		self.grid[35][744]=chr(9608)
		
		self.createstairs(750,35)
		self.createstairs(759,27)
		self.createblocks(759,27,8,8)
		self.createblocks(800,5,20,60)
		self.createflag(872,28)