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
				
		# Overall error equation? : E(x) = 0.5 * sum([output_layer[i].value for i in output_layer] ** 2)
		self.net_error = 0.5 * sum([output_layer[i].value for i in output_layer] ** 2)
		
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

class InputNode:
	def set_value(self, value):
		# This magic number should be half of the maximum value of pmGetPixelQuickly
		self.value = (value / 8388607.5) - 1
class HiddenNode: pass

class OutputNode:
	def __init__(self, letterOffset):
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

# Misc. Functions

#Returns coordinates of bounding box as [leftBound, rightBound, topBound, bottomBound].
def boundingBox(inputFile, cutoffvalue):
    colIntensity = pmColumnSums(inputFile, 0)
    rowIntensity = pmRowSums(inputFile, 0)
    print(colIntensity)
    print(rowIntensity)
    leftBound = None
    rightBound = None
    bottomBound = None
    topBound = None
    for i in range(len(colIntensity)):
		if (colIntensity[i] / len(rowIntensity) != cutoffvalue) and not leftBound:
			leftBound = i
        if (colIntensity[i] / len(rowIntensity) == cutoffvalue) and leftBound and not rightBound:
            rightBound = i
      	# print([leftBound, rightBound, topBound, bottomBound])
        # print(rightBound)
    for i in range(len(rowIntensity)):
        if (rowIntensity[i] / len(colIntensity) != cutoffvalue) and not bottomBound:
          bottomBound = i
        if (rowIntensity[i] / len(colIntensity) == cutoffvalue) and bottomBound and not topBound:
          topBound = i
        #print([leftBound, rightBound, topBound, bottomBound])
		print([bottomBound, topBound])
    return [leftBound, rightBound, bottomBound, topBound]


# Returns the length along a given dimension of one block inside the bounding box.
# Postcondition: returns an integer.
def blockLength(bound1, bound2, resolution):
    length = (bound2 - bound1 + 1) / resolution
    # Converts block sizes to integers to prevent the wrong data type being inputted into PixelMath methods later.
    # Hopefully this conversion won't affect the values inputted to the input nodes too much.
  	length = int(length)
	return length


# Given the name of an image and the desired resolution, returns the data for each block of the letter in said image.
# Precondition: Parameter imageName must be in '' quotes
# Precondition: This really only works for images containing one capial letter and nothing else but a solid-color background.
# Postcondition: Returns a 2D array.
def imageData(imageName, resolution):
	image = pmOpenImage(0, imageName)
	imageBoundingBox = boundingBox(image, 255)

	leftBound = imageBoundingBox[0]
	rightBound = imageBoundingBox[1]
	bottomBound = imageBoundingBox[2]
	topBound = imageBoundingBox[3]
	
	print(imageBoundingBox)
  
  	# Defines the height and width of each block inside the bounding box subject to the given resolution.
  	blockLengthX = blockLength(leftBound, rightBound, resolution)
  	blockLengthY = blockLength(bottomBound, topBound, resolution) # Assumes the point (0, 0) is at top left corner of image
  	print([blockLengthX, blockLengthY])
  	image_Data = [[0 for i in range(resolution)] for j in range(resolution)]
  	for j in range(len(image_Data)):
    	for i in range(len(image_Data)):
      		print([j, i])
      		# This should be tested to see if my math for the pixelAvg() parameters is correct.
      		image_Data[j][i] = pixelAvg(image, leftBound + i * blockLengthX, bottomBound + j * blockLengthY, leftBound + (i + 1) * blockLengthX - 1, bottomBound + (j + 1) * blockLengthY - 1)
      		print(image_Data[j][i])
  	return image_Data


# Returns the average pixel color/intensity value over the defined rectangle.
# This should be tested; specifically, to make sure the denominator in the average equation is correct.
# Precondition: The rectangle defined by x1, y1, x2, and y2 is a block.
def pixelAvg(img, x1, y1, x2, y2):
	print([x1, y1, x2, y2])
  	sum = 0
  	for y in range(y1, y2 + 1):
    	for x in range(x1, x2 + 1):
      		# Probably need to use pmGetPixel here
      		errortest = pmGetPixel(img, x, y)[0]
      		sum += pmGetPixelQuickly(img, x, y)
  	return sum / ((x2 - x1 + 1) * (y2 - y1 + 1)) # Assumes the point (0, 0) is at bottom left corner of image
# Some weight times the pixel value should equal 1

# Load image in
#filename = pmGetString('Enter image file name')
#inputFile = pmOpenImage(0, filename)

# Bounding box
#inputFileBoundingBox = boundingBox(inputFile, 255)

# Training Data
# Load in training images - 50x50px Images

a_Data = imageData('a.png', resolution)
# And so forth for every training image...

print(a_Data)

training_data = [(a_Data, 'A')] # , (b_Data, 'B'), ...]

## TODO: Add more letters ##

###### CONSTANTS ######
resolution = 10 # Defines the number of vertical/horizontal blocks
input_nodes = resolution ** 2 # Image is split up blocks spanning 10 x 10 
output_nodes = 26 # One for each character of the alphabet (UPPERCASE ONLY!)
hidden_nodes = (input_nodes + output_nodes) / 2 # A starting point... may require fine tuning.
# Initialize the network
network = NeuralNetwork(input_nodes, hidden_nodes, output_nodes)
# Run through training data...
epoch = 0 # Used to determine how many times we have ran through the training data.
while True:
	for datum in training_data:
		predicted_character forward_propagate(datum[0], datum[1])
		backward_propagate()
	#### START STATS LINES #### 
	print 'Pass: ' + str(epoch) + ' Predicted Character: ' + str(predicted_character) \
	 	+ ' Current network error rate is: ' + str(network.net_error) + '%'
	#### END STATS LINES ####	
	epoch += 1
	if network.net_error <= 0.05 or epoch > 100:
		break
# Network should be trained to data...