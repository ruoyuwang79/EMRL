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

def distance_to_danger():
	total = 0
	for agent in building.agents:
		nearest = min(((agent - exit.pos) for exit in building.exits), key = lambda x: x.x + x.y)
		total += nearest.x + nearest.y
	return total
	pass

def possibility_of_danger():
	pass