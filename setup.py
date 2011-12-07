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
    #print([leftBound, rightBound, topBound, bottomBound])
    #print(rightBound)
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

# Defines the number of vertical/horizontal blocks
resolution = 10



# Training Data
# Load in training images - 50x50px Images

a_Data = imageData('a.png', resolution)
# And so forth for every training image...

print(a_Data)

training_data = [(a_Data, 'A')] # , (b_Data, 'B'), ...]
                
## TODO: Add more letters ##

# Neural Network

# Input Layer - Initialized for each image - Nothing to do here

# Hidden Layer
hidden_nodes = 63 # May be adjusted to find sweet spot
hiddenLayer = [hiddenNode(hidden_nodes) for i in range(hidden_nodes)]

# Output Layer - A node for each letter in the alphabet
outputLayer = [outputNode(26, i) for i in range(26)]

# Forward Propagation
# Begin adding in items from the training set.

# Total input nodes = total blocks: vertical * horizontal
input_nodes  = resolution**2
for i in training_data:
        inputLayer = [inputNode(training_data[i][0][j/10][j%10]) for j in range(input_nodes)]
        inputValues = [inputLayer[j].value for j in inputLayer]
        for j in hiddenLayer:
                hiddenLayer[j].setInputs = inputValues
        hiddenValues = [hiddenLayer[j].output for j in hiddenLayer]
        for j in outputLayer:
                outputLayer[j].setInputs = hiddenValues
        predictedLetter = max([outputLayer[j] for j in outputLayer]).letter
       # if predictedLetter == training_data[i][1]:
                #We made a match
        #else:
                

# Backpropagation



##      TODO    ##
