d = {
	'a': '2',
	'b': '22',
	'c': '222',
	'd': '3',
	'e': '33',
	'f': '333',
	'g': '4',
	'h': '44',
	'i': '444',
	'j': '5',
	'k': '55',
	'l': '555',
	'm': '6',
	'n': '66',
	'o': '666',
	'p': '7',
	'q': '77',
	'r': '777',
	's': '7777',
	't': '8',
	'u': '88',
	'v': '888',
	'w': '9',
	'x': '99',
	'y': '999',
	'z': '9999',
	' ': '0',
}

n = int(raw_input())

for i in xrange(1, n+1):
	s = ''
	for c in raw_input():
		a = d[c]
		if len(s) and a[0] == s[-1]:
			s += ' '
		s += a
	print 'Case #%s: %s' % (i, s)
