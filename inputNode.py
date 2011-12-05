class inputNode:
	def __init__(self, value):
		self.value = normalizeValue(value)
		
	def normalizeValue(value):
	        return (value / 8388607/2) - 1
