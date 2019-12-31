import math 
import numpy as np 
import data, rule 
EXIT_INDEX = data.EXIT_INDEX 

def Priority(p, allPeople): 
	time_flag = 0 
	update_exits_dis(p) 
	if (p.change==0): 
		update_target(p) 
		update_flow(allPeople) 
		p.change = 5 
	else: 
		p.change -= 1 

	direction_list = which_direction(p) 
	direction = direction_list.index(max(direction_list)) 

	while rule.Can_Move(p, allPeople, direction) != True: 
		direction_list[direction] = -100 
		direction = direction_list.index(max(direction_list)) 
	return direction 

def PedestrianAround(p): 
	around = [] 
	around.append([[p.x - 1, p.y + 1], [p.x, p.y + 1], [p.x + 1, p.y + 1], [p.x - 1, p.y], [p.x, p.y], [p.x + 1, p.y],[p.x - 1, p.y - 1], [p.x, p.y - 1], [p.x + 1, p.y - 1]]) 
	return around 

def update_exits_dis(p): 
	for i in range(len(EXIT_INDEX)): 
		p.exits_dis[i] = math.sqrt((EXIT_INDEX[i].position[0] - p.x) ** 2 + (EXIT_INDEX[i].position[1] - p.y) ** 2) 

def Find_weight(Dis2Exit,Dis2Danger,Width,Flow,DE_min,Dis2R_max,width_max,flow_min,k1,k2,k3,k4): 
	return k1*math.exp(1-Dis2Exit/(DE_min)) +k2*math.exp(1-Dis2R_max/(Dis2Danger))+ k3*math.exp(1-width_max/Width) + k4*math.exp(1- Flow/(flow_min)) 

def update_target(p): 
	ll=[0,0,0] 
	k1=0.7; 
	k2=0.6; 
	k3=0.3 
	k4=0.4; 
	Flow=[]; 
	Width=[]; 
	Dis2Danger=[]; 
	for exit in EXIT_INDEX: 
		Flow.append(exit.flow) 
		Width.append(exit.width) 
		Dis2Danger.append(math.sqrt((exit.position[0] - data.Danger_center[0]) ** 2 + (exit.position[1] - data.Danger_center[1]) ** 2)) 
		#print(Dis2Danger) 
		DE_min= min(list(filter(lambda x : x > 0, p.exits_dis))); 
		Dis2R_max = max(Dis2Danger); 
		width_max = max(Width) 
		flow_min = min(list(filter(lambda x : x > 0, Flow))) 
		for i in range(len(EXIT_INDEX)): 
			ll[i]=Find_weight(p.exits_dis[i],Dis2Danger[i],EXIT_INDEX[i].width,EXIT_INDEX[i].flow,DE_min,Dis2R_max,width_max,flow_min,k1,k2,k3,k4) 

		if ll[0] == max(ll): 
			p.target=EXIT_INDEX[0].position 
		elif ll[1] == max(ll): 
			p.target=EXIT_INDEX[1].position 
		elif ll[2] == max(ll): 
			p.target=EXIT_INDEX[2].position 

def which_direction(p): 
	around = getPedestrianAround(p)
	direction_list=[] 
	danger_list=[] 
	final = [] 
	for j in around[0]: 
		danger_list.append(math.sqrt((j[0] - data.Danger_center[0]) ** 2 + (j[1] - data.Danger_center[1]) ** 2)) 
		direction_list.append(math.sqrt((j[0] - p.target[0]) ** 2 + (j[1] - p.target[1]) ** 2)) 

		min_direction = min(list(filter(lambda x : x > 0, direction_list))) 
		max_danger = max(danger_list) 
		for i in range(8): 
			final.append( 0.7*math.exp(1-direction_list[i]/(min_direction)) + 0.25*math.exp(1-max_danger/(danger_list[i]+0.0000000000000001) )) 
		return final 

def distance2exit(p,nx,ny): 
	for exit in EXIT_INDEX: 
		if exit.position == p.target: 
			E = exit 
			break 
	dis=[] 
	if p.target[0] == 0 or p.target[0] == data.ROOM_M: #出口在左右 
		for y in range(int(p.target[1]-E.width/2) , int(p.target[1]+E.width/2)): 
			dis.append(math.sqrt((nx - p.target[0]) ** 2 + (ny - y) ** 2)) 

	if p.target[1] == 0 or p.target[1] == data.ROOM_N: #出口在shangxia 
		for x in range(int(p.target[0]-E.width/2) , int(p.target[0]+E.width/2)): 
			dis.append(math.sqrt((nx - x) ** 2 + (ny - p.target[1]) ** 2)) 

	return min(dis) 

def update_flow(allPeople): 
	for exit_i in EXIT_INDEX: 
		exit_i.flow = 0.000000000000 
	for p_i in allPeople: 
		for exit_i in EXIT_INDEX: 
			if p_i.target == exit_i.position: 
				exit_i.flow += 1
				break