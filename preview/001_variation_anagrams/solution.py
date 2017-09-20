import string

def sanitize(line):
	name1, name2 = [name.strip().strip('\"') for name in line.split(",")]
	return name1.lower().replace(" ", ""), name2.lower().replace(" ", "")

def ispotter(name1, name2):
	allchars = set(name1) | set(name2)
	counter1 = {c: 0 for c in allchars}
	counter2 = {c: 0 for c in allchars}

	for c in name1:
		counter1[c] = counter1[c] + 1
	for c in name2:
		counter2[c] = counter2[c] + 1

	for c in allchars:
		if counter1[c] != counter2[c]:
			return "Invalid Pattern"
	return "Valid Pattern"

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
			name1, name2 = sanitize(line)
			print ispotter(name1, name2)
		except (EOFError):
			break