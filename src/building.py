from rule import *
import random
import math

class Position:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

	def __add__(self, other):
		return Position(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Position(abs(self.x - other.x), abs(self.y - other.y))

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

	def is_in(self,L):

		for item in L:
			if item.x == self.x and item.y == self.y:
				return True

		return False

	# def Around(self): 
	# 	around = [] 
	# 	around.append([[self.x - 1, self.y + 1], [self.x, self.y + 1], [self.x + 1, self.y + 1], [self.x - 1, self.y], [self.x, self.y], [self.x + 1, self.y],[self.x - 1, self.y - 1], [self.x, self.y - 1], [self.x + 1, self.y - 1]]) 
	# 	return around 

class Agent(Position):
	def __init__(self):
		self.weights = []
		self.alpha = 0.2
		self.discount = 0.8

	def evaluation(self, building):
		if agents_position(self, building):
			return find_neighbor_num(self, 4, building) + distance_to_exit(self) + distance_to_danger(self)
		else:
			return -float('inf')

	def update(self, action):
		self.x += action.x
		self.y += action.y
		
	def move(self, action):
		return self + action

	def possible_actions(self, building):
		actions = []
		threshold = 100 # may be programmable
		for action in Actions.directions:
			QValue = self.evaluation(self.move(action), building)
			if QValue > threshold:
				actions.append((action, QValue))

		return sorted(actions, key = lambda x: -x[1])

	####q learning
	def getQValue(self, state, action,feature):
		"""
		  Should return Q(state,action) = w * featureVector
		  where * is the dotProduct operator
		"""
		"*** YOUR CODE HERE ***"
		#feat = self.featExtractor.getFeatures(state,action)
		temp = 0
		for i in feature:#
			temp += self.weights[i]*feature[i]
		return temp

	   
	def update(self, state, action, nextState, reward, feature, building):
		"""
		   Should update your weights based on transition
		"""
		"*** YOUR CODE HERE ***"
		#feat = self.featExtractor.getFeatures(state,action)
		temp = (reward+self.discount*self.computeValueFromQValues(nextState, building)-self.getQValue(state,action))
		for i in feature:
			self.weights[i] += self.alpha * temp * feature[i]

	def computeValueFromQValues(self, state,building):
		"""
		  Returns max_action Q(state,action)
		  where the max is over legal actions.  Note that if
		  there are no legal actions, which is the case at the
		  terminal state, you should return a value of 0.0.
		"""
		"*** YOUR CODE HERE ***"
		temp = {}
		act = self.getLegalActions(state,building)
		if len(act) == 0:
			return float(0)
		for a in act:
			temp[a] = self.getQValue(state,a)

		all_temp = list(temp.items())
        values = [x[1] for x in all_temp]
		return max(values)#temp[temp.argMax()]

	def getLegalActions(self, state, building):
		res = []
		for i in Actions.directions:
			if not building.grid.isWall(state + i):
				res.append(i)
		return res


class Actions:
	NORTHWEST = Position(-1, 1)
	NORTH = Position(0, 1)
	NORTHEAST = Position(1, 1)
	WEST = Position(-1, 0)
	STOP = Position(0, 0)
	EAST = Position(1, 0)
	SOUTHWEST = Position(-1, -1)
	SOUTH = Position(0, -1)
	SOUTHEAST = Position(1, -1)

	directions = [NORTHWEST, NORTH, NORTHEAST, WEST, STOP, EAST, SOUTHWEST, SOUTH, SOUTHEAST]

class Grid:
	def __init__(self, blueprint):
		# blueprint should be a boolean 2-dim array
		self.grid = self.decrease_dim(blueprint)

	def decrease_dim(self, blueprint):
		# if blueprint is high dimension, need to find a method to decrease dimension
		return blueprint

	def isWall(self, position):
		return self.grid[position.x][position.y]

	def getDirections(self, position):
		return [direction for direction in Actions.directions if not self.isWall(position + direction)]

class Danger_Source:
	def __init__(self, danger_center, danger_type = 'fire'):
		self.danger_center = Position(danger_center[0], danger_center[1])
		self.danger_type = danger_type
		self.danger_area = [self.danger_center]
		self.extension_function = self.get_function(danger_type)

		self.extension_speed = None
		self.extension_range = None

	def get_function(self, danger_type):
		# maybe different danger_source have different function
		if danger_type is "fire":
			return 2, 3

		elif danger_type is "gas":
			return 4, 6
			

	def danger_extension(self, grid):
		# will be called in the building periodically
		# use grid.getDirections(somePosition) to get available direction (in list)
		self.extension_speed, self.extension_range = self.get_function(self.danger_type)

		for p in self.danger_area:

			around = [Position(p.x - 1, p.y + 1), Position(p.x, p.y + 1), Position(p.x + 1, p.y + 1), Position(p.x - 1, p.y), Position(p.x, p.y), Position(p.x + 1, p.y),Position(p.x - 1, p.y - 1), Position(p.x, p.y - 1), Position(p.x + 1, p.y - 1)] 

			possible_area = random.sample(around, self.extension_speed)

			for pos in possible_area:

				distance2danger_center = math.sqrt((self.danger_center.x - pos.x) ** 2 + (self.danger_center.y - pos.y) ** 2)

				if distance2danger_center <= self.extension_range and (not pos.is_in(self.danger_area)):

					self.danger_area.append(pos)


class Building:
	def __init__(self, blueprint, exits, danger_centers, agents):
		# the blueprint of the building, should not be changed
		self.grid = Grid(blueprint)
		self.exits = list(Position(exit[0], exit[1]) for exit in exits)

		# need to update, the period can be determined by the main
		self.danger_sources = list(Danger_Source(danger) for danger in danger_centers)
		self.agents = list(Agent(agent[0], agent[1]) for agent in agents)

	def update(self):
		for danger_source in self.danger_sources:
			danger_source.danger_extension(self.grid)
		# how to update agents states
		# for agent in self.agents:
		# 	agent.update()


	def evaluation(self):
		agentsActions = [agent.possible_actions(self) for agent in self.agents]
		if checkIllegal(actions):
			QValue = 0
		return 0
		# use all agents information to get a global programming

	def takeActions(self):
		actions = self.evalution()
		assert(len(actions) == len(self.agents))
		for i in len(self.agents):
			self.agents[i].update(actions[i])
		
		for agent in self.agents:
			if agent in self.exits:
				self.agents.remove(agent)
		# based on evalution, choose an action
