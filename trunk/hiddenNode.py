import math
from random import random

class hiddenNode:
	def __init__(self, inputs, num_nodes):
		self.inputs = inputs
		self.weightsIn = [random() for i in num_nodes]
		self.output = output()
		
	def adjustWeight(input, error):
		self.weights[input] -= error 

	def output():
                return sigmoid_func(sum([self.inputs[i]*self.weights[i] for i in self.weights]))
	
	def sigmoid_func(h):
		return 1/(1+math.exp(-h))
