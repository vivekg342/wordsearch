import random
import string

class Grid:

	def __init__(self, wid, hgt):
		"""
		Initializes the grid and fills with random letters
		"""
		if wid <=0 or hgt <=0:
			raise ValueError('wid and hgt need to be positive integers')
		self.wid = wid
		self.hgt = hgt
		self.data = [None] * (wid * hgt)
		self.letter_index = {l: [] for l in string.ascii_lowercase}
		self.fill()

	def to_text(self):
		"""
		Converts the grid in human readable format.
		"""
		result = []
		for row in range(self.hgt):
			result.append(' '.join(self.data[row * self.wid :(row + 1) * self.wid]))

		return '\n'.join(result)

	def fill(self):
		"""
		Fills the grid with random letters and stores
		"""
		for p in range(self.wid * self.hgt):
				random_letter = random.choice(string.ascii_lowercase)
				self.data[p] = random_letter
				self.letter_index[random_letter].append(p)


	def get_next_pos(self, word, pos, direction, x, y):
		"""
		Calculates the next position based on direction parameter
		(0: vertical, 1: horizontal, 2: diagonal down, 3: diagonal up)
		"""
		increment, dimension  = divmod(direction, 4)
		increment  = -1 if increment > 0 else 1
		if dimension == 0:
			y = y + increment
		elif dimension == 1:
			x = x + increment
		elif dimension == 2:
			x = x + increment
			y = y + increment
		elif dimension == 3:
			x = x + increment
			y = y - increment
		return x,y

	def _search_in_direction(self, word, direction, pos=1, x=0, y=0):
		"""
		Recursively checks for word traversing in four possible directions
		"""

		# Comptes the next position
		x, y = self.get_next_pos(word, pos, direction, x, y)

		# Returns False if out of bounds
		if x < 0  or x >= self.wid or y<0  or y >= self.hgt: return False

		# Returns False if positional alphabet doesn't match
		if word[pos] != self.data[y*self.wid + x]: return False

		# If all alphabets match return True
		if pos == len(word)-1: return True

		return self._search_in_direction(word, direction, pos+1, x, y)


	def search(self, word):
		"""
		searches the grid for a specific word in a DFS fashion
		"""

		arr = self.letter_index[word[0]]
		if len(arr)==0: return False
		for coord in arr:
			y, x = divmod(coord, self.wid)
			for direction in range(8):
				if self._search_in_direction(word, direction, 1, x, y):
					return True
		return False

