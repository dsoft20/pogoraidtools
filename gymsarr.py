import os

in_file = open("./data/gyms.csv","r")
temp = in_file.read().splitlines()
in_file.close()

arr = "var gymsarr = ["

for i in range(0,len(temp)):
	if i < len(temp)-1:
		arr = arr+"\""+temp[i]+"\","
		
	if i == len(temp)-1:
		arr = arr+"\""+temp[i]+"\"];"
				
out_file = open("./data/gymsarr.txt","w")
out_file.write(arr)
out_file.close()