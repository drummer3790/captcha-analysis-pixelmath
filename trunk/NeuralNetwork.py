class NeuralNetwork:
	def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
		self.input_nodes = [inputNode() for i in range(input_nodes)]
		self.hidden_nodes = [hiddenNode() for i in range(hidden_nodes)]
		self.output_nodes = [outputNodes() for i in range(output_nodes)]
		self.learning_rate = learning_rate
	
	def forward_propagate(input, expected_output, image_resolution):
		# Setup input nodes
		input_nodes = image_resolution**2
		for i in input:
			self.input_nodes[i].set_value(input[i])
		
		# Setup hidden nodes
		for i in self.hidden_nodes:
			
		
		# Setup output nodes
	def backpropagate():
		
	def sigmoid(x):
		return 1/(1+math.exp(-x))