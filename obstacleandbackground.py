from board import Board as createboard

class Obstacle(createboard):

	def createblocks(self,obstaclex,obstacley,length,height):
		i=obstacley
		finalj=obstaclex+height
		finali=obstacley+length
		while i<=finali:
			j=obstaclex
			while j<=finalj:
				self.grid[i][j]=chr(9608)
				j+=1
			i+=1

	def createcoins(self,coinx,coiny):
		i=coiny
		finalj=coinx+2
		finali=coiny+1
		while i<=finali:
			j=coinx
			while j<=finalj:
				self.grid[i][j]='?'
				j+=1
			i+=1	

	def createpipes_small(self,pipex,pipey):
		for j in range(pipex,pipex+10):
			self.grid[pipey][j]=chr(9608)

		for i in range(1,3):
			for j in range(pipex+2,pipex+8):
				self.grid[pipey+i][j]=chr(9608)

	def createpipes_big(self,pipex,pipey):
		for j in range(pipex,pipex+10):
			self.grid[pipey][j]=chr(9608)

		for i in range(1,5):
			for j in range(pipex+2,pipex+8):
				self.grid[pipey+i][j]=chr(9608)

	def createstairs(self,stairx,stairy):
		k=stairx
		for i in range(0,8):
			for j in range(k,stairx+9):
					self.grid[stairy-i][j]=chr(9608)
			if i%2 is 1:
				k+=2

	def createstairs_reverse(self,stairx,stairy):
		k=stairx+9
		for i in range(0,8):
			for j in range(stairx,k):
				self.grid[stairy-i][j]=chr(9608)
			if i%2 is 1:
				k-=2

	def create_small_cloud(self,s_cloudx,s_cloudy):
		self.grid[s_cloudy][s_cloudx]="\\"
		self.grid[s_cloudy][s_cloudx+3]="/"
		self.grid[s_cloudy][s_cloudx+1]="_"
		self.grid[s_cloudy][s_cloudx+2]="_"
		self.grid[s_cloudy-1][s_cloudx+3]="\\"
		self.grid[s_cloudy-1][s_cloudx]="/"
		self.grid[s_cloudy-2][s_cloudx+1]="_"
		self.grid[s_cloudy-2][s_cloudx+2]="_"
	
	def create_big_cloud(self,b_cloudx,b_cloudy):
		self.grid[b_cloudy][b_cloudx]="\\"
		self.grid[b_cloudy-1][b_cloudx-1]="\\"
		self.grid[b_cloudy-2][b_cloudx-1]="/"
		self.grid[b_cloudy-3][b_cloudx]="/"
		self.grid[b_cloudy][b_cloudx+6]="/"
		for i in range(1,6):
			self.grid[b_cloudy][b_cloudx+i]="_"
		self.grid[b_cloudy-1][b_cloudx+7]="/"
		self.grid[b_cloudy-2][b_cloudx+7]="\\"
		self.grid[b_cloudy-3][b_cloudx+6]="\\"
		for i in range(1,6):
			self.grid[b_cloudy-4][b_cloudx+i]="_"
			
	def createvalley(self,valley_x,valley_y):

		finish_1=valley_x+5
		start_2=valley_y
		finish_2=valley_y+3
		while start_2<=finish_2:
			start_1=valley_x
			while start_1<=finish_1:
				self.grid[start_2][start_1]=" "
				start_1+=1
			start_2+=1
	
	def createmountains(self,startx,starty):

		count=0
		self.grid[starty][startx]="*"
		for i in range(starty,starty+7):
			for j in range(startx-count,startx+count+1):
				self.grid[i][j]="*"
			count+=1

	def createflag(self,startx,starty):

		for i in range(starty,starty+8):
			self.grid[i][startx]=chr(9608)
		self.createblocks(startx+1,starty,2,8)