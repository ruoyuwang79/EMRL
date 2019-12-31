import random 
import numpy as np 
import data
import matplotlib.pyplot as plt 

def creatPeople(): 
	allBlock = [] 
	allPeople = [] 
	for i in range(1, data.ROOM_M): 
		for j in range(1, data.ROOM_N): 
			b = data.Block() 
			b.x = i 
			b.y = j 
			if random.random() > 0.05: 
				b.able = True 
			else: b.able = False 
			allBlock.append(b) 

	random.shuffle(allBlock) 
	allPeople = allBlock[:data.PEOPLE_NUMBER] 
	return allPeople