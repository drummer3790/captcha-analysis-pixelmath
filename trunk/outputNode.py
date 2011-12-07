from random import random

class outputNode:
	def __init__(self, num_nodes, letterOffset):
		self.weights = [random() for i in inputs]
        self.letter = chr(ord('A') + letterOffset)

	def __str__(self):
		return str(self.letter)
		
	def __lt__(self, other):
		return self.output < other.output
	
	def __gt__(self, other):
		return self.output > other.output
	
	def __eq__(self, other):
		return self.output == other.output
	
	def __ne__(self, other):
		return self.output != other.output
		
	def adjustWeight(input, error):
		self.weights[input] -= error 
