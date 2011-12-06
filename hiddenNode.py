import math
from random import random

class hiddenNode:
	def __init__(self, num_nodes):
		self.weightsIn = [random() for i in num_nodes]
		
	def adjustWeight(input, error):
		self.weights[input] -= error 

	def output():
                return sigmoid_func(sum([self.inputs[i]*self.weights[i] for i in self.weights]))
	
	def sigmoid_func(h):
		return 1/(1+math.exp(-h))
		
	def setInputs(inputs):
		self.inputs = inputs
