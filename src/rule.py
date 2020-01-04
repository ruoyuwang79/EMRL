def congestion(building):
	# how to solve the congestion problem
	# need to take the door size into consideration
	# return a number to evalute the condition
	pass

def distance_to_exit(building):
	total = 0
	for agent in building.agents:
		nearest = min(((agent - exit.pos) for exit in building.exits), key = lambda x: x.x + x.y)
		total += nearest.x + nearest.y
	return total

def distance_to_danger(building):
	total = 0
	for agent in building.agents:	
		min_dis = float('inf')
		for danger_source in building.danger_sources:
			for danger in danger_source.danger_area:
				distance = agent - danger
				if distance.x + distance.y < min_dis:
					min_dis = distance.x + distance.y
		total += min_dis
	return total

def agents_position(building, actions):
	assert(len(building.agents) == len(actions))
	agentsAction = list(zip(building.agents, actions))
	for agent in agentsAction:
		if building.grid.isWwall(agent[0]) or building.grid.isWwall(agent[0].move(agent[1])):
			return False
	return True

def possibility_of_danger(building):
	# Based on Ziqi's model
	pass
