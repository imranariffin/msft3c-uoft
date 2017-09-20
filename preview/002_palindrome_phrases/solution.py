import string

def sanitize(line):
	return "".join([c if c.isalnum() else "" for c in line.lower().strip().replace(" ", "")])

def ispalindrome(line):
	n = len(line)
	for i in range(n/2):
		if line[i] != line[n - i - 1]:
			return False
	return True

def longest_palindrome(line):
	ret = (0, 0)
	maxlen = 0
	for i in range(len(line)):
		for j in range(i + 1, len(line))[::-1]:
			sanitized_line = sanitize(line[i:j])
			lenp = j - i
			# print (i, j), sanitized_line, ispalindrome(sanitized_line)
			if ispalindrome(sanitized_line) and lenp > maxlen:
				maxlen = lenp
				ret = (i, j)

	return ret

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
			print line
			i, j = longest_palindrome(line)
			print line[i:j]
		except (EOFError):
			break