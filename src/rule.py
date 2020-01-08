# Agent features
def distance_to_exit(agent, exits):
	nearest = min(((agent - exit) for exit in exits), key = lambda x: x.x + x.y)
	return nearest.x + nearest.y

def distance_to_danger(agent, danger_sources):
	min_dis = float('inf')
	for danger_source in danger_sources:
		for danger in danger_source.danger_area:
			distance = agent - danger
			if distance.x + distance.y < min_dis:
				min_dis = distance.x + distance.y
	return min_dis

def danger_condition(agent, grid, danger_sources):
	return sum((1 / ((agent - danger_source.danger_center).x + (agent - danger_source.danger_center).y)) for danger_source in danger_sources)

def agents_position(agent, grid, danger_sources):
	for danger_source in danger_sources:
		if agent in danger_source.danger_area:
			return False
	if grid.isWall(agent):
			return False
	return True

def possibility_of_danger(agent):
	# Based on Ziqi's model
	pass

# Overall features
def find_neighbor_num(agent,d,building):
	total = -1
	for i in building.agents:
		pos = i-agent
		if (pos.x+pos.y) < d:
			total += 1
	return total

def congestion(building):
	# how to solve the congestion problem
	# need to take the door size into consideration
	# return a number to evalute the condition
	total = 0
	d = 4
	for agent in building.agents:
		total += find_neighbor_num(agent,d,building)
	return total

# Help functions
def cross_wall(grid, pos1, pos2):
	pass