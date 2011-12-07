from random import random
class NeuralNetwork:
	def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
		self.input_layer = [inputNode() for i in range(input_nodes)]
		self.hidden_layer = [hiddenNode() for i in range(hidden_nodes)]
		self.output_layer = [outputNodes() for i in range(output_nodes)]
		self.learning_rate = learning_rate
		self.input_layer.weights = [random() for i in self.hidden_layer]
		self.hidden_layer.weights = [random() for i in self.output_layer]
	
	def forward_propagate(input_data, expected_output, image_resolution):
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
			if self.output_layer[i].letter == expected_output:
				self.output_layer[i].error = 1 - self.output_layer[i].input
			else:
				self.output_layer[i].error = abs(0 - self.output_layer[i].input)
		
		predicted_letter = max(self.output_layer[i] for i in self.output_layer).letter
			
	def backpropagate():
		
	def sigmoid(x):
		return 1/(1+math.exp(-x))