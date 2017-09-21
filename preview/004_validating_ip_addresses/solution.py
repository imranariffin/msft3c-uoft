import math
MIN_IP_VALUE = 0
MAX_IP_VALUE = int(math.pow(255, 3))*255 + int(math.pow(255, 2))*255
MAX_IP_VALUE += int(math.pow(255, 1))*255 + int(math.pow(255, 0))*255

def parse(line):
	"""
	@param line: string
	@rvalue: list(tuple(int))
	"""
	return [tuple([int(t) for t in ip.split(".")]) for ip in line.split(" ")]

def convert(ip):
	"""
	@param ip: list[int]
	@rvalue: int
	"""
	t1, t2, t3, t4 = ip[0], ip[1], ip[2], ip[3]
	t1, t2 = int(math.pow(255, 3)) * t1, int(math.pow(255, 2)) * t2
	t3, t4 = int(math.pow(255, 1)) * t3, t4
	num = t1 + t2 + t3 + t4
	return num

def isvalid(line):
	"""
	@param line: string
	@rvalue: boolean
	"""
	ip = line.split(" ")[2]
	terms = filter(lambda e: e != "", ip.split("."))
	if len(terms) < 4:
		return False
	terms = [int(t) for t in terms]
	for t in terms:
		if t > 255 or t < 0:
			return False
	ip = convert(terms)
	# print ip
	if ip < MIN_IP_VALUE or ip > MAX_IP_VALUE:
		return False
	return True

def isinrange(ipmin, ipmax, ip):
	"""
	@param ipmin: tupple(integer, integer, integer, integer)
	@param ipmax: tupple(integer, integer, integer, integer)
	@param ip: tupple(integer, integer, integer, integer)
	@rvalue: string
	"""
	ipmin, ipmax, ip = convert(ipmin), convert(ipmax), convert(ip)
	if ip < ipmin or ip > ipmax:
		return "OutRange"
	return "InRange"

if __name__ == '__main__':
	while True:
		try:
			line = raw_input()
			if not isvalid(line):
				print "InValid"
			else:
				minip, maxip, ip = parse(line)
				print isinrange(minip, maxip, ip)
		except (EOFError):
			break