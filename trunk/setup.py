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
		


# Perceptron

# 10 x 10 array
template = 