from random import random
class NeuralNetwork:
	def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
		self.input_layer = [inputNode() for i in range(input_nodes)]
		self.hidden_layer = [hiddenNode() for i in range(hidden_nodes)]
		self.output_layer = [outputNodes(i) for i in range(output_nodes)]
		self.learning_rate = learning_rate
		self.input_layer.weights = [random() for i in self.hidden_layer]
		self.hidden_layer.weights = [random() for i in self.output_layer]
	
	def forward_propagate(input_data, expected_output):
		# Setup input nodes
		for i in input_layer:
			self.input_layer[i].set_value(input_data[i])
			self.input_layer[i].output = [self.input_layer[i].value * \
				self.input_layer[j].weights for j in self.input_layer.weights]
		
		# Setup hidden nodes
		for i in self.hidden_layer:
			self.hidden_layer[i].input = sum([self.input_layer[j].output[i]
			 	for j in self.input_layer])
			self.hidden_layer[i].value = sigmoid(self.hidden_layer[i].input)
			self.hidden_layer[i].output = [self.hidden_layer[i].value * \
				self.hidden_layer.weights[j] for j in self.hidden_layer.weights]
		
		# Setup output nodes
		for i in self.output_layer:
			self.output_layer[i].input = sum([self.hidden_layer[j].output[i]
				for j in self.hidden_layer])
			self.output_layer[i].value = sigmoid(self.output_layer[i].input)
			# Error = tk - outk
			if self.output_layer[i].letter == expected_output:
				self.output_layer[i].error = 1 - self.output_layer[i].input
			else:
				self.output_layer[i].error = abs(0 - self.output_layer[i].input)
		
			# Returns the letter it predicted
			return max(self.output_layer[i] for i in self.output_layer).letter
			
	def backpropagate():
		# ∆wij = ηδj outj
		# If output node: δj = (tj − outj )g'j(hj)
		# Else: δj = g'j(hj)sum(δkwk) over k
		# Starting at output....
		for i in self.output_layer:
			self.output_layer[i].delta = self.output_layer[i].error * 
				sigmoid_prime(self.output_layer[i].value)
			self.output_layer[i].deltaW = learning_rate * (self.output_layer[i].delta) * 
				self.output_layer[i].value
		# Hidden Nodes....
		for i in self.hidden_layer:
			self.hidden_layer[i].delta = sigmoid_prime(self.hidden_layer[i].value) * 
				sum([self.output_layer[i].delta * self.hidden_layer[i].weights[j]
					for j in self.hidden_layer[i].weights)
			self.hidden_layer[i].deltaW = learning_rate * (self.hidden_layer[i].delta) * 
				self.hidden_layer[i].value
		# Update Weights...
		# Input Layer...
		for i in self.input_layer:
			for j in self.hidden_layer:
				self.input_layer[i].weights[j] += self.hidden_layer[j].deltaW
		# Hidden Layer...
		for i in self.hidden_layer:
			for j in self.output_layer:
				self.hidden_layer[i].weights[j] += self.output_layer[j].deltaW

	def sigmoid(x):
		return 1/(1+math.exp(-x))
		
	def sigmoid_prime(x):
		return sigmoid(x)*(1 - sigmoid(x))