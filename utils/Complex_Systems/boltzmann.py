import random as rnd
import time 
import os
import numpy as np
import matplotlib.pyplot as plt
 
class board:
	def __init__(self,nrows=5,ncols=5):
		self.nrows = nrows
		self.ncols = ncols
		self.nodes = [5 for i in range(nrows*ncols)]
	def print(self):
		i = 0
		for element in self.nodes:
			print(element, end=' ')
			i += 1
			if i == self.ncols:
				print('\n')
				i = 0
	def neighbors(self,pos):
		neighbors = []
		if pos in range(0,self.ncols*self.nrows,self.ncols):
			neighbors.append([pos + 1])
		elif pos in range(self.ncols-1,self.ncols*self.nrows,self.ncols):
			neighbors.append([pos - 1])
		else:
			neighbors.append([pos + 1])
			neighbors.append([pos - 1])
		if pos in range(self.ncols):
			neighbors.append([pos + self.ncols])
		elif pos in range(self.ncols*(self.nrows-1),self.ncols*self.nrows):
			neighbors.append([pos - self.ncols])
		else:
			neighbors.append([pos + self.ncols])
			neighbors.append([pos - self.ncols])
		return neighbors
	def evolve(self):
		for row in range(self.nrows):
			for col in range(self.ncols):
				pos = col + self.ncols*row
				neighbour = rnd.choice(self.neighbors(pos))[0]
				if rnd.uniform(0,1) < 0.5:
					self.nodes[pos] += 1
					if self.nodes[neighbour] > 0:
						self.nodes[neighbour] -= 1
				else:
					if self.nodes[pos] > 0:
						self.nodes[pos] -= 1
					self.nodes[neighbour] += 1
	def data(self):
		x = np.arange(0, max(self.nodes))
		y = np.zeros(max(self.nodes))
		for element in self.nodes:
			y[element-1] += 1
		return x,y
		
myboard = board(100, 100)	

for i in range(25):
	myboard.evolve()	
data = myboard.data()
plt.plot(data[0],data[1])
plt.show()