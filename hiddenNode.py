class hiddenNode:
	def __init__(self, value, weight):
		self.value = normalizeValue(value)
		self.weight = weight
		
	def normalizeValue(value):
		return (value / 8388607/2) - 1
		
	def adjustWeight(error):
		return self.weight 
