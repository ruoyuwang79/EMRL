from rule import *
import random, math

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

class Agent(Position):
	def __init__(self, x, y, mwh = 100, numds = 1, weights = []):
		self.x = int(x)
		self.y = int(y)
		self.weights = [1 / mwh, 1 / mwh, 1 / numds]
		if weights:
			self.weights = weights
		self.alpha = 0.5
		self.discount = 0.9

	def __add__(self, other):
		return Agent(self.x + other.x, self.y + other.y, weights = self.weights)

	def takeAction(self, action):
		self.x += action.x
		self.y += action.y

	def getLegalActions(self, building):
		return [action for action in Actions.directions if agents_position(self + action, building.grid, building.danger_sources)]

	def getFeatures(self, action, building):
		return [distance_to_exit(self + action, building.exits), distance_to_danger(self + action, building.danger_sources), danger_condition(self + action, building.grid, building.danger_sources)]

	def getValue(self, building):
		actions = self.getLegalActions(building)
		values = []
		for action in actions:
			values.append(self.getQValue(action, self.getFeatures(action, building)))
		return max(values)

	def getQValue(self, action, features):
		return sum(self.weights[i] * features[i] for i in range(len(self.weights)))

	def getPolicy(self, building):
		actions = self.getLegalActions(building)
		return max(actions, key = lambda x: self.getQValue(x, self.getFeatures(x, building)))

	def Astar(self, building, target):
		legalActions = self.getLegalActions(building)
		if Actions.WEST in legalActions and target.y < self.y:
			return Actions.WEST
		elif Actions.SOUTH in legalActions and target.x > self.x:
			return Actions.SOUTH
		else:
			return random.choice(legalActions)
	   
	def update(self, action, reward, features, building):
		diff = (reward + self.discount * (self + action).getValue(building) - self.getQValue(action, features))
		
		for i in range(len(features)):
			self.weights[i] += self.alpha * diff * features[i]

class Actions:
	NORTHWEST = Position(-1, -1)
	NORTH = Position(-1, 0)
	NORTHEAST = Position(-1, 1)
	WEST = Position(0, -1)
	STOP = Position(0, 0)
	EAST = Position(0, 1)
	SOUTHWEST = Position(1, -1)
	SOUTH = Position(1, 0)
	SOUTHEAST = Position(1, 1)

	directions = [NORTH, WEST, STOP, EAST, SOUTH]

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
			return 2, 90

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

				rand = random.random()

				if rand > 0.1:

					continue

				distance2danger_center = math.sqrt((self.danger_center.x - pos.x) ** 2 + (self.danger_center.y - pos.y) ** 2)

				if distance2danger_center <= self.extension_range and (pos not in self.danger_area):

					self.danger_area.append(pos)

class Building:
	def __init__(self, blueprint, exits, danger_centers, agents):
		# the blueprint of the building, should not be changed
		self.grid = Grid(blueprint)
		self.exits = list(Position(exit[0], exit[1]) for exit in exits)

		# need to update, the period can be determined by the main
		self.danger_sources = list(Danger_Source(danger) for danger in danger_centers)
		self.agents = list(Agent(agent[0], agent[1], max(len(self.grid.grid), len(self.grid.grid[0])), len(danger_centers)) for agent in agents)

	def update(self):
		for danger_source in self.danger_sources:
			danger_source.danger_extension(self.grid)
		# how to update agents states
		for agent in self.agents:
			# actions = agent.getLegalActions(self)
			# for action in actions:
			# 	agent.update(action, get_reward(agent, self.exits), agent.getFeatures(action, self), self)
			# agent.takeAction(agent.getPolicy(self))
			agent.takeAction(agent.Astar(self, Position(37, 26)))
			if agent in self.exits:
				self.agents.remove(agent)


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
