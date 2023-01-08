import tokenize, io

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
