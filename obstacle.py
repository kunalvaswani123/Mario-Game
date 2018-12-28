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

	def createpipes(self,pipex,pipey):
		for j in range(pipex,pipex+10):
			self.grid[pipey][j]=chr(9608)

		for i in range(1,5):
			for j in range(pipex+2,pipex+8):
				self.grid[pipey+i][j]=chr(9608)

	def createstairs(self,stairx,stairy):
		k=stairx
		for i in range(0,5):
			for j in range(k,stairx+5):
				self.grid[stairy-i][j]=chr(9608)
			k+=1

	def createstairsr(self,stairx,stairy):
		k=stairx+5
		for i in range(0,5):
			for j in range(stairx,k):
				self.grid[stairy-i][j]=chr(9608)
			k-=1

	def create_small_cloud(self,s_cloudx,s_cloudy):
		self.grid[s_cloudy][s_cloudx]="\\"
		self.grid[s_cloudy][s_cloudx+2]="/"
		self.grid[s_cloudy][s_cloudx+1]="__"
		self.grid[s_cloudy-1][s_cloudx+3]="\\"
		self.grid[s_cloudy-1][s_cloudx]="/"
		self.grid[s_cloudy-2][s_cloudx+1]="__"
	
	def create_big_cloud(self,b_cloudx,b_cloudy):
		self.grid[b_cloudy][b_cloudx]="\\"
		self.grid[b_cloudy-1][b_cloudx-1]="\\"
		self.grid[b_cloudy-2][b_cloudx-1]="/"
		self.grid[b_cloudy-3][b_cloudx]="/"
		self.grid[b_cloudy][b_cloudx+2]="/"
		self.grid[b_cloudy][b_cloudx+1]="________"
		self.grid[b_cloudy-1][b_cloudx+10]="/"
		self.grid[b_cloudy-2][b_cloudx+10]="\\"
		self.grid[b_cloudy-3][b_cloudx+9]="\\"
		self.grid[b_cloudy-4][b_cloudx+1]="________"
			



