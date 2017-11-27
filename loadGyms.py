import os

def order(arr):
	text = ""
	arr = sorted(arr, key=str.lower)
	
	for i in range(0,len(arr)):
		text = text+"\""+ arr[i]+"\""
		if i<len(arr)-1:
			text = text+","

	return text

in_file = open("./data/gyms.csv","r")
temp = in_file.read().splitlines()
in_file.close()

d =[]
in_file = open("./data/citylist.txt","r")
cities = in_file.read().splitlines()
in_file.close()
tempcities =[]
loadgymfunction = ""
citiesgyms = []

for i in range(0,len(cities)):
	citiesgyms.append(list())
	
for i in range(0,len(temp)):
	d = temp[i].split(',')
	
	for cn in range(0,len(cities)):
		if d[3].replace(" ","") == cities[cn].replace(" ",""):			
			citiesgyms[cn].append(d[0])
	
for i in range(0,len(citiesgyms)):
	citiesgyms[i].sort();
	
loadgymfunction = "function loadGyms()\n{\n"

for i in range(0,len(cities)):
	loadgymfunction = loadgymfunction +"var "+cities[i].replace(" ","")+"=["
	for g in range(0,len(citiesgyms[i])):
		if g<len(citiesgyms[i])-1:
			loadgymfunction = loadgymfunction +"\""+citiesgyms[i][g]+"\","
		else:
			loadgymfunction = loadgymfunction +"\""+citiesgyms[i][g]+"\"];\n"

				
loadgymfunction = loadgymfunction +"\nvar ccity = document.getElementById(\"city\");"
loadgymfunction = loadgymfunction +"\nvar gym = document.getElementById(\"gym\");"
loadgymfunction = loadgymfunction +"\ngym.options.length = 0;\n"

for i in range(0,len(cities)):
	loadgymfunction = loadgymfunction + "\nif (ccity.value == \""+ cities[i]+"\")\n{\n"
	loadgymfunction = loadgymfunction + "\tfor (i =0;i<"+ cities[i].replace(" ","")+".length;++i)\n\t{\n"
	loadgymfunction = loadgymfunction + "\t\tgym.options[gym.options.length] = new Option("+cities[i].replace(" ","")+"[i],"+cities[i].replace(" ","")+"[i]);\n\t}\n}"


loadgymfunction = loadgymfunction +"\n}"

out_file = open("./data/loadGyms.txt","w")
out_file.write(loadgymfunction)
out_file.close()

