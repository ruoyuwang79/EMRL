import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider, Button, RadioButtons 
import building, initialpedestrian 
exits= building.EXIT_INDEX 

def draw_main(Peoples,time_after_step): 
	plt.clf() 
	draw_wall() 
	plt.xlabel('%s %d' % ('Time Step: ', time_after_step) ,color='k',fontsize='x-large',fontweight='bold') 
	draw_exit() 
	drawPeople(Peoples) 
	if time_after_step == 0 or time_after_step == 10 or time_after_step == 40 or time_after_step == 80 or time_after_step == 100 or time_after_step == 20 or time_after_step == 60: 
		plt.savefig("%d.png" %time_after_step ) 
	if data.FLAG == False: 
		plt.close() 
	else: 
		plt.pause(0.1) 

def drawPeople(P): 
	P_x_able = [] 
	P_y_able= [] 
	P_x_disable = [] 
	P_y_disable = [] 
	for p in P: 
		if p.able: 
			P_x_able.append(p.x) 
			P_y_able.append(p.y) 
		else: 
			P_x_disable.append(p.x) 
			P_y_disable.append(p.y) 
	plt.scatter(P_x_able, P_y_able, c = 'b', marker='*',s=5) 
	plt.scatter(P_x_disable, P_y_disable, c='b', marker='*',s=5) 

def draw_wall(): 
	plt.plot([0, data.ROOM_M], [0, 0], 'k-') 
	plt.plot([0,data.ROOM_M],[data.ROOM_M,data.ROOM_M],'k-') 
	plt.plot([0, 0], [0, data.ROOM_N], 'k-') 
	plt.plot([data.ROOM_M, data.ROOM_M], [0, data.ROOM_N], 'k-') 
	plt.scatter(data.Danger_center[0],data.Danger_center[1],c = 'r', marker='D',s=30) 

def draw_exit(): 
	if len(exits) == 1: 
		plt.plot([exits.position[0] - e.width/2,exits.position[0] + e.width/2],[exits.position[1],exits.position[1]],'w-',linewidth = 2) 
	else: 
		for e in exits: 
			exit_list = [] 
			if int(e.position[0]) != 0 and e.position[0] != data.ROOM_M: 
				e_x_0 = e.position[0] - e.width / 2 
				e_x_1 = e.position[0] + e.width / 2 
				exit_list.append(([e_x_0,e.position[1]]))
				exit_list.append(([e_x_1,e.position[1]])) 
			if e.position[1] != 0 and e.position[1] != data.ROOM_M: 
				e_y_0 = e.position[1] - e.width / 2 
				e_y_1 = e.position[1] + e.width / 2 
				exit_list.append(([e.position[0],e_y_0])) 
				exit_list.append(([e.position[0],e_y_1])) 
			plt.plot([exit_list[0][0],exit_list[1][0]],[exit_list[0][1],exit_list[1][1]],'g+',linewidth=4) 
			plt.plot([exit_list[0][0],exit_list[1][0]],[exit_list[0][1],exit_list[1][1]],'w-',linewidth=3) 

if __name__ == '__main__': 
	draw_main()