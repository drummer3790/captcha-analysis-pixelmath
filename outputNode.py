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
