import os

in_file = open("./data/gyms.csv","r")
temp = in_file.read().splitlines()
in_file.close()

cities = []
tempcities =[]

loadgymfunction = ""

for i in range(0,len(temp)):
	d = temp[i].split(",")
	tempcities.append(d[3])
	
cities = list(set(tempcities))

cityoption = ""
			
cities.sort()

for i in range(0,len(cities)):
	cityoption = cityoption +"city.options[city.options.length] = new Option(\""+cities[i]+"\",\""+cities[i]+"\");\n"

	
	
out_file = open("./data/city.txt","w")
out_file.write(cityoption)
out_file.close()

out_file = open("./data/citylist.txt","w")
for i in range(0,len(cities)):
	out_file.write(cities[i]+"\n")
out_file.close()