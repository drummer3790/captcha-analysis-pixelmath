# Load image in
filename = pmGetString('Enter image file name')
inputFile = pmOpenImage(0, filename)

# Bounding box
cutoffvalue = 255 # Color we consider to be not the letter
colIntensity = pmColumnSums(inputFile, 0)
rowIntensity = pmRowSums(inputFile, 0)
leftBound = None
rightBound = None
topBound = None
bottomBound = None

for i in range(len(colIntensity)):
	if (colIntensity[i] / len(rowIntensity) != cutoffvalue) and not leftBound:
		leftBound = i
	if (colIntensity[i] / len(rowIntensity) == cutoffvalue) and leftBound:
		rightBound = i - 1
		
for i in range(len(rowIntensity)):
	if (rowIntensity[i] / len(colIntensity) != cutoffvalue) and not topBound:
		topBound = i
	if (rowIntensity[i] / len(colIntensity) == cutoffvalue) and topBound:
		bottomBound = i - 1

# Training Data
# Defines the number of vertical/horizontal blocks
resolution = 10
# Load in training images - 50x50px Images
a = pmOpenImage(0, 'a.png')
a_Data = [[0 for i in range(resolution)] for j in range(resolution)]
for i in range(len(a_Data)):
	for j in range(len(a_Data)):
		a_Data[j][i] = pixelAvg(a, j * 5, i * 5, (j + 1) * 5, (i + 1) * 5)

# Neural Network

# Input Layer
# Total input nodes = total blocks: vertical * horizontal
input_nodes  = resolution**2
inputLayer = [inputNode(a_Data[i/10][i%10]) for i in range(input_nodes)]

# Hidden Layer
hidden_nodes = 13 # May be adjusted to find sweet spot
inputValues = [inputLayer[i].value for i in inputLayer]
hiddenLayer = [hiddenNode(inputValues, hidden_nodes) for i in range(hidden_nodes)]

# Output Layer - A node for each letter in the alphabet
hiddenValues = [hiddenLayer[i].output for i in hiddenLayer]
outputLayer = [outputNode(hiddenValues, 26, i) for i in range(26)]
match = outputLayer.index(max([outputLayer[i].output for i in outputLayer]))


# Misc. Functions
def pixelAvg(img, x1, y1, x2, y2,):
	sum = 0
	for y in range(y2 + 1):
		for x in range(x2 + 1):
			# Probably need to use pmGetPixel here.
			sum += pmGetPixelQuickly(img, x, y)
	return sum / 25
# Some weight times the pixel value should equal 1
