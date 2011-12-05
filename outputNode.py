from random import random

class outputNode:
	def __init__(self, inputs, num_nodes, letterOffset):
		self.inputs = inputs
		self.weights = [random() for i in inputs]
		self.output = self.output()
                self.value = chr(ord('A') + letterOffset)
		
	def adjustWeight(input, error):
		self.weights[input] -= error 

	def output():
                return sum([self.inputs[i]*self.weights[i] for i in self.inputs)
