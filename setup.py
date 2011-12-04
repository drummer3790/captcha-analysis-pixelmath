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


# Neural Network
 
 inputNodes = []



# 10 x 10 array
template = [[0 for i in range(10)] for j in range(10)]
# Perceptron Learning

# Load in training images
a = pmOpenImage(0, 'a.png')
a_Data = [[0 for i in range(10)] for j in range(10)]
for i in range(len(a_Data)):
	for j in range(len(a_Data)):
		a_Data[j][i] = pixelAvg(a, j * 5, i * 5, (j + 1) * 5, (i + 1) * 5)
threshold = 0.5
learnRate =
weights = [0 for i in range(100)]
training_set = [

def pixelAvg(img, x1, y1, x2, y2,):
	sum = 0
	for y in range(y2 + 1):
		for x in range(x2 + 1):
			# Probably need to use pmGetPixel here.
			sum += pmGetPixelQuickly(img, x, y)
	return sum / 25
# Some weight times the pixel value should equal 1