from random import random

class outputNode:
	def __init__(self, num_nodes, letterOffset):
		self.weights = [random() for i in inputs]
        self.letter = chr(ord('A') + letterOffset)
		self.inputs = None
		self.output = None
	
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

	def output():
        return sum([self.inputs[i]*self.weights[i] for i in self.inputs)
	
	def setInputs(inputs):
		self.inputs = inputs
		self.output = output()
