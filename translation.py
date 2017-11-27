translationdata =[]

def translate(line):
	global translationdata
	
	if len(translationdata) == 0:
		in_file = open("./data/translation.txt","r")
		translationdata = in_file.read().splitlines()
		in_file.close()
	
	d =[]
	
	for i in range(0, len(translationdata)):
		d = translationdata[i].split(',')
		
		if d[0] in line:
			if len(d) == 2:
				line = line.replace(d[0],d[1])
			else:
				sub = ""
				for i in range(1,len(d)):
					sub = sub + d[i]
		
	return line