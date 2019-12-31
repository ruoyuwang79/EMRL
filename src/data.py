class Block(): 
	def __init__(self): 
		self.x = 0 
		self.y = 0 
		self.initial_flag = True 
		self.position_dic = [] 
		self.change = 0
		self.is_wall= False
		self.able = True 
		self.exits_dis = [0,0,0]
		self.target = []

class Exit(object): 
	def __init__(self, width,position): 
		self.width = width
		self.position=position
		self.flow = 0.0000000000001
		
FLAG = True 
ROOM_M = 100 
ROOM_N = 100 
Danger_center = [80,60] 
PEOPLE_DENSITY = 0.03 
PEOPLE_NUMBER = int(ROOM_M * ROOM_N * PEOPLE_DENSITY) 
Exit_1 = Exit(8,[30, 100])
Exit_2 = Exit(6,[100,70])
Exit_3 = Exit(8,[0,30])
EXIT_INDEX=[Exit_1, Exit_2, Exit_3]