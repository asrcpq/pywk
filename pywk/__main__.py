import sys, io, os
import tokenize

def convert(pywk_prog):
	prog = ""
	indent_level = 0
	toks = tokenize.tokenize(io.BytesIO(pywk_prog.encode()).read)
	for t in toks:
		# print(t)
		lf = False
		normal_print = False
		indent_change = 0
		if t.type == tokenize.OP and t.string == ";":
			lf = True
		elif t.type == tokenize.OP and t.string == "{":
			lf = True
			indent_change = 1
		elif t.type == tokenize.OP and t.string == "}":
			lf = True
			indent_change -= 1
		elif t.type == tokenize.NEWLINE:
			lf = True
		elif t.type != tokenize.ENCODING:
			normal_print = True

		indent_level += indent_change
		assert indent_level >= 0
		if indent_change == 1:
			prog += ":"
		if lf:
			prog += "\n" + "\t" * indent_level
		if normal_print:
			prog += t.string + " "
	return prog

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
