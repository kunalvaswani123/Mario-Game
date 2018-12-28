class Board:
    currentindex=0
    last_checkpoint=5
    score=0
    lives=3
    bonus=0
    quit=0
    enemy_kill=0
    bullet_kill=[0,0]
    grid=[[] for i in range(0,40)]
    _border=[]
    _floor=[]
    for i in range(0,1100):
        _floor.append(chr(9608))
    for i in range(0,40):
        for j in range(0,1100):
            if i >= 36 : 
                grid[i]=_floor[:]
            else:
                grid[i].append(' ')
    screen=[[] for i in range(0,40)]
    for i in range(0,40):
        for j in range(0,100):
            screen[i].append(grid[i][j])
    def slidegridright(self):
        tempcurrentindex=self.currentindex
        for i in range(0,100):
            for j in range(0,40):
                self.screen[j][i]=self.grid[j][tempcurrentindex+1]
            tempcurrentindex+=1 
        self.currentindex+=1
    def slidegridleft(self):
        tempcurrentindex=self.currentindex
        if tempcurrentindex != 0:
            for i in range(0,100):
                for j in range(0,40):
                    self.screen[j][i]=self.grid[j][tempcurrentindex-1]
                tempcurrentindex+=1 
            self.currentindex-=1
    def printgrid(self):
        tempcurrentindex=self.currentindex
        for i in range(0,100):
            for j in range(0,40):
                if i is 2 and j is 2:
                    self.screen[j][i]="Score: "+str(self.score)
                elif i is 2 and j is 3:
                    self.screen[j][i]="Lives Left: "+str(self.lives)
                elif i is 2 and j is 4:
                    self.screen[j][i]="Bonus: "+str(self.bonus)
                else:
                    self.screen[j][i]=self.grid[j][tempcurrentindex]
            tempcurrentindex+=1 
        for i in range(0,40):
            temprow=[]
            for j in range(0,100):
                temprow.append(self.screen[i][j])
            print(''.join(temprow))
