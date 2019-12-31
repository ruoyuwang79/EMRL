import data, income 
EXIT_INDEX = data.EXIT_INDEX; 

def PeopleMove(p, allPeople, direction): 
	flag = Can_Move(p,allPeople,direction) 
	if flag: 
		if direction == 0: 
			p.x = p.x - 1 
			p.y = p.y + 1 
		elif direction == 1: 
			p.y = p.y + 1 
		elif direction == 2: 
			p.x = p.x + 1 
			p.y = p.y + 1 
		elif direction == 3: 
			p.x = p.x - 1
		elif direction == 4: 
			p.y = p.y 
			p.x = p.x 
		elif direction == 5: 
			p.x = p.x + 1 
		elif direction == 6: 
			p.x = p.x - 1 
			p.y = p.y - 1 
		elif direction == 7: 
			p.y = p.y - 1
		elif direction == 8: 
			p.x = p.x + 1 
			p.y = p.y - 1 
	else: 
		p.y = p.y 
		p.x = p.x

def InExit(p, allPeople): 
	for exit in EXIT_INDEX: 
		if (exit.position[1] == data.ROOM_N or exit.position[1] == 0) and (exit.position[0] != data.ROOM_M and exit.position[0] != 0 ): 
			if (p.x >= exit.position[0] - exit.width/2 and p.x <= exit.position[0] + exit.width/2) and (p.y == data.ROOM_N or p.y == 0): 
				allPeople.remove(p) 
				break 
		if (exit.position[1] != data.ROOM_N and exit.position[1] != 0 ) and (exit.position[0] == data.ROOM_M or exit.position[0] == 0): 
			if (p.y >= exit.position[1] - exit.width/2 and p.y <= exit.position[1] + exit.width/2) and (p.x == data.ROOM_M or p.x == 0): 
				allPeople.remove(p) 
				break

def Can_Move(p,allPeople,direction): 
	flag = True 
	n_x = p.x 
	n_y = p.y 
	if direction == 0: 
		n_x = p.x - 1 
		n_y = p.y + 1 
	elif direction == 1: 
		n_y = p.y + 1 
	elif direction == 2: 
		n_x = p.x + 1 
		n_y = p.y + 1 
	elif direction == 3: 
		n_x = p.x - 1 
	elif direction == 4: 
		n_x = p.x 
		n_y = p.y 
	elif direction == 5: 
		n_x = p.x + 1 
	elif direction == 6: 
		n_x = p.x - 1 
		n_y = p.y - 1
	elif direction == 7: 
		n_y = p.y - 1 
	elif direction == 8: 
		n_x = p.x + 1 
		n_y = p.y - 1 

	if is_wall(n_x,n_y): 
		return False 
	for p_i in allPeople: 
		if p_i.x == p.x and p_i.y ==p.y: 
			pass 
		else: 
			if n_x == p_i.x and n_y == p_i.y: 
				flag = False 
	return flag

def is_wall(x,y): 
	if(x == data.Danger_center[0] and y == data.Danger_center[1]): 
		return True 
	for exit in EXIT_INDEX: 
		if (exit.position[1] == data.ROOM_N ) and (exit.position[0] != data.ROOM_M and exit.position[0] != 0 ) : 
			if x >= exit.position[0] - exit.width/2 and x <= exit.position[0] + exit.width/2 and (y == data.ROOM_N): 
				return False 
		if (exit.position[1] == 0 ) and (exit.position[0] != data.ROOM_M and exit.position[0] != 0 ) : 
			if x >= exit.position[0] - exit.width/2 and x <= exit.position[0] + exit.width/2 and (y == 0): 
				return False 
		if (exit.position[1] != data.ROOM_N and exit.position[1] != 0) and (exit.position[0] == data.ROOM_M) : 
			if y >= exit.position[1] - exit.width/2 and y <= exit.position[1] + exit.width/2 and (x == data.ROOM_M): 
				return False 
		if (exit.position[1] != data.ROOM_N and exit.position[1] != 0) and (exit.position[0] == 0) : 
			if y >= exit.position[1] - exit.width/2 and y <= exit.position[1] + exit.width/2 and (x==0): 
				return False 
		if x <= 0 or x >= data.ROOM_M or y <= 0 or y >= data.ROOM_N: 
			return True 
		else: 
			return False