import os
import translation

def loadFile(name):
	openfile = name.replace("##","")
	openfile = openfile.replace("\t","")
	openfile = openfile.replace(" ","")
	in_file = open("./data/" +openfile + ".txt","r")
	temp = in_file.read().splitlines()
	in_file.close()
	
	ext = ""
	for i in range(0,len(temp)):
		ext = ext+temp[i]+"\n"
		
	return ext

in_file = open("base.txt","r")
temp = in_file.read().splitlines()
in_file.close()

raidreport = ""
for i in range(0,len(temp)):
	if "##" not in temp[i]:
		raidreport = raidreport + translation.translate(temp[i])+"\n"
	else:
		raidreport = raidreport + loadFile(temp[i])+"\n"

		
out_file = open("reportraid.html","w")
out_file.write(raidreport)
out_file.close()
		
