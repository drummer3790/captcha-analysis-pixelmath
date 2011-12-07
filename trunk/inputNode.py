class inputNode:
	def set_value(self, value):
		# This magic number should be half of the maximum value of pmGetPixelQuickly
		self.value = (value / 8388607.5) - 1
