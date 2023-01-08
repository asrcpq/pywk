import sys, os
from pywk import convert

def main():
	file = False
	noexec = False
	assert len(sys.argv) >= 2
	for arg in sys.argv[1:]:
		if arg == "-f":
			file = True
		if arg == "-p":
			noexec = True
	if file:
		prog = open(sys.argv[-1]).read()
	else:
		prog = sys.argv[-1]
	prog = convert(prog)
	if noexec:
		print(prog)
	else:
		exec(prog)

if __name__ == "__main__":
	main()
