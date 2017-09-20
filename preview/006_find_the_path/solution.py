class Solution:
	def __init__(self, matrix, word):
		self.matrix = matrix
		self.h = len(matrix)
		self.w = len(matrix[0])
		self.word = word
		self.paths = []
		self.visited = set()

	def dfs(self, k, i, j, path):
		if k >= len(self.word):
			return
		if i >= self.h or j >= self.w:
			return
		if (i, j) in self.visited:
			return
		if i == self.h - 1 and j == self.w - 1:
			path.append((i, j))
			self.paths.append(path)
			return
		if matrix[i][j] != self.word[k]:
			return

		self.visited.add((i, j))
		path.append((i, j))
		self.dfs(k + 1, i + 1, j, list(path))
		self.dfs(k + 1, i - 1, j, list(path))
		self.dfs(k + 1, i, j + 1, list(path))
		self.dfs(k + 1, i, j - 1, list(path))

	def finalize(self):
		traversed = set()
		for path in self.paths:
			for i, j in path:
				traversed.add((i, j))

		for i in range(self.h):
			for j in range(self.w):
				if (i, j) not in traversed:
					self.matrix[i][j] = '.'
	
	def print_matrix(self):
		for row in self.matrix:
			print "".join(row)

if __name__ == '__main__':
	word = raw_input()
	matrix = []
	while True:
		try:
			row = []
			for c in raw_input():
				row.append(c)
			matrix.append(row)
		except (EOFError):
			break

	s = Solution(matrix, word)
	s.dfs(0, 0, 0, [])
	s.finalize()
	s.print_matrix()
	