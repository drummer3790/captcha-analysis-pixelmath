# coding=utf-8
import math
from random import random
debug_file = open('debug','w')
class NeuralNetwork:
        def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
                self.input_layer = [InputNode() for i in range(input_nodes)]
                self.hidden_layer = [HiddenNode() for i in range(hidden_nodes)]
                self.output_layer = [OutputNode(i) for i in range(output_nodes)]
                self.learning_rate = learning_rate
                for node in self.input_layer:
                        node.weights = [random() for i in self.hidden_layer]
                for node in self.hidden_layer:
                        node.weights = [random() for i in self.output_layer]
        
        def forward_propagate(self, input_data, expected_output, epoch):
                # Setup input nodes
                for i in range(len(self.input_layer)):
						self.input_layer[i].set_value(input_data[i/10][i%10])
						#self.input_layer[i].value = self.sigmoid(input_data[i/10][i%10])
						debug_file.write('Normalized input value for input: ' + str(i) + ' = ' + str(self.input_layer[i].value) + '\n')
						self.input_layer[i].output = [self.input_layer[i].value * \
                                self.input_layer[i].weights[j] for j in range(len(self.input_layer[i].weights))]
						debug_file.write('Input nodes output: ' + str(i) + ' = ' + str(self.input_layer[i].output) + '\n')
                
                # Setup hidden nodes
                for i in range(len(self.hidden_layer)):
                        self.hidden_layer[i].input = sum([self.input_layer[j].output[i]
                                for j in range(len(self.input_layer))])
                        debug_file.write('Hidden Input Value: ' + str(self.hidden_layer[i].input) + '\n')
                        self.hidden_layer[i].value = self.sigmoid(self.hidden_layer[i].input)
                        self.hidden_layer[i].output = [self.hidden_layer[i].value * \
                                self.hidden_layer[i].weights[j] for j in range(len(self.hidden_layer[i].weights))]
                        
                        debug_file.write('Calculated Hidden Value: ' + str(self.hidden_layer[i].value) + '\n')
                
                # Setup output nodes
                for i in range(len(self.output_layer)):
						self.output_layer[i].input = sum([self.hidden_layer[j].output[i] \
							for j in range(len(self.hidden_layer))])
						self.output_layer[i].value = self.sigmoid(self.output_layer[i].input)
						debug_file.write('Output Input Value: ' + str(self.output_layer[i].input) + '\n')
						debug_file.write('Calculated Output Value: ' + str(self.output_layer[i].value) + '\n')
						self.output_layer[i].target = 1 if self.output_layer[i].letter == expected_output else 0 
						self.output_layer[i].error = self.output_layer[i].target - self.output_layer[i].value
						debug_file.write('Calculated error value: ' + str(self.output_layer[i].error) + '\n')   
                # Overall error equation : E(x) = 0.5 * sum([output_layer[i].error for i in output_layer] ** 2)
                self.net_error = 0.5 * sum([self.output_layer[i].error ** 2 for i in range(len(self.output_layer))])

        '''This is essentially the same as forward propagate, except here we will not check target or calculate error'''
        def predict(self, input_data):
                # Setup input nodes
                for i in range(len(self.input_layer)):
                        self.input_layer[i].set_value(input_data[i/10][i%10])
                        self.input_layer[i].output = [self.input_layer[i].value * \
                                self.input_layer[i].weights[j] for j in range(len(self.input_layer[i].weights))]
                
                # Setup hidden nodes
                for i in range(len(self.hidden_layer)):
                        self.hidden_layer[i].input = sum([self.input_layer[j].output[i]
                                for j in range(len(self.input_layer))])
                        self.hidden_layer[i].value = self.sigmoid(self.hidden_layer[i].input)
                        self.hidden_layer[i].output = [self.hidden_layer[i].value * \
                                self.hidden_layer[i].weights[j] for j in range(len(self.hidden_layer[i].weights))]
                
                # Setup output nodes
                for i in range(len(self.output_layer)):
                        self.output_layer[i].input = sum([self.hidden_layer[j].output[i]
                                for j in range(len(self.hidden_layer))])
                        self.output_layer[i].value = self.sigmoid(self.output_layer[i].input)
                return max([self.output_layer[i] for i in range(len(self.output_layer))]).letter
        
        def backpropagate(self):
                # Starting at output....
                for i in range(len(self.output_layer)):
						self.output_layer[i].delta = self.output_layer[i].error * \
                                self.sigmoid_prime(self.output_layer[i].value)
						debug_file.write('Delta for output node: ' + str(i) + ' = ' + str(self.output_layer[i].delta) + '\n')
						debug_file.write('Calculated value for output node: ' + str(i) + ' = ' + str(self.output_layer[i].value) + '\n')
						debug_file.write('Sigmoid Prime value for output node: ' + str(i) + ' = ' + str(self.sigmoid_prime(self.output_layer[i].value)) + '\n')
						debug_file.write('Error value for output node: ' + str(i) + ' = ' + str(self.output_layer[i].error) + '\n')
						
						self.output_layer[i].deltaW = learning_rate * (self.output_layer[i].delta) * \
                                self.output_layer[i].value
                # Hidden Nodes....
                for i in range(len(self.hidden_layer)):
						sum_output_deltas = sum([(self.output_layer[j].delta * self.hidden_layer[i].weights[j]) \
                                        for j in range(len(self.hidden_layer[i].weights))])
						self.hidden_layer[i].delta = self.sigmoid_prime(self.hidden_layer[i].value) * sum_output_deltas
						debug_file.write('Delta for hidden node: ' + str(i) + ' = ' + str(self.hidden_layer[i].delta) + '\n')
						debug_file.write('Calculated value for hidden node: ' + str(i) + ' = ' + str(self.hidden_layer[i].input) + '\n')
						debug_file.write('Sigma Prime value for hidden node: ' + str(i) + ' = ' + str(self.sigmoid_prime(self.hidden_layer[i].input)) + '\n')
						debug_file.write('Output Delta Sum: ' + str(i) + ' = ' + str(sum_output_deltas) + '\n')
						if self.hidden_layer[i].delta > 1:
							debug_file.write('WOAH! Delta for layer ' + str(i) + ' is : ' + str(self.hidden_layer[i].delta) + '\n')
						self.hidden_layer[i].deltaW = learning_rate * (self.hidden_layer[i].delta) * \
                                self.hidden_layer[i].value
                # Update Weights...
                # Input Layer...
                for i in range(len(self.input_layer)):
                        for j in range(len(self.hidden_layer)):
								self.input_layer[i].weights[j] += self.hidden_layer[j].deltaW
								
                # Hidden Layer...
                for i in range(len(self.hidden_layer)):
                        for j in range(len(self.output_layer)):
								self.hidden_layer[i].weights[j] += self.output_layer[j].deltaW

        def sigmoid(self, x):
                return 1/(1+math.exp(-x))
				#return math.tanh(x)
        
        def sigmoid_prime(self, x):
                return self.sigmoid(x)*(1 - self.sigmoid(x))
				#return 1.0 - self.sigmoid(x)**2

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
                return self.value < other.value
                                       
        def __gt__(self, other):       
                return self.value > other.value
                                   
        def __le__(self, other):       
                return self.value <= other.value
                                       
        def __ge__(self, other):       
                return self.value >= other.value
                                       
        def __eq__(self, other):       
                return self.value == other.value
                                       
        def __ne__(self, other):       
                return self.value != other.value

# Misc. Functions

#Returns coordinates of bounding box as [leftBound, rightBound, topBound, bottomBound].
def boundingBox(inputFile, cutoffvalue):
	colIntensity = pmColumnSums(inputFile, 0)
	# rowIntensity[0] is TOP row!
	rowIntensity = pmRowSums(inputFile, 0)
	leftBound = None
	rightBound = None
	bottomBound = None
	topBound = None

	for i in range(len(colIntensity)):
		if (colIntensity[i] / len(rowIntensity) != cutoffvalue) and not leftBound:
			leftBound = i
		if (colIntensity[i] / len(rowIntensity) == cutoffvalue) and leftBound and not rightBound:
			rightBound = i
	for i in range(len(rowIntensity)): # 
		# bottomBound: first row with any red in it.
		if (rowIntensity[i] / len(colIntensity) != cutoffvalue) and not topBound:
			topBound = len(rowIntensity) - i
		# topBound: first row after bottomBound without any red in it.
		if (rowIntensity[i] / len(colIntensity) == cutoffvalue) and topBound and not bottomBound:
			bottomBound = len(rowIntensity) - i
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
  
        # Defines the height and width of each block inside the bounding box subject to the given resolution.
        blockLengthX = blockLength(leftBound, rightBound, resolution)
        blockLengthY = blockLength(bottomBound, topBound, resolution) # Assumes the point (0, 0) is at top left corner of image
        image_Data = [[0 for i in range(resolution)] for j in range(resolution)]
        for j in range(len(image_Data)):
                for i in range(len(image_Data)):
                        # This should be tested to see if my math for the pixelAvg() parameters is correct.
                        image_Data[j][i] = pixelAvg(image, leftBound + i * blockLengthX, bottomBound + j * 
							blockLengthY, leftBound + (i + 1) * blockLengthX - 1, bottomBound + (j + 1) * 
								blockLengthY - 1)
        return image_Data


# Returns the average pixel color/intensity value over the defined rectangle.
# This should be tested; specifically, to make sure the denominator in the average equation is correct.
# Precondition: The rectangle defined by x1, y1, x2, and y2 is a block.
def pixelAvg(img, x1, y1, x2, y2):
        sum = 0
        for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                        # Probably need to use pmGetPixel here
                        errortest = pmGetPixel(img, x, y)[0]
                        sum += pmGetPixelQuickly(img, x, y)
        return sum / ((x2 - x1 + 1) * (y2 - y1 + 1)) # Assumes the point (0, 0) is at bottom left corner of image
# Some weight times the pixel value should equal 1

# Bounding box

# Training Data
# Load in training images - 50x50px Images
resolution = 10 # Defines the number of vertical/horizontal blocks
training_data = []
###### CONSTANTS ######
input_nodes = resolution ** 2 # Image is split up blocks spanning 10 x 10 
output_nodes = 5 # One for each character of the alphabet (UPPERCASE ONLY!)
for i in range(output_nodes):
	current_letter = str(chr(ord('A') + i))
	training_data.append((imageData('test_set/'+ current_letter +'.png', resolution), current_letter))
hidden_nodes = (input_nodes + output_nodes) / 2 # A starting point... may require fine tuning.
learning_rate = 0.1 # Again this may need to be adjusted...
# Initialize the network
network = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
# Run through training data...
epoch = 1 # Used to determine how many times we have ran through the training data.
print 'Now training the neural network...'
while True:
        for datum in training_data:
                debug_file.write(str(datum[1])+'\n')
                predicted_character = network.forward_propagate(datum[0], datum[1], epoch)
                network.backpropagate()  
		#print 'Epoch#: ' + str(epoch) + ' - Current Network Error Rate is: ' + str(network.net_error)
		epoch += 1
        if network.net_error <= 0.05 or epoch > 1000:
                break
# Network should be trained to data...

# Try something new...
##### This is merely left over test code #####
#basic_captcha_a = imageData('captchas/basic_captcha_a.png', resolution)
#easy_captcha_a = imageData('captchas/easy_captcha_a.png', resolution)
#new_font_captcha_a = imageData('captchas/new_font_captcha_a.png', resolution)
#new_font_captcha_b = imageData('captchas/new_font_captcha_b.png', resolution)
#hard_captcha_a = imageData('captchas/hard_captcha_a.png', resolution)
#test_set_c = imageData('test_set/c.png', resolution)
#basic_captcha_x = imageData('captchas/basic_captcha_x.png', resolution)
#new_data = [(basic_captcha_a, 'A'), (easy_captcha_a, 'A'), (new_font_captcha_a, 'A'),\
#        (new_font_captcha_b, 'B'), (hard_captcha_a, 'A'), (basic_captcha_x, 'X')]
#new_data = [(basic_captcha_a, 'A'), (easy_captcha_a, 'A'), (new_font_captcha_a, 'A'),\
#        (new_font_captcha_b, 'B'), (hard_captcha_a, 'A'), (test_set_c, 'C')]
#for datum in training_data:
#        predicted_character = network.predict(datum[0])
#        print 'This image contains the character: ' + str(predicted_character)
#        print 'Is this the expected output? '
#        if predicted_character == datum[1]:
#                print 'Yes.'
#        else:
#                print 'No.'
				
# User Input:
# Load image in
print 'Please select an image for recognition.'
filename = pmGetString('Enter image file name')
new_captcha = imageData(filename, resolution)
predicted_character = network.predict(new_captcha)
print 'This image contains the character: ' + str(predicted_character)