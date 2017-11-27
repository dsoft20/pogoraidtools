# pogoraidtools
A simple tool to share little reports for pogo raids!

**Preview**

![screenshot](https://i.imgur.com/dr7MEZN.jpg)

The tool is written in python3 and generates a static html page.

**Usage:**

1. Edit the **gym.csv** in the **./data/** folder to add your local gyms!
The format of the csv is:
Gym name, latitude, longitude, city
**please do not insert additional commas (,)**
2. Update the pokemon raid list by editing **fivestar.txt, fourstar.txt, threestar.txt, twostar.txt, onestar.txt**, if you want to add a raid boss (for example magikarp that was recently reintroduced) you simply have to edit 
**onestar.txt** from 
```
var onestar = ["Ivysaur","Charmeleon","Wartortle","Metapod","Egg 1*"];
```
to
```
var onestar = ["Magikarp","Ivysaur","Charmeleon","Wartortle","Metapod","Egg 1*"];
```
it's just easy like editing (and it is) a javascript array!

3. Once you have edited the ./data/gym.csv double click to **generate.bat** (or generate.sh [not tested]) to generate the reportraid.html.

4. Now upload everything to your favorite host!

*The page can be translated by editing the file **./data/translation.txt***
