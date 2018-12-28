from getch import _Getch as getinput
from move import game,moveenemy as enemy,moveboss as boss
from level import level1
import signal 
import time

class AlarmException(Exception):
	pass

def alarmhandler(signum, frame):
	raise AlarmException

def user_input(timeout=0.1):
	signal.signal(signal.SIGALRM,alarmhandler)
	signal.setitimer(signal.ITIMER_REAL,timeout)
	try:
		text = getinput()()
		signal.alarm(0)
		return text
	except AlarmException:
		pass
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''

all_mountains=[76,223,261,300,488,559]
all_enemies=[10,102,154,229,412,524,640,723]
all_enemyobjects=[]
deleted_enemies=[]
all_bulletsr=[]
all_bulletsl=[]
quitflag=0
checkpoints=[5,200,370,620,726]

sample=level1(5,34,1)
boss=boss(850,30)

def check_checkpoints():
	for check in checkpoints:
		if sample.playerx >= check:
			sample.last_checkpoint=check

def bounce_on_spring():
	if sample.playerx >= 740 and sample.playerx <=747:
		if sample.playery is 31:
			sample.createblocks(740,34,0,8)
			for i in range(740,749):
				sample.grid[33][i]=" "
	if sample.playerx >= 740 and sample.playerx <=747:
		if sample.playery is 32:
			sample.createblocks(740,35,0,8)
			for i in range(740,749):
				sample.grid[34][i]=" "

def relieve_spring():
	if sample.playerx < 740 or sample.playerx >747:
		flag=0
		for i in range(740,749):
			if sample.grid[34][i] is not " ":
				flag=1
		if flag is 0:
			sample.createblocks(740,34,0,8)
			for i in range(740,749):
				sample.grid[35][i]=" "
			sample.grid[35][744]=chr(9608)
	if sample.playerx < 740 or sample.playerx >747:
		flag=0
		for i in range(740,749):
			if sample.grid[33][i] is not " ":
				flag=1
		if flag is 0:
			sample.createblocks(740,33,0,8)
			for i in range(740,749):
				sample.grid[34][i]=" "
			sample.grid[34][744]=chr(9608)

def boss_check():
	boss.checkbullets()
	if boss.health <= 0:
		boss.deleteboss()
		sample.bonus+=1000
	else:
		boss.move()

def check_enemy_killr():
	for bullet in all_bulletsr:
		sample.grid[bullet[1]][bullet[0]]=' '
		bullet[0]+=1
		if bullet[0]>=900:
			all_bulletsr.remove(bullet)
			continue
		if sample.grid[bullet[1]][bullet[0]] in {chr(9608),'?','*',chr(177)}:
			all_bulletsr.remove(bullet)
			continue
		sample.spawnbullet(bullet[0],bullet[1])

def check_enemy_killl():
	for bullet in all_bulletsl:
		sample.grid[bullet[1]][bullet[0]]=' '
		bullet[0]-=1
		if bullet[0]<=1:
			all_bulletsl.remove(bullet)
			continue
		if sample.grid[bullet[1]][bullet[0]] in {chr(9608),'?','*',chr(177)}:
			all_bulletsl.remove(bullet)
			continue
		sample.spawnbullet(bullet[0],bullet[1])

def create_enemy(object):
	object.deleteenemy()
	object.move()
	object.spawn()

for i in all_enemies:
	all_enemyobjects.append(enemy(i,34))

def introduction():
	for i in range(0,20):
		print()
	for i in range(0,45):
		print(" ",end='')
	print("THE NEW")
	for i in range(0,40):
		print(" ",end='')
	print("SUPER MARIO BROS.")
	for i in range(0,20):
		print()
	time.sleep(2)	

def endwon():
	for i in range(0,20):
		print()
	for i in range(0,47):
		print(" ",end='')
	print("YOU WON!")
	for i in range(0,40):
		print(" ",end='')
	print("YOUR TOTAL SCORE:",end='')
	print(sample.score+sample.bonus)
	for i in range(0,20):
		print()

def endlost():
	for i in range(0,20):
		print()
	for i in range(0,45):
		print(" ",end='')
	print("YOU LOST")
	for i in range(0,40):
		print(" ",end='')
	print("THANKS FOR PLAYING!")
	for i in range(0,20):
		print()

def endquit():
	for i in range(0,20):
		print()
	for i in range(0,45):
		print(" ",end='')
	print("YOU QUIT")
	for i in range(0,40):
		print(" ",end='')
	print("THANKS FOR PLAYING!",end='')
	for i in range(0,20):
		print()

introduction()
sample.display()
sample.spawn()
sample.printgrid()

while sample.lives:
	
	bounce_on_spring()
	check_checkpoints()
	if sample.quit is 1:
		sample.lives-=1
		sample.deleteplayer()
		sample.quit=0	
		for i in range(0,sample.playerx-sample.last_checkpoint):
			sample.slidegridleft()
		sample.playerx=sample.last_checkpoint
		sample.playery=34	
		sample.spawn()
		sample.printgrid()
		continue

	if sample.playerx>=870:
		break

	if boss.quit is 1:
		sample.quit=1
		boss.quit=0
		continue
	
	if boss.health > 0:
		boss_check()

	for mountainindex in all_mountains:
		sample.createmountains(mountainindex,29)
	
	for object_1 in all_enemyobjects:
		create_enemy(object_1)
		if object_1.quit is 1:
			sample.quit=1
			all_enemyobjects.remove(object_1)
			object_1.deleteenemy()
		object_1.quit=0		

	check_enemy_killr()
	check_enemy_killl()

	sample.spawn()
	getchar=user_input()

	if getchar is 'q':
		quitflag=1
		break

	if getchar is 'r':
		all_bulletsr.append([sample.playerx+2,sample.playery])
		sample.spawnbullet(sample.playerx+2,sample.playery)
    
	if getchar is 'e':
		all_bulletsl.append([sample.playerx-1,sample.playery])
		sample.spawnbullet(sample.playerx-1,sample.playery)

	if getchar is 'd':
		temp=sample.playerx
		sample.moveforward()
		if sample.playerx>=50 and temp!=sample.playerx:
			sample.slidegridright()
		if temp!=sample.playerx:
			sample.score+=1
		sample.printgrid()

	if getchar is 'a':
		temp=sample.playerx
		sample.movebackward()
		if sample.playery<50 and temp!=sample.playerx:
			sample.slidegridleft()
		sample.printgrid()

	if getchar is 'w':
		if sample.playerx >= 740 and sample.playerx <=747:
			sample.jumpup(20)
		else:
			sample.jumpup(8)
		sample.printgrid()
		curtime=time.time()
		while(time.time()-curtime<=0.7):
			sample.printgrid()
			getnewchar=user_input()
			if getnewchar is 'd':
				temp=sample.playerx
				sample.moveforward()
				if sample.playerx>=50 and temp!=sample.playerx:
					sample.slidegridright()
			if getnewchar is 'a':
				temp=sample.playerx
				sample.movebackward()
				if sample.playery<50 and temp!=sample.playerx:
					sample.slidegridleft()
			sample.printgrid()
	sample.fall()

	if sample.enemy_kill is 1:
		for object_1 in all_enemyobjects:
			check_1=sample.playerx
			check_2=sample.playerx-1
			check_3=sample.playerx+1
			if object_1.enemyx in {check_1,check_2,check_3}:
				all_enemyobjects.remove(object_1)
				deleted_enemies.append(object_1)
		sample.enemy_kill=0

	if sample.bullet_kill[0] is 1:
		for object_1 in all_enemyobjects:
			if object_1.enemyx is sample.bullet_kill[1]:
				all_enemyobjects.remove(object_1)
				deleted_enemies.append(object_1)
		sample.bullet_kill[0]=0		
	
	sample.printgrid()

	sample.score+=100*len(deleted_enemies)	

	for object_1 in deleted_enemies:
		object_1.deleteenemy()
		deleted_enemies.remove(object_1)
	relieve_spring()

if quitflag is 1:
	endquit()
elif sample.lives is 0:
	endlost()
else:
	endwon()